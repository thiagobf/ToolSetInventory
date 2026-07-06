import sqlite3
from enum import Enum

DB_NAME = r".\database\sqlitedb\toolsetinventory.db"

class BrandCode(Enum): 
    NONBRAND = "NOB"
    BOSCH = "BOS"
    DEWALT = "DEW"
    MAKITA = "MAK"
    MILWAUKEE = "MIL"
    RYOBI = "RYO"
    BLACK_DECKER = "BLD"
    HITACHI = "HIT"
    PORTER_CABLE = "PTC"
    SKIL = "SKL"
    METABO = "MET"
    STAMACO = "STA"
    STARRET = "STT"
    DANNY = "DAN"
    TRAMONTINA = "TRA"
    FERRARI = "FER"
    DEXTER = "DEX"
    IRWIN = "IRW"
    DREMEL = "DRE" 
    WESTERN = "WES"

def get_brand_code(brand_name):
    brand_name = brand_name.upper()
    for brand in BrandCode:
        if brand.name == brand_name:
            return brand.value
    return BrandCode.NONBRAND.value

def generate_tool_code(brand_code, tool_name):
    tool_name = tool_name.upper()
    code = f"{brand_code}-{tool_name[:3]}"
    return code

def generate_tool_numcode(tool_code,indextool):
    tool_code = tool_code.upper()
    code = f"{tool_code}-{indextool:05d}"
    return code

def LoadFile():
    RecordsList = []
    Record = []
    with open(".\\database\\rawdata\\tools.csv", "r",encoding='utf-8') as file:
        for line in file:
            RecordsList.append(line.strip())
            
        for Record in RecordsList:
            Record = Record.split(";")
            Brand = Record[0].upper()
            Name = Record[1]
            Description = Record[2]

        print("Brand: ", Brand)
        print("Name: ", Name)
        print("Code: ", generate_tool_numcode(generate_tool_code(get_brand_code(Brand), Name), 1))
        print("Description: ", Description)

def loadTools(brand, code, name, description, price):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO Tools (brand, code, name, description, price) VALUES (?, ?, ?, ?, ?)", (brand, code, name, description, price))
    print(f"Inserted: {brand}, {code}, {name}, {description}, {price}")
    conn.commit()
    conn.close()


LoadFile()
#loadTools("Bosch", "BOS-001", "Cordless Drill", "18V Cordless Drill with battery and charger", 99.99)
