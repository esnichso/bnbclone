from tkinter import * 
from tkinter import ttk



class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("BnB Clone") # Titel setzen

        self.loginpage = LoginPage(self.root, self)
        self.mieterpage = MieterPage(self.root, self)
    
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
        
        self.closeButton = ttk.Button(self.firstFrame, 
                                      text="Schließen", 
                                      command=self.total.grid_forget
                                      )
        self.closeButton.grid(row=2, column=1)
        

        self.firstFrame.grid()


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
        print("Anmelden als", "Mieter" if mieter else "Vermiter")
        self.loginFrame.grid_forget()
        self.firstFrame.grid()
        self.total.grid_forget()
        if mieter:
            self.app.mieterpage.total.grid()
            self.app.mieterpage.startpage.grid()


class MieterPage:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.total = ttk.Frame(self.master)
        
        self.startpage = ttk.Frame(self.total)
        self.startpage.grid()
        self.suchPage = ttk.Frame(self.total)

        self.startpageBanner = ttk.Label(self.startpage,
                                text="Eingeloggt als Mieter")
        self.startpageBanner.grid()

        self.startpageSucheButton = ttk.Button(self.startpage,
                                               text="Suche",
                                               command= lambda: [self.startpage.grid_forget(), self.suchPage.grid()])
        self.startpageSucheButton.grid()

        self.startpageAbmeldeButton = ttk.Button(self.startpage, 
                                     text="Abmelden", 
                                     command= lambda: [self.startpage.grid_forget(), self.total.grid_forget(), app.loginpage.total.grid()]
                                     )
        self.startpageAbmeldeButton.grid()

        self.suchpageBanner = ttk.Label(self.suchPage,
                                        text="Suche")
        self.suchpageBanner.grid()

        self.suchPageBackButton = ttk.Button(self.suchPage, 
                                     text="Zurück", 
                                     command= lambda: [self.suchPage.grid_forget(),  self.startpage.grid()]
                                     )
        self.suchPageBackButton.grid()

app = App()
app.run()
