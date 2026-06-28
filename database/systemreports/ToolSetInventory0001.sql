select ToolSetInventory.Quantity, ToolSetInventory.Price, tools.Code, tools.Brand, provider.name 
  from ToolSetInventory  
  Join tools on tools.IdTool = ToolSetInventory.IdTool
  join Provider on provider.IdProvider = ToolSetInventory.IdProvider;