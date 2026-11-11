import sqlite3
import time
import logging 
from threading import Lock
from pathlib import Path
from typing import List, Optional, Union

from models.tools import ToolsModel


class ToolRepository:
	_tools_cache: dict[Path, tuple[float, tuple[tuple[int, str, str, int], ...]]] = {}
	_tools_cache_lock = Lock()

	def __init__(
		self,
		database_path: Optional[Union[str, Path]] = None,
		cache_ttl_seconds: float = 60.0,
	):
		logging.basicConfig(level=logging.INFO)
		logger = logging.getLogger(__name__)
		logger.info("Initializing ToolRepository")
		project_root = Path(__file__).resolve().parents[4]
		self.database_path = Path(database_path) if database_path else (
			project_root / "database" / "sqlitedb" / "toolsetinventory.db"
		)
		if cache_ttl_seconds < 0:
			raise ValueError("cache_ttl_seconds must be non-negative")
		self.cache_ttl_seconds = cache_ttl_seconds

	def get_tool_by_id(self, tool_id: int) -> Optional[ToolsModel]:
		connection = sqlite3.connect(self.database_path)
		try:
			row = connection.execute(
				"""
				SELECT
					tools.IdTool,
					tools.Name,
					tools.Description,
					COALESCE(SUM(inventory.Quantity), 0) AS Quantity,
					COALESCE(inventory.Price, 0) AS Price
				FROM Tools AS tools
				LEFT JOIN ToolSetInventory AS inventory
					ON inventory.IdTool = tools.IdTool
				WHERE tools.IdTool = ?
				GROUP BY tools.IdTool, tools.Name, tools.Description
				""",
				(tool_id,),
			).fetchone()
		finally:
			connection.close()

		if row is None:
			return None

		logger = logging.getLogger(__name__)
		logger.info(f"Retrieved tool with ID {tool_id}: {row}")
		return ToolsModel(
			id=row[0],
			name=row[1],
			description=row[2],
			quantity=row[3],
			price=row[4]
		)

	def get_tools(self) -> List[ToolsModel]:
		
		cache_key = self.database_path.resolve()
		with self._tools_cache_lock:
			cached = self._tools_cache.get(cache_key)
			now = time.monotonic()
			if cached is not None and cached[0] > now:
				rows = cached[1]
			else:
				connection = sqlite3.connect(self.database_path)
				try:
					rows = tuple(connection.execute(
						"""
						SELECT
							tools.IdTool,
							tools.Name,
							tools.Description,
							COALESCE(SUM(inventory.Quantity), 0),
							Coalesce(inventory.Price, 0) AS Price
						FROM Tools AS tools
						LEFT JOIN ToolSetInventory AS inventory
							ON inventory.IdTool = tools.IdTool
						GROUP BY tools.IdTool, tools.Name, tools.Description
						ORDER BY tools.IdTool
						"""
					).fetchall())
				finally:
					connection.close()

				if self.cache_ttl_seconds > 0:
					self._tools_cache[cache_key] = (
						time.monotonic() + self.cache_ttl_seconds,
						rows,
					)
				else:
					self._tools_cache.pop(cache_key, None)

		logger = logging.getLogger(__name__)
		logger.info(f"Retrieved {len(rows)} tools from the database.")
		return [
			ToolsModel(
				id=row[0],
				name=row[1],
				description=row[2],
				quantity=row[3],
				price=row[4]
			)
			for row in rows
		]

