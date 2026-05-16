import customtkinter as ctk

from app.src.mainFrame import MainFrame
from app.src.systemInformation import SystemInformation
from app.src.moreInformations import MoreInformation
from app.src.resourcePath import resourcePath

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("System Monitor")
        self.setGeometry(850, 725)
        self.iconbitmap(resourcePath('app/icons/app.ico'))
        self.resizable(False, False)

        #place frames
        self.mainFrame = MainFrame(self)
        self.mainFrame.place(anchor="center", relx=0.5, rely=0.5)

        self.systemFrame = SystemInformation(self.mainFrame)
        self.systemFrame.place(anchor="center", relx=0.5, rely=0.42)

        self.moreFrame = MoreInformation(self.mainFrame)
        self.moreFrame.place(anchor="center", relx=0.5, rely=0.78)

    def setGeometry(self, width: int, height: int):
        # place the app in the center of the screen
        x = int((self.winfo_screenwidth() / 2) - (width / 2))
        y = int((self.winfo_screenheight() / 2) - (height / 2))
        self.geometry(f"{width}x{height}+{x}+{y}")