import customtkinter as ctk
import psutil, platform, os, sys, socket

from PIL import Image
from app.src.resourcePath import resourcePath

class SystemInformation(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent,
            fg_color="transparent",
            width=850,
            height=350,
            corner_radius=0
        )

        self.title = ctk.CTkButton(master=self,
            text="System Informationen",
            image=ctk.CTkImage(dark_image=Image.open(resourcePath('app/icons/systemInfo.png')), size=(25, 25)),
            fg_color="transparent",
            hover="disabled",
            font=("Roboto Medium", 16)
        )
        self.title.place(anchor="center", relx=0.15, rely=0.08)

        # CPU Usage Design 1
        self.cpuUsage = ctk.CTkButton(master=self,
            text="CPU Auslastung",
            image=ctk.CTkImage(dark_image=Image.open(resourcePath('app/icons/cpuIcon.png')), size=(28, 28)),
            width=788,
            height=55,
            fg_color="#18212C",
            border_width=1,
            border_color="#2F3640",
            hover="disabled",
            corner_radius=0,
            anchor="w",
            font=("Roboto", 15)
        )
        self.cpuUsage.place(anchor="center", relx=0.5, rely=0.22)

        self.cpuText = ctk.CTkLabel(master=self.cpuUsage,
            text_color="#2C6EDA",
            font=("Roboto", 16),
        )
        self.cpuText.place(anchor="center", relx=0.68, rely=0.5)

        self.cpuBar = ctk.CTkProgressBar(master=self.cpuUsage,
            width=200,
            height=10,
            border_width=0,
            corner_radius=8,
            progress_color="#2C6EDA",
            fg_color="#29333F"
        )
        self.cpuBar.place(anchor="center", relx=0.85, rely=0.5)

        # RAM Usage Design 2
        self.ramUsage = ctk.CTkButton(master=self,
            text="RAM Auslastung",
            image=ctk.CTkImage(dark_image=Image.open(resourcePath('app/icons/ramIcon.png')), size=(28, 28)),
            width=788,
            height=55,
            fg_color="#18212C",
            border_width=1,
            border_color="#2F3640",
            hover="disabled",
            corner_radius=0,
            anchor="w",
            font=("Roboto", 15)
        )
        self.ramUsage.place(anchor="center", relx=0.5, rely=0.362)

        self.ramText = ctk.CTkLabel(master=self.ramUsage,
            text_color="#2C6EDA",
            font=("Roboto", 16),
        )
        self.ramText.place(anchor="center", relx=0.68, rely=0.5)

        self.ramBar = ctk.CTkProgressBar(master=self.ramUsage,
            width=200,
            height=10,
            border_width=0,
            corner_radius=8,
            progress_color="#2C6EDA",
            fg_color="#29333F"
        )
        self.ramBar.place(anchor="center", relx=0.85, rely=0.5)

        # operationSystem Design 3
        self.operationSystem = ctk.CTkButton(master=self,
            text="Betriebssystem",
            image=ctk.CTkImage(dark_image=Image.open(resourcePath('app/icons/windowsIcon.png')), size=(28, 28)),
            width=788,
            height=55,
            fg_color="#18212C",
            border_width=1,
            border_color="#2F3640",
            hover="disabled",
            corner_radius=0,
            anchor="w",
            font=("Roboto", 15)
        )
        self.operationSystem.place(anchor="center", relx=0.5, rely=0.515)

        self.oStext = ctk.CTkLabel(master=self.operationSystem,
            text="",
            text_color="#82919A",
            font=("Roboto", 15)
        )
        self.oStext.place(anchor="center", relx=0.88, rely=0.5)

        # hostName Design 4
        self.hostName = ctk.CTkButton(master=self,
            text="Hostname",
            image=ctk.CTkImage(dark_image=Image.open(resourcePath('app/icons/hostName.png')), size=(28, 28)),
            width=788,
            height=55,
            fg_color="#18212C",
            border_width=1,
            border_color="#2F3640",
            hover="disabled",
            corner_radius=0,
            anchor="w",
            font=("Roboto", 15)
        )
        self.hostName.place(anchor="center", relx=0.5, rely=0.66)

        self.hostText = ctk.CTkLabel(master=self.hostName,
            text=socket.gethostname(),
            text_color="#82919A",
            font=("Roboto", 15)
        )
        self.hostText.place(anchor="center", relx=0.94, rely=0.5)

        # networkConnection Design 5
        self.networkConnection = ctk.CTkButton(master=self,
            text="Internet Status",
            image=ctk.CTkImage(dark_image=Image.open(resourcePath('app/icons/networkIcon.png')), size=(28, 28)),
            width=788,
            height=55,
            fg_color="#18212C",
            border_width=1,
            border_color="#2F3640",
            hover="disabled",
            corner_radius=0,
            anchor="w",
            font=("Roboto", 15)
        )
        self.networkConnection.place(anchor="center", relx=0.5, rely=0.805)

        self.networkText = ctk.CTkLabel(master=self.networkConnection,
            text_color="#82919A",
            font=("Roboto", 15)
        )
        self.networkText.place(anchor="center", relx=0.94, rely=0.5)


        def updateGUI():
            CPUUSAGE = psutil.cpu_percent(interval=None)
            self.cpuBar.set(CPUUSAGE / 100)
            self.cpuText.configure(text=str(CPUUSAGE)+'%')
            RAMUSAGE = list(psutil.virtual_memory())[2]
            self.ramBar.set(RAMUSAGE / 100)
            self.ramText.configure(text=str(RAMUSAGE)+'%')
            OPERATIONSYSTEM = self.getWindowsVersion()
            self.oStext.configure(text=OPERATIONSYSTEM)
            CONNECTION = self.getNetwork()
            self.networkText.configure(text=CONNECTION)

            self.after(500, updateGUI)
        
        updateGUI()
    
    def getWindowsVersion(self):
        version = ''
        # check if Windows device
        if platform.system() != "Windows":
            self.oStext.place(anchor="center", relx=0.66, rely=0.5)
            return "Keine Windows-Version erkannt - Informationen können nicht geladen werden."
        else:
            version += "Windows "

        # check Windows Version
        if platform.release() == "10":
            version += "11 " if int(sys.getwindowsversion().build) >= 22000 else "10 "
        else:
            version += f"{platform.release()} "

        # read which edition (home, pro...)
        if platform.win32_edition() == "Professional":
            version += "Pro "
        elif platform.win32_edition() == "Core":
            version += "Home "
        
        # get bit architecture
        if os.environ.get("PROCESSOR_ARCHITECTURE") == "AMD64":
            version += "64-bit"
        else:
            version += "32-bit"
        return version
    
    def getNetwork(self, host="8.8.8.8", port=53, timeout=3):
        """
        Checks if there is an active internet connection by 
        pinging a public server
        """
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            self.networkText.configure(text_color="#4ACF67")
            return "Online"
        except socket.error:
            self.networkText.configure(text_color="#B80808")
            return "Offline"