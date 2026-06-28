Select Provider.Name "Provider", Tools.Name "Tool Name", Borrower.Name "Borrower", Loan.BorrowDate 
  From Loan 
  Join Borrower On Borrower.IdBorrower = Loan.IdBorrower
  Join ToolSetInventory On ToolSetInventory.IdInventory = Loan.IdInventory
  Join Provider On Provider.IdProvider = ToolSetInventory.IdProvider
  Join Tools On Tools.IdTool = ToolSetInventory.IdTool;