INSERT INTO "Provider"(Name,Code,Address,Country,Phone) Values('Tony Starck','TS000001','Av. Rio Grande do Sul, 1000, Caraguatatuba, SP','Brasil','19 98136-1712');

INSERT INTO "Tools"(Brand,Code,Name,Description,Price) Values('Makita','MK000001','Furadeira de Impacto','Furadeira de impacto 1/2" 650W',450.00);

INSERT INTO "ToolSetInventory"(IdProvider,IdTool,Quantity,Price) Values(1,1,10,450.00); 

INSERT INTO "Borrower"(Name,Code,Address,Country,Phone) Values('Tony Starck','TS000001','Av. Rio Grande do Sul, 1000, Caraguatatuba, SP','Brasil','19 98136-1712');

INSERT INTO "Loan"(IdInventory,IdBorrower,BorrowDate,DueDate,ReturnDate,Status,LoanPrice) Values(1,1,'2024-06-01 10:00:00','2024-06-10 10:00:00',NULL,1,450.00);
