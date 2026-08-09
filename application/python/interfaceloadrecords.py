import sqlite3
from datetime import datetime
from enum import Enum

DB_NAME = r".\database\sqlitedb\toolsetinventory.db"


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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

class LoadRecords(): 
    def __init__(self):
        self.size = 20
        self.MakerHash =  [[] for _ in range(self.size)]

    def _GenerateHash(self, KeyMaker):
        return hash(KeyMaker) % self.size
    
    def insertMaker(self, KeyMaker):
        index = self._GenerateHash(KeyMaker)
        if self.MakerHash[index] is None:
            self.MakerHash[index] = []
        self.MakerHash[index].append(KeyMaker)

    def searchMaker(self, KeyMaker):
        index = self._GenerateHash(KeyMaker)
        if self.MakerHash[index] is not None:
            for maker in self.MakerHash[index]:
                if maker == KeyMaker:
                    return True
        return False
    
    def generate_unique_code(self, Maker):
        index = self._GenerateHash(Maker)
        if self.MakerHash[index] is None:
            self.MakerHash[index] = []
        self.MakerHash[index].append(Maker)
        unique_code = f"{Maker[:3].upper()}-{len(self.MakerHash[index]):05d}"
        return unique_code
    
    def get_brand_code(self, brand_name):
        brand_name = brand_name.upper()
        for brand in BrandCode:
            if brand.name == brand_name:
                return brand.value
        return BrandCode.NONBRAND.value

    def generate_tool_code(self, brand_code, tool_name):
        tool_name = tool_name.upper()
        UniqueCode = self.generate_unique_code(brand_code)
        return UniqueCode

    def generate_tool_numcode(self, tool_code, indextool):
        tool_code = tool_code.upper()
        code = f"{tool_code}-{indextool:05d}"
        return code

    def loadToolsInDB(self, brand, code, name, description, price):
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("INSERT INTO Tools (brand, code, name, description, price) VALUES (?, ?, ?, ?, ?)", (brand, code, name, description, price))
        conn.commit()
        conn.close()

    def LoadFile(self):
        RecordsList = []
        Record = []
        print(f"[{get_timestamp()}] <<Loading records from file>>")
        with open(".\\database\\rawdata\\tools.csv", "r",encoding='utf-8') as file:
            for line in file:
                RecordsList.append(line.strip())
                
            for Record in RecordsList:
                Record = Record.split(";")
                Brand = Record[0].upper()
                Name = Record[1]
                Description = Record[2]
                price = float(Record[3].replace(",","."))
                ToolCode = self.generate_tool_code(Brand, Name)
                self.loadToolsInDB(Brand, ToolCode, Name, Description, price)




if __name__ == "__main__":
    print(f"[{get_timestamp()}] Begin Loading Records")
    print("*******************************")
    print(f"[{get_timestamp()}] Instantiating LoadRecords class")
    LoadRecord = LoadRecords()
    print(f"[{get_timestamp()}] Loading records from file")
    LoadRecord.LoadFile()
    print("*******************************")
    print(f"[{get_timestamp()}] Loading records completed")
    print(f"[{get_timestamp()}] End of Loading Records")

#loadTools("Bosch", "BOS-001", "Cordless Drill", "18V Cordless Drill with battery and charger", 99.99)
