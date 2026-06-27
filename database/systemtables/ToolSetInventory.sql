drop table ToolSetInventory;
drop table Provider;
drop table Tools;

CREATE TABLE "Tools" (
  "IdTool" Integer PRIMARY KEY AutoIncrement,
  "Brand" char[50],
  "Code" "Char[10]",
  "Name" "Char[50]",
  "Description" "Char[100]",
  "Price" real,
  "CreationDate" timestamp DEFAULT (now())
);

CREATE TABLE "Provider" (
  "IdProvider" Integer PRIMARY KEY AutoIncrement,
  "Name" char[50],
  "Code" char[10],
  "Address" "Char[100]",
  "Country" "Char[50]",
  "Phone" "Char[20]",
  "CreationDate" timestamp DEFAULT (now())
);

CREATE TABLE "ToolSetInventory" (
   "IdInventory" Integer PRIMARY KEY AutoIncrement,
   "IdProvider" Integer,
   "IdTool" Integer,
  "Quantity" Integer DEFAULT '0',
  "Price" Real DEFAULT '0',
  "CreationDate" timestamp DEFAULT (now()),
  FOREIGN KEY(IdProvider) REFERENCES Provider(IdProvider) ,
  FOREIGN KEY(IdTool) REFERENCES Tools(IdTool)
);


