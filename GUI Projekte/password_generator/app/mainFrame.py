import customtkinter as ctk
from PIL import Image
from app.loadResourcePath import resource_path

class mainFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent,
             width=750,
             height=625,
             fg_color="#161C22",
             corner_radius=12,
             border_color="#1E262C",
             border_width=2
        )

        self.icon = ctk.CTkLabel(master=self,
             text=None,
             image=ctk.CTkImage(dark_image=Image.open(resource_path("icons/inAppPng.png")), size=(70, 70))
        )
        self.icon.place(anchor="center", relx=0.05, rely=0.095)

        self.appText = ctk.CTkLabel(master=self,
             text="Passwort Generator",
             font=("Calibri", 32, "bold"),
             text_color="#ECEEEF"
        )
        self.appText.place(anchor="center", relx=0.28, rely=0.0845)

        self.sloganText = ctk.CTkLabel(master=self,
             text="Erstelle sichere Passwörter in Sekunden",
             font=("Arial", 12.8),
             text_color="#75889E"
        )
        self.sloganText.place(anchor="center", relx=0.265, rely=0.13)