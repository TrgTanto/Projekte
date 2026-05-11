import customtkinter as ctk
import clipboard, string, secrets
import app.settingFrame as setFrame
from app.loadResourcePath import resource_path

from PIL import Image

class generatorFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent,
             width=725,
             height=235,
             fg_color="#192126",
             corner_radius=12,
             border_color="#1E262C",
             border_width=2
        )
        self.password = ''
        
        self.titleText = ctk.CTkButton(master=self,
            text="Dein Passwort",
            text_color="#EBECEC",
            image=ctk.CTkImage(dark_image=Image.open(resource_path("icons/password.png")), size=(25, 25)),
            font=("Segoe UI Semibold", 17),
            hover="disabled",
            fg_color="transparent",
            width=0,
            height=0
        )
        self.titleText.place(anchor="center", relx=0.105, rely=0.1)

        self.generatedPassword = ctk.CTkButton(master=self,
            text="Noch kein Passwort generiert",
            width=425,
            height=75,
            font=("Helvetica", 20),
            fg_color="#10171B",
            anchor="w",
            corner_radius=12,
            border_width=1,
            border_color="#293036",
            hover=False,
            command=lambda:clipboard.copy(self.password)
        )
        self.generatedPassword.place(anchor="center", relx=0.31, rely=0.37)

        self.copyButton = ctk.CTkButton(master=self,
            text="Kopieren",
            image=ctk.CTkImage(dark_image=Image.open(resource_path("icons/copy.png")), size=(25, 25)),
            fg_color="#1E5AB3",
            border_width=1,
            border_color="#303840",
            width=115,
            height=50,
            font=("Segoe UI Semibold", 14),
            command=lambda: clipboard.copy(self.password)
        )
        self.copyButton.place(anchor="center", relx=0.70, rely=0.37)

        self.generateNew = ctk.CTkButton(master=self,
            text="Neu generieren",
            text_color="#E4E6E8",
            fg_color="#141B20",
            border_width=1,
            border_color="#303840",
            image=ctk.CTkImage(dark_image=Image.open(resource_path("icons/loop.png")), size=(20, 20)),
            width=145,
            height=45,
            font=("Segoe UI Semibold", 14),
            command=lambda: self.generatePassword()
        )
        self.generateNew.place(anchor="center", relx=0.89, rely=0.37)

        self.strengthText = ctk.CTkLabel(master=self,
            text=f"Stärke:",
            text_color="#E4E6E8",
            font=("Segoe UI Semibold", 16)
        )
        self.strengthText.place(anchor="center", relx=0.059, rely=0.66)

        self.strengthTextMode = ctk.CTkLabel(master=self,
            text=f"-",
            text_color="#E4E6E8",
            font=("Segoe UI Semibold", 16)
        )
        self.strengthTextMode.place(anchor="center", relx=0.11, rely=0.66)

        # #4A4D50 = transparent \ kW transparent not supported
        self.redBar = ctk.CTkProgressBar(master=self,
            width=112.5,
            height=10,
            corner_radius=12,
            progress_color="#4A4D50", #F32334
        )
        self.redBar.place(anchor="center", relx=0.095, rely=0.75)

        self.orangeBar = ctk.CTkProgressBar(master=self,
            width=112.5,
            height=10,
            corner_radius=12,
            progress_color="#4A4D50", #F7722E
        )
        self.orangeBar.place(anchor="center", relx=0.255, rely=0.75)

        self.goldBar = ctk.CTkProgressBar(master=self,
            width=112.5,
            height=10,
            corner_radius=12,
            progress_color="#4A4D50", #E69E0F
        )
        self.goldBar.place(anchor="center", relx=0.415, rely=0.75)

        self.glowGoldBar = ctk.CTkProgressBar(master=self,
            width=112.5,
            height=10,
            corner_radius=12,
            progress_color="#4A4D50", #FBBC04
        )
        self.glowGoldBar.place(anchor="center", relx=0.575, rely=0.75)

        self.greenBar = ctk.CTkProgressBar(master=self,
            width=112.5,
            height=10,
            corner_radius=12,
            progress_color="#4A4D50", #22D341
        )
        self.greenBar.place(anchor="center", relx=0.735, rely=0.75)

        self.glowGreenBar = ctk.CTkProgressBar(master=self,
            width=112.5,
            height=10,
            corner_radius=12,
            progress_color="#4A4D50", #21C53C
        )
        self.glowGreenBar.place(anchor="center", relx=0.895, rely=0.75)

        self.tippMsg = ctk.CTkButton(master=self,
            text="Tipp: Verwende Passwörter mit mindestens 16 Zeichen für maximale Sicherheit.",
            hover="disabled",
            text_color="#ACB5C0",
            fg_color="transparent",
            image=ctk.CTkImage(dark_image=Image.open(resource_path("icons/check.png")), size=(23, 23)),
            font=("Segoe UI Semibold", 13)
        )
        self.tippMsg.place(anchor="center", relx=0.36, rely=0.92)

    def progressBarReset(self):
        self.redBar.set(0)
        self.redBar.configure(progress_color="#4A4D50")
        self.orangeBar.set(0)
        self.orangeBar.configure(progress_color="#4A4D50")
        self.goldBar.set(0)
        self.goldBar.configure(progress_color="#4A4D50")
        self.glowGoldBar.set(0)
        self.glowGoldBar.configure(progress_color="#4A4D50")
        self.greenBar.set(0)
        self.greenBar.configure(progress_color="#4A4D50")
        self.glowGreenBar.set(0)
        self.glowGreenBar.configure(progress_color="#4A4D50")

    def generatePassword(self):
        upperLetters = setFrame.UpChars
        lowerLetters = setFrame.LowChars
        digits = setFrame.Numbers
        punctuation = setFrame.Puncs
        passwordLength = setFrame.passwordLength
        
        optionsEnabled = sum([upperLetters, lowerLetters, digits, punctuation])
        genChars = ''

        if upperLetters:
            genChars += string.ascii_uppercase
        
        if lowerLetters:
            genChars += string.ascii_lowercase
        
        if digits:
            genChars += string.digits
        
        if punctuation:
            genChars += string.punctuation

        if len(genChars) == 0:
            self.progressBarReset()
            self.strengthTextMode.configure(text="-", text_color="#E4E6E8")
            self.strengthTextMode.place(anchor="center", relx=0.11, rely=0.66)
            self.generatedPassword.configure(text="Bitte wähle mindestens eine Zeichenart aus.")
            return

        pw = ''
        for n in range(passwordLength):
            pw += secrets.choice(genChars)
        self.password = pw
        self.generatedPassword.configure(text=pw)

        '''
        Point System for the StrengthBar
        1 Point = text \ Sehr Schwach   #F32334
        2 Point = text \ Schwach        #F7722E
        3 Point = text \ Mittel         #E69E0F
        4 Point = text \ Stark          #FBBC04   
        5 Point = text \ Sehr Stark     #22D341
        6 Point = text \ Extrem stark   #21C53C
        
        Requirements \ Previous requirement needed for higher score:
        1 Point = Length of 4
        2 Points = Length of 8 & 2 options enabled
        3 Points = Length of 12
        4 Points = Length of 16
        5 Points = 3 options enabled
        6 Points = Length of 24 & 4 options enabled
        Special Requirements:
        2 Points = if length >= 20 & 1 options enabled
        '''

        self.progressBarReset()

        points = 0

        if passwordLength >= 4:
            points += 1

        if passwordLength >= 8 and optionsEnabled >= 2 and points == 1:
            points += 1

        if passwordLength >= 12 and points == 2:
            points += 1
        
        if passwordLength >= 16  and points == 3:
            points += 1
        
        if optionsEnabled >= 3  and points == 4:
            points += 1
        
        if passwordLength >= 24 and optionsEnabled == 4 and points == 5:
            points += 1

        if passwordLength >= 20 and optionsEnabled == 1:
            points +=2

        # StrengthBar
        if points >= 1:
            self.redBar.set(1)
            self.redBar.configure(progress_color="#F32334")

        if points >= 2:
            self.orangeBar.set(1)
            self.orangeBar.configure(progress_color="#F7722E")

        if points >= 3:
            self.goldBar.set(1)
            self.goldBar.configure(progress_color="#E69E0F")

        if points >= 4:
            self.glowGoldBar.set(1)
            self.glowGoldBar.configure(progress_color="#FBBC04")

        if points >= 5:
            self.greenBar.set(1)
            self.greenBar.configure(progress_color="#22D341")

        if points >= 6:
            self.glowGreenBar.set(1)
            self.glowGreenBar.configure(progress_color="#21C53C")
        
        # StrengthText
        if points == 1:
            self.strengthTextMode.configure(text="Sehr Schwach", text_color="#F32334")
            self.strengthTextMode.place(anchor="center", relx=0.172, rely=0.663)

        if points == 2:
            self.strengthTextMode.configure(text="Schwach", text_color="#F7722E")
            self.strengthTextMode.place(anchor="center", relx=0.145, rely=0.663)

        if points == 3:
            self.strengthTextMode.configure(text="Mittel", text_color="#E69E0F")
            self.strengthTextMode.place(anchor="center", relx=0.133, rely=0.663)

        if points == 4:
            self.strengthTextMode.configure(text="Stark", text_color="#FBBC04")
            self.strengthTextMode.place(anchor="center", relx=0.127, rely=0.663)

        if points == 5:
            self.strengthTextMode.configure(text="Sehr Stark", text_color="#22D341")
            self.strengthTextMode.place(anchor="center", relx=0.153, rely=0.663)

        if points == 6:
            self.strengthTextMode.configure(text="Extrem stark", text_color="#21C53C")
            self.strengthTextMode.place(anchor="center", relx=0.163, rely=0.663)