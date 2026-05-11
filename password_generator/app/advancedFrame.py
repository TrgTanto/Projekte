import customtkinter as ctk
import clipboard, hashlib


class advancedFrame(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.setWindow(500, 500)
        self.resizable(False, False)
        self.title("Hash-Rechner")
        self.hash = ''

        self.bg = ctk.CTkFrame(master=self,
            fg_color="#0F161B",
            width=500,
            height=500
        )
        self.bg.place(anchor="center", relx=0.5, rely=0.5)

        self.main = ctk.CTkFrame(master=self.bg,
            width=480,
            height=480,
            fg_color="#161C22",
            corner_radius=12,
            border_color="#1E262C",
            border_width=2
        )
        self.main.place(anchor="center", relx=0.5, rely=0.5)

        self.titleText = ctk.CTkLabel(master=self.main,
            text="Hash-Rechner",
            font=("Segoe UI Semibold", 20),
            text_color="#EBECEC"
        )
        self.titleText.place(anchor="center", relx=0.5, rely=0.05)

        self.enterPassword = ctk.CTkEntry(master=self.main,
            placeholder_text="Passwort eingeben",
            fg_color="#192025",
            border_color="#242B30",
            border_width=1,
            width=460,
            height=50,
            font=("Helvetica", 13.5),
            justify="center"
        )
        self.enterPassword.place(anchor="center", relx=0.5, rely=0.2)

        self.optionText = ctk.CTkLabel(master=self.main,
            text="Algorithmus",
            font=("Helvetica", 16),
            text_color="#EBECEC"
        )
        self.optionText.place(anchor="center", relx=0.5, rely=0.4)

        self.optionMenu = ctk.CTkOptionMenu(master=self.main,
            width=250,
            height=35,
            values=[
                "MD5",
                "SHA-1",
                "SHA-224",
                "SHA-256",
                "SHA-384",
                "SHA-512",
                "SHA3-224",
                "SHA3-256",
                "SHA3-384",
                "SHA3-512"
            ],
            fg_color="#0D1418",
            font=("Helvetica", 18),
            dropdown_font=("Helvetica", 18),
            button_color="#0D1418",
            button_hover_color="#0D1418",
            dropdown_fg_color="#161C22",
            dropdown_text_color="#EBF0F8",
            dropdown_hover_color="#0D1418",
            anchor="center",
            command=self.optionMenuCalc
        )
        self.optionMenu.place(anchor="center", relx=0.5, rely=0.47)
        self.optionMenu.set("Algorithmus auswählen")

        self.hashButton = ctk.CTkButton(master=self.main,
            text="Noch kein Hash berechnet – bitte starten.",
            text_color="#FCFDFC",
            fg_color="#0D1418",
            hover=False,
            width=460,
            height=40,
            anchor="center",
            font=("Helvetica", 16),
            command=lambda:clipboard.copy(self.hash)
        )
        self.hashButton.place(anchor="center", relx=0.5, rely=0.65)

        self.calcHashText = ctk.CTkLabel(master=self,
            text="",
            font=("Helvetica", 12),
            fg_color="#161C22"
        )
        self.calcHashText.place(anchor="center", relx=0.5, rely=0.8)

    # sets the app in the center of the screen
    def setWindow(self, width: int, height: int):
        screenWidth, screenHeight = self.winfo_screenwidth(), self.winfo_screenheight()
        x = int(((screenWidth / 2) - (width / 2)))
        y = int((screenHeight / 2) - (height / 2))
        self.geometry(f"{width}x{height}+{x}+{y}")

    def optionMenuCalc(self, choice):
        password = self.enterPassword.get().encode("utf-8")

        # if password is empty
        if len(password) == 0:
            self.hashButton.configure(text="Passwort zur Berechnung erforderlich.")
            return
        
        if choice == "MD5":
            x = hashlib.md5(password).hexdigest()

        if choice == "SHA-1":
            x = hashlib.sha1(password).hexdigest()
        
        if choice == "SHA-224":
            x = hashlib.sha224(password).hexdigest()
        
        if choice == "SHA-256":
            x = hashlib.sha256(password).hexdigest()
        
        if choice == "SHA-384":
            x = hashlib.sha384(password).hexdigest()

        if choice == "SHA-512":
            x = hashlib.sha512(password).hexdigest()
        
        if choice == "SHA3-224":
            x = hashlib.sha3_224(password).hexdigest()
        
        if choice == "SHA3-256":
            x = hashlib.sha3_256(password).hexdigest()
        
        if choice == "SHA3-384":
            x = hashlib.sha3_384(password).hexdigest()
        
        if choice == "SHA3-512":
            x = hashlib.sha3_512(password).hexdigest()

        self.hash = x
        hashText = self.hash[:50] + '\n' + self.hash[50:100] + '\n' + self.hash[100:] 
        self.hashButton.configure(text=f"{choice}-Hash erfolgreich erstellt – klicken zum Kopieren")
        self.calcHashText.configure(text=hashText)