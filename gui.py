from tkinter import * 
from tkinter import ttk

import sqlinterface


class App:
    def __init__(self, db):
        self.root = Tk()
        self.root.title("BnB Clone") # Titel setzen
        self.database = sqlinterface.Database(db)

        self.loginpage = LoginPage(self.root, self)
        self.mieterpage = MieterPage(self.root, self)
        self.vermieterpage = VermieterPage(self.root, self)
    
    def run(self):
        self.root.mainloop()
    

class LoginPage:
    def __init__(self, master, app):
        master.geometry("350x500")
        self.master = master
        self.app = app
        self.total = ttk.Frame(self.master)
        self.total.grid()

        self.firstFrame = ttk.Frame(self.total)    
        
        self.firstBanner = ttk.Label(self.firstFrame, 
                                     text="Login Page"
                                     )
        self.firstBanner.grid(row=0, column=0, columnspan=3)
        
        self.mieterButton = ttk.Button(self.firstFrame, 
                                       text="Einloggen als Mieter", 
                                       command=lambda: self.showLogin(mieter=True)
                                       )
        self.mieterButton.grid(row=1, column=0)
        
        self.vermieterButton = ttk.Button(self.firstFrame, 
                                          text="Einloggen als Vermieter", 
                                          command=lambda: self.showLogin(mieter=False)
                                          )
        self.vermieterButton.grid(row=1, column=2)

        ttk.Button(self.firstFrame, text="Neu Registirien", command= lambda: [self.firstFrame.grid_forget(), self.registerPage()]).grid(row=2, column=1)
        
        self.closeButton = ttk.Button(self.firstFrame, 
                                      text="Schließen", 
                                      command=self.total.grid_forget
                                      )
        self.closeButton.grid(row=3, column=1)
        

        self.firstFrame.grid()

    def registerPage(self):
        self.firstBanner.grid_forget()
        self.registerFrame = ttk.Frame(self.total)
        self.registerFrame.grid()

        ttk.Label(self.registerFrame, text="Registrieren")
        mieterState = BooleanVar()
        ttk.Radiobutton(self.registerFrame, text="Mieter", variable=mieterState, value=True).grid(row=1, column=0)
        ttk.Radiobutton(self.registerFrame, text="Vermieter", variable=mieterState, value=False).grid(row=1, column=1)

        ttk.Label(self.registerFrame, text="Email").grid(row=2, column=0)
        self.emailEntry = ttk.Entry(self.registerFrame)
        self.emailEntry.grid(row=2, column=1)

        ttk.Label(self.registerFrame, text="Name").grid(row=3, column=0)
        self.nameEntry = ttk.Entry(self.registerFrame)
        self.nameEntry.grid(row=3, column=1)    

        x = lambda d: self.app.database.addMieter(d) if mieterState.get() else self.app.database.addVermieter(d)

        ttk.Button(self.registerFrame, text="Account erstellen", command= lambda: [print({"name": self.nameEntry.get(), "email": self.emailEntry.get()}), x({"name": self.nameEntry.get(), "email": self.emailEntry.get()}), self.registerFrame.grid_forget(), self.showLogin(mieterState.get())]).grid() 



    def showLogin(self, mieter):
        print(f"Einloggen als {'Mieter' if mieter else 'Vermieter'}")
        self.firstFrame.grid_forget()

        self.loginFrame = ttk.Frame(self.total)

        self.loginBanner = ttk.Label(self.loginFrame, 
                                      text=f"Einloggen als {'Mieter' if mieter else 'Vermieter'}"
                                      )
        self.loginBanner.grid(row=0, column=0)
        
        self.EmailField = ttk.Entry(self.loginFrame)
        self.EmailField.grid(row=1, column=0)
        

        self.loginButton = ttk.Button(self.loginFrame, text="Anmelden", command=lambda: self.anmelden(mieter)) # anmelde funktion
        self.loginButton.grid(row=1, column=1)

        self.backButton = ttk.Button(self.loginFrame, 
                                     text="Zurück", 
                                     command= lambda: [self.loginFrame.grid_forget(), self.firstFrame.grid()]
                                     )
        self.backButton.grid(row=2, column=0)

        self.loginFrame.grid()

    def anmelden(self, mieter):
        print(self.EmailField.get())
        print("Anmelden als", "Mieter" if mieter else "Vermieter")

        if mieter:
            res = self.app.database.select(f"SELECT * FROM Mieter WHERE Email == '{self.EmailField.get()}'")
            if res == []:
                print("User existiert nicht")
                ttk.Label(self.loginFrame, text="falsche Email").grid()
            else:
                global mieterID
                mieterID = res[0]
                print(mieterID)
                self.loginFrame.grid_forget()
                self.firstFrame.grid()
                self.total.grid_forget()
                self.app.mieterpage.total.grid()
                self.app.mieterpage.startpage.grid()
        else:
            res = self.app.database.select(f"SELECT * FROM Vermieter WHERE Email == '{self.EmailField.get()}'")
            if res == []:
                print("User existiert nicht")
                ttk.Label(self.loginFrame, text="falsche Email").grid()
            else:
                global vermieterID
                vermieterID = res[0]
                print(vermieterID)
                self.loginFrame.grid_forget()
                self.firstFrame.grid()
                self.total.grid_forget()
                self.app.vermieterpage.total.grid()
                self.app.vermieterpage.startpage.grid()
                
                


