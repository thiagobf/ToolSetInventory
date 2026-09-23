



class ToolsModel:
    

    def __init__(self, id: int, name: str, description: str, quantity: int):
        self.id = id
        self.name = name
        self.description = description
        self.quantity = quantity

    @staticmethod
    def FindToolById(id: int):
        # Implement the logic to find a tool by its ID in the database
        # For demonstration purposes, let's assume we have a list of tools
        tools = [
            ToolsModel( 1, "Hammer", "A tool for hammering nails", 10),
            ToolsModel( 2, "Screwdriver", "A tool for driving screws", 15),
            ToolsModel( 3, "Wrench", "A tool for tightening bolts", 5),
        ]

        for tool in tools:
            if tool.id == id:
                return tool

        return None