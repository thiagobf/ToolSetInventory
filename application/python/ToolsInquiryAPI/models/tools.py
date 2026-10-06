



class ToolsModel:
    

    def __init__(self, id: int, name: str, description: str, quantity: int):
        self.id = id
        self.name = name
        self.description = description
        self.quantity = quantity

    @staticmethod
    def FindToolById(id: int):
        from repositories.tool_repository import ToolRepository

        return ToolRepository().get_tool_by_id(id)

    @staticmethod
    def FindToolList() -> list["ToolsModel"]:
        from repositories.tool_repository import ToolRepository

        return ToolRepository().get_tools()

    