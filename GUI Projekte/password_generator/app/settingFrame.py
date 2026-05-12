import customtkinter as ctk

from PIL import Image
from app.advancedFrame import advancedFrame
from app.loadResourcePath import resource_path

passwordLength = 12 # startIndex
UpChars, LowChars, Numbers, Puncs = True, True, True, True  # automatically enabled

class settingFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent,
             width=725,
             height=235,
             fg_color="#192126",
             corner_radius=12,
             border_color="#1E262C",
             border_width=2
        )

        self.titleText = ctk.CTkButton(master=self,
            text="Einstellungen",
            text_color="#EBECEC",
            image=ctk.CTkImage(dark_image=Image.open(resource_path("icons/settings.png")), size=(25, 25)),
            font=("Segoe UI Semibold", 17),
            hover="disabled",
            fg_color="transparent",
            width=0,
            height=0
        )
        self.titleText.place(anchor="center", relx=0.1, rely=0.1)

        self.passwortLenText = ctk.CTkLabel(master=self,
            text="Passwortlänge:",
            text_color="#ACB5C0",
            font=("Segoe UI Semibold", 15),
        )
        self.passwortLenText.place(anchor="center", relx=0.09, rely=0.3)
        self.numberLenText = ctk.CTkLabel(master=self,
            text="12",
            text_color="#ACB5C0",
            font=("Segoe UI Semibold", 15),
        )
        self.numberLenText.place(anchor="center", relx=0.177, rely=0.3)      

        self.slideBar = ctk.CTkSlider(master=self,
            from_=4,
            to=32,
            width=200,
            height=15,
            progress_color="#3466AA",
            fg_color="#2B353F",
            button_color="#F0F4FA",
            button_hover_color="#F0F4FA",
            hover=False,
            corner_radius=12,
            border_width=1,
            command=self.sliderNumber
        )
        self.slideBar.place(anchor="center", relx=0.157, rely=0.43)
        

        self.minText = ctk.CTkLabel(master=self,
            text=4,
            text_color="#ACB5C0",
            font=("Helvetica", 13.5)
        )
        self.minText.place(anchor="center", relx=0.027, rely=0.52)

        self.maxText = ctk.CTkLabel(master=self,
            text=32,
            text_color="#ACB5C0",
            font=("Helvetica", 13.5)
        )
        self.maxText.place(anchor="center", relx=0.285, rely=0.52)

        self.vcmd = (self.register(self.checkEntry), "%P")
        self.entrySlider = ctk.CTkEntry(master=self,
            placeholder_text=0,
            fg_color="#192025",
            validate="key",
            validatecommand=self.vcmd,
            border_color="#242B30",
            border_width=1,
            width=70,
            height=40,
            justify="center",
            font=("Helvetica", 13.5)
        )
        self.entrySlider.place(anchor="center", relx=0.36, rely=0.43)
    
        self.optionText = ctk.CTkLabel(master=self,
            text="Zeichenarten",
            text_color="#EEEFF0",
            font=("Segoe UI Semibold", 17, "bold"),
        )
        self.optionText.place(anchor="center", relx=0.525, rely=0.32)

        self.lettersUp = ctk.CTkCheckBox(master=self,
            text="Großbuchstaben (A-Z)",
            font=("Helvetica", 14.5),
            border_width=1,
            border_color="#293037",
            fg_color="#2868C8",
            checkbox_width=20,
            checkbox_height=20,
            hover_color="#2868C8",
            command=lambda: self.checkBoxes()
        )
        self.lettersUp.place(anchor="center", relx=0.57, rely=0.45)

        self.lettersLow = ctk.CTkCheckBox(master=self,
            text="Kleinbuchstaben (a-z)",
            font=("Helvetica", 14.5),
            border_width=1,
            border_color="#293037",
            fg_color="#2868C8",
            checkbox_width=20,
            checkbox_height=20,
            hover_color="#2868C8",
            command=lambda: self.checkBoxes()
        )
        self.lettersLow.place(anchor="center", relx=0.5668, rely=0.559)

        self.numbers = ctk.CTkCheckBox(master=self,
            text="Zahlen (0-9)",
            font=("Helvetica", 14.5),
            border_width=1,
            border_color="#293037",
            fg_color="#2868C8",
            checkbox_width=20,
            checkbox_height=20,
            hover_color="#2868C8",
            command=lambda: self.checkBoxes()
        )
        self.numbers.place(anchor="center", relx=0.793, rely=0.45)

        self.puncs = ctk.CTkCheckBox(master=self,
            text="Sonderzeichen (!@#$%)",
            font=("Helvetica", 14.5),
            border_width=1,
            border_color="#293037",
            fg_color="#2868C8",
            checkbox_width=20,
            checkbox_height=20,
            hover_color="#2868C8",
            command=lambda: self.checkBoxes()
        )
        self.puncs.place(anchor="center", relx=0.845, rely=0.559)

        self.advancedOptions = ctk.CTkButton(master=self,
            text="Erweiterte Optionen",
            fg_color="#151B21",
            border_width=1,
            border_color="#242B32",
            corner_radius=12,
            hover_color="#161C22",
            font=("Segoe UI Semibold", 16.5),
            width=700,
            height=50,
            command=self.openOptions
        )
        self.advancedOptions.place(anchor="center", relx=0.5, rely=0.83)
        self.advancedOptionsFrame = None # placeholder

        # Options automatically enabled
        self.lettersUp.select() #deselect
        self.lettersLow.select()#deselect
        self.numbers.select()   #deselect
        self.puncs.select()     #deselect

        
    def sliderNumber(self, value):
        global passwordLength
        self.numberLenText.configure(text=f"{int(value)}")
        passwordLength = int(value)

    def checkEntry(self, n):
        global passwordLength

        # deleting
        if n == "":
            return True
        
        # onlyNumbers allowed
        if not n.isdigit():
            return False
        
        # only 2 digits allowed
        if len(n) > 2:
            return False

        # max value 32
        if int(n) > 32:
            return False

        if int(n) <= 0:
            self.slideBar.set(12)
            self.numberLenText.configure(text="12")
        elif int(n) < 4:
            passwordLength = int(4)
            self.slideBar.set(4)
            self.numberLenText.configure(text="4") 
        else:
            passwordLength = int(n)
            self.slideBar.set(int(n))
            self.numberLenText.configure(text=f"{int(n)}")

        return True

    def checkBoxes(self):
        global UpChars, LowChars, Numbers, Puncs
        UpChars = (self.lettersUp.get() == 1)
        LowChars = (self.lettersLow.get() == 1)
        Numbers = (self.numbers.get() == 1)
        Puncs = (self.puncs.get() == 1)
    

    def openOptions(self):
        if self.advancedOptionsFrame is None or not self.advancedOptionsFrame.winfo_exists():
            self.advancedOptionsFrame = advancedFrame() # create window
        else:
            self.advancedOptionsFrame.focus() # if window already exists focus it