class VermieterPage:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.total = ttk.Frame(self.master)
        

        self.mainpage()

    def mainpage(self):
        
        self.startpage = ttk.Frame(self.total)
        self.startpage.grid()
        ttk.Label(self.startpage, text="Eingeloogt als Vermieter").grid()
        ttk.Button(self.startpage, text="Neue Wohnung listen", command = lambda: [self.startpage.grid_forget(), self.createNewListingPage()]).grid()
        ttk.Button(self.startpage, text="Abmelden", command= lambda: [self.total.grid_forget(), self.app.loginpage.total.grid()]).grid()

    def createNewListingPage(self):
        self.listingPage = ttk.Frame(self.total)
        self.listingPage.grid()

        ttk.Label(self.listingPage, text="Stadt").grid(row=0, column=0)
        self.stadtEntry = ttk.Entry(self.listingPage)
        self.stadtEntry.grid(row=0, column=1)

        ttk.Label(self.listingPage, text="Land").grid(row=1, column=0)
        self.landEntry = ttk.Entry(self.listingPage)
        self.landEntry.grid(row=1, column=1)

        ttk.Label(self.listingPage, text="Betten").grid(row=2, column=0)
        self.bettenEntry = ttk.Entry(self.listingPage)
        self.bettenEntry.grid(row=2, column=1)


        ttk.Button(self.listingPage, text="Erstellen", command= lambda: [self.app.database.addWohnung({"stadt": self.stadtEntry.get(), "land": self.landEntry.get(), "betten": self.bettenEntry.get(), "vid": vermieterID}), self.listingPage.grid_forget(), self.startpage.grid()]).grid()
        ttk.Button(self.listingPage, text="Abbrechen", command= lambda: [self.listingPage.grid_forget(), self.startpage.grid()]).grid()
        
        
        

