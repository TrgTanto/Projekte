import customtkinter as ctk
from app.mainFrame import mainFrame
from app.generatorFrame import generatorFrame
from app.settingFrame import settingFrame
from app.loadResourcePath import resource_path

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.setWindow(775, 650)
        self.resizable(False, False)
        self.title("Passwort Generator")

        # Background
        self.bg = ctk.CTkFrame(master=self,
             width=775,
             height=650,
             fg_color="#0E151A"
        )
        self.bg.place(anchor="center", relx=0.5, rely=0.5)

        # Load Frames
        self.firstFrame = mainFrame(self.bg)
        self.firstFrame.place(anchor="center", relx=0.5, rely=0.5)

        self.generator = generatorFrame(self.firstFrame)
        self.generator.place(anchor="center", relx=0.5, rely=0.38)

        self.settings = settingFrame(self.firstFrame)
        self.settings.place(anchor="center", relx=0.5, rely=0.78)

    # sets the app in the center of the screen
    def setWindow(self, width: int, height: int):
        screenWidth, screenHeight = self.winfo_screenwidth(), self.winfo_screenheight()
        x = int(((screenWidth / 2) - (width / 2)))
        y = int((screenHeight / 2) - (height / 2))
        self.geometry(f"{width}x{height}+{x}+{y}")