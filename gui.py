from tkinter import * 
from tkinter import ttk

root = Tk()
root.title("BnB Clone") # Titel setzen


class LoginPage:
    def __init__(self, master):
        master.geometry("350x500")
        self.master = master

        self.firstFrame = ttk.Frame(self.master)    
        
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
        """
        self.closeButton = ttk.Button(self.firstFrame, 
                                      text="Schließen", 
                                      command=self.firstFrame.grid_forget
                                      )
        self.closeButton.grid(row=2, column=1)
        """

        self.firstFrame.grid()


    def showLogin(self, mieter):
        print(f"Einloggen als {'Mieter' if mieter else 'Vermieter'}")
        self.firstFrame.grid_forget()

        self.loginFrame = ttk.Frame(self.master)

        self.loginBanner = ttk.Label(self.loginFrame, 
                                      text=f"Einloggen als {'Mieter' if mieter else 'Vermieter'}"
                                      )
        self.loginBanner.grid(row=0, column=0)
        
        self.EmailField = ttk.Entry(self.loginFrame)
        self.EmailField.grid(row=1, column=0)
        

        self.loginButton = ttk.Button(self.loginFrame, text="Anmelden", command=lambda: print(self.EmailField.get())) # anmelde funktion
        self.loginButton.grid(row=1, column=1)

        self.backButton = ttk.Button(self.loginFrame, 
                                     text="Zurück", 
                                     command= lambda: [self.loginFrame.grid_forget(), self.firstFrame.grid()]
                                     )
        self.backButton.grid(row=2, column=0)

        self.loginFrame.grid()

        

    

page = LoginPage(root)

root.mainloop()