import sqlite3

class Database:
    def __init__(self, file):
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()

    def listMieter(self):
        return self.cursor.execute("SELECT * FROM Mieter").fetchall()
    
    def listVermieter(self):
        return self.cursor.execute("SELECT * FROM Vermieter").fetchall()
    
    def listWohnungen(self, land="", stadt="", betten=""):
        query = "SELECT * FROM Vermieter, Wohnungen WHERE Vermieter.VermieterID == Wohnungen.VermieterID"
        if land != "":
            query += " AND Wohnungen.Land == '" + land + "'"
        if stadt != "":
            query += " AND Wohnungen.Stadt == '" + stadt + "'" 
        if betten != "":
            query += " AND Wohnungen.betten >= " + betten + ""
        return self.cursor.execute(query).fetchall()

    def listBuchungen(self):
        return self.cursor.execute("SELECT Buchungen.BuchungsID, Mieter.MieterID, Mieter.name, Wohnungen.WID, Buchungen.Datum FROM Buchungen, Mieter, Wohnungen WHERE Buchungen.WohnungsID = Wohnungen.WID").fetchall()

    def select(self, query):
       return self.cursor.execute(query).fetchall()
    
    
    def addVermieter(self, data=(str, str)):
        self.cursor.execute(f"INSERT INTO \"main\".\"Vermieter\" (\"Name\", \"Email\") VALUES (\'{data["name"]}\', \'{data["email"]}\')")
        self.connection.commit()

    def addMieter(self, data=(str, str)):
        self.cursor.execute(f"INSERT INTO \"main\".\"Mieter\" (\"Name\", \"Email\") VALUES (\'{data["name"]}\', \'{data["email"]}\')")
        self.connection.commit()

    def addWohnung(self, data):
        self.cursor.execute(f"INSERT INTO \"main\".\"Wohnungen\" (\"Stadt\", \"Land\", \"Betten\", \"VermieterID\") VALUES (\'{data["stadt"]}\', \'{data["land"]}\', \'{data["betten"]}\', \'{data["vid"]}\')")
        self.connection.commit()
    
    def addBuchung(self, data):
        self.cursor.execute(f"INSERT INTO \"main\".\"Buchungen\" (\"WohnungsID\", \"MieterID\", \"Datum\") VALUES (\'{data["wid"]}\', \'{data["mid"]}\', \'{data["datum"]}\')")
        self.connection.commit()

        

db = Database("datenbank/db.sqlite")
res = db.listWohnungen(betten="5")
for i in res:
    print(i)
    