class MieterPage:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.total = ttk.Frame(self.master)
        
        self.mainpage()
        

    def mainpage(self):
        self.startpage = ttk.Frame(self.total)
        self.startpage.grid()

        self.startpageBanner = ttk.Label(self.startpage,
                                text="Eingeloggt als Mieter")
        self.startpageBanner.grid()

        self.startpageSucheButton = ttk.Button(self.startpage,
                                               text="Suche",
                                               command= lambda: [self.startpage.grid_forget(), self.initsuchpage()])
        self.startpageSucheButton.grid()

        self.startpageAbmeldeButton = ttk.Button(self.startpage, 
                                     text="Abmelden", 
                                     command= lambda: [self.startpage.grid_forget(), self.total.grid_forget(), app.loginpage.total.grid()]
                                     )
        self.startpageAbmeldeButton.grid()


    def initsuchpage(self):
        self.suchPage = ttk.Frame(self.total)
        self.suchPage.grid()

        self.suchpageBanner = ttk.Label(self.suchPage,
                                        text="Suche")
        self.suchpageBanner.grid(row=0, column=0)

        self.suchpageStadtLabel = ttk.Label(self.suchPage, text="Stadt")
        self.suchpageStadtLabel.grid(row=1, column=0)
        self.suchpageStadt = StringVar()

        StadtData = ["Any"] + self.app.database.select("SELECT Stadt from Wohnungen GROUP BY Stadt") #Städte abfragen
        self.suchpageStadtAuswahl = ttk.OptionMenu(self.suchPage, self.suchpageStadt, *StadtData)
        self.suchpageStadtAuswahl.grid(row=1, column = 1)
        
        self.suchpageLandLabel = ttk.Label(self.suchPage, text="Land")
        self.suchpageLandLabel.grid(row=2, column=0)
        self.suchpageLand = StringVar()

        LandData = ["Any"] + self.app.database.select("SELECT Land from Wohnungen GROUP BY Land") # Länder Abfrage

        self.suchpageLandAuswahl = ttk.OptionMenu(self.suchPage, self.suchpageLand, *LandData)
        self.suchpageLandAuswahl.grid(row=2, column = 1)

        self.suchpageBettenLabel = ttk.Label(self.suchPage, text="Betten")
        self.suchpageBettenLabel.grid(row=3, column=0)
        self.suchpageBettenAnzahl = ttk.Entry(self.suchPage)
        self.suchpageBettenAnzahl.grid(row=3, column=1)

        self.suchPageSubmitButton = ttk.Button(self.suchPage, 
                                     text="Suche", 
                                     command= lambda: self.suche()
                                     )
        self.suchPageSubmitButton.grid()
        
        self.suchPageResults = ttk.Frame(self.suchPage)
        self.suchPageResults.grid()

        self.suchPageBackButton = ttk.Button(self.suchPage, 
                                     text="Zurück", 
                                     command= lambda: [self.suchPage.grid_forget(),  self.startpage.grid()]
                                     )
        self.suchPageBackButton.grid()


    def suche(self):
        self.suchPageResults.grid_forget()
        self.suchPageResults = ttk.Frame(self.suchPage)
        self.suchPageResults.grid()

        stadt = self.suchpageStadt.get()
        land = self.suchpageLand.get()
        betten = self.suchpageBettenAnzahl.get()

        print("Stadt:", stadt, "\nLand:", land, "\nBetten:", betten) 

        res = self.app.database.listWohnungen(land=land, stadt=stadt, betten=betten)
        print(res)
        counter = 0
        resgui = []
        for i in res:
            resgui.append((ttk.Label(self.suchPageResults, text=f"Apartment Nr. {i[3]}\n{i[4]}, {i[5]}\nBetten: {i[6]}\n\n"), 
                             ttk.Button(self.suchPageResults, text="Buchen", command= lambda c= i: Buchungsfenster(self.master, self.app, c[3]))))
            resgui[counter][0].grid(row=counter, column=0)
            resgui[counter][1].grid(row=counter, column = 1)
            counter+=1

class Buchungsfenster(Toplevel):
    def __init__(self, master, app, wid):
        super().__init__(master=master)
        self.app = app
        self.title("Buchung")
        self.geometry("200x200")
        ttk.Label(self, text=f"Buchung - {wid}").grid()
        d = [i for i in self.app.database.selectWohnung(wid)[0]]
        print(d)
        ttk.Label(self, text=f"Apartment Nr. {d[0]}\n{d[2]}, {d[1]}\nBetten: {d[3]}\nVermietet von {d[4]}").grid()
        datum = ttk.Entry(self)
        datum.grid()
        ttk.Button(self, text="Buchen", command= lambda: print(f"MieterID: {mieterID}\nWohnungsID: {wid}\nDatum: {datum.get()}")).grid()

app = App("datenbank/db.sqlite")
app.run()
