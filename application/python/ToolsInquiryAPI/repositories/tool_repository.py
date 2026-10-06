import sqlite3
from pathlib import Path
from typing import List, Optional, Union

from models.tools import ToolsModel


class ToolRepository:
	def __init__(self, database_path: Optional[Union[str, Path]] = None):
		project_root = Path(__file__).resolve().parents[4]
		self.database_path = Path(database_path) if database_path else (
			project_root / "database" / "sqlitedb" / "toolsetinventory.db"
		)

	def get_tool_by_id(self, tool_id: int) -> Optional[ToolsModel]:
		connection = sqlite3.connect(self.database_path)
		try:
			row = connection.execute(
				"""
				SELECT
					tools.IdTool,
					tools.Name,
					tools.Description,
					COALESCE(SUM(inventory.Quantity), 0)
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

		return ToolsModel(
			id=row[0],
			name=row[1],
			description=row[2],
			quantity=row[3],
		)

	def get_tools(self) -> List[ToolsModel]:
		connection = sqlite3.connect(self.database_path)
		try:
			rows = connection.execute(
				"""
				SELECT
					tools.IdTool,
					tools.Name,
					tools.Description,
					COALESCE(SUM(inventory.Quantity), 0)
				FROM Tools AS tools
				LEFT JOIN ToolSetInventory AS inventory
					ON inventory.IdTool = tools.IdTool
				GROUP BY tools.IdTool, tools.Name, tools.Description
				ORDER BY tools.IdTool
				"""
			).fetchall()
		finally:
			connection.close()

		return [
			ToolsModel(
				id=row[0],
				name=row[1],
				description=row[2],
				quantity=row[3],
			)
			for row in rows
		]

