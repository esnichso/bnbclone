
class Wohnungsverzeichnis:
    def __init__(self):
        self.wohnungen = []
    
    def add_wohnung(self, w):
        self.wohnungen.append(w)

    def get_info_all(self):
        for i in self.wohnungen:
            print(i)
            print(i.get_info())
    
    def search_city(self, city):
        return [i for i in self.wohnungen if i.city == city]

class Wohnung:
    def __init__(self, vermieter, city=str, country=str, beds=int):
        self.vermieter = vermieter
        self.city = city
        self.country = country
        self.beds = beds
    
    def get_info(self):
        print(f"Vermieter: {self.vermieter.name}\nStadt: {self.city}\nLand: {self.country}\nBetten: {self.beds}")


class Vermieter:
    def __init__(self, verzeichnis, name, mail):
        self.verzeichnis = verzeichnis
        self.wohnungen = []
        self.name = name
        self.mail = mail
    
    def neue_wohnung(self, city, country, beds):
        w = Wohnung(self, city, country, beds)
        self.wohnungen.append(w)
        self.verzeichnis.add_wohnung(w)
        

    def get_info_all(self):
        for i in self.wohnungen:
            print(i)
            print(i.get_info())

class Mieter:
    def __init__(self, name=str, mail=str):
        self.name = name
        self.mail = mail

    def book(self, wohnung_id):
        pass

allg = Wohnungsverzeichnis()

v1 = Vermieter(allg, "Lucas", "lucas@buschbeck.de")

v1.neue_wohnung("Berlin", "Deutschland", 4)
v1.neue_wohnung("Amsterdam", "Niederlande", 4)
#v1.get_info_all()

print(allg.search_city("Berlin"))