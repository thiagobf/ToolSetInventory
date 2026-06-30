import sqlite3

DB_NAME = r".\database\sqlitedb\toolsetinventory.db"


def loadTools(brand, code, name, description, price):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO Tools (brand, code, name, description, price) VALUES (?, ?, ?, ?, ?)", (brand, code, name, description, price))
    print(f"Inserted: {brand}, {code}, {name}, {description}, {price}")
    conn.commit()
    conn.close()


loadTools("Bosch", "BOS-001", "Cordless Drill", "18V Cordless Drill with battery and charger", 99.99)
