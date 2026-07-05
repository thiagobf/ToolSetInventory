import sqlite3

DB_NAME = r".\database\sqlitedb\toolsetinventory.db"

def LoadFile():
    RecordsList = []
    with open(".\\database\\rawdata\\tools.csv", "r",encoding='utf-8') as file:
        for line in file:
            RecordsList.append(line.strip())
        
        print(RecordsList)

def loadTools(brand, code, name, description, price):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO Tools (brand, code, name, description, price) VALUES (?, ?, ?, ?, ?)", (brand, code, name, description, price))
    print(f"Inserted: {brand}, {code}, {name}, {description}, {price}")
    conn.commit()
    conn.close()

LoadFile()
#loadTools("Bosch", "BOS-001", "Cordless Drill", "18V Cordless Drill with battery and charger", 99.99)
