import customtkinter as ctk
import getpass, time, psutil

from PIL import Image
from datetime import timedelta, datetime
from app.src.resourcePath import resourcePath

class MoreInformation(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent,
            fg_color="transparent",
            width=850,
            height=175,
            corner_radius=0
        )

        self.title = ctk.CTkButton(master=self,
            text="Weitere Informationen",
            image=ctk.CTkImage(dark_image=Image.open(resourcePath('app/icons/moreInfo.png')), size=(22, 22)),
            fg_color="transparent",
            hover="disabled",
            font=("Roboto Medium", 16)
        )
        self.title.place(anchor="center", relx=0.15, rely=0.08)

        # Username Design 1
        self.username = ctk.CTkButton(master=self,
            text="Benutzername",
            width=788,
            image=ctk.CTkImage(dark_image=Image.open(resourcePath('app/icons/userIcon.png')), size=(25, 25)),
            height=45,
            fg_color="#18212C",
            border_width=1,
            border_color="#2F3640",
            hover="disabled",
            corner_radius=0,
            anchor="w",
            font=("Arial", 15)
        )
        self.username.place(anchor="center", relx=0.5, rely=0.3)

        self.usernameText = ctk.CTkLabel(master=self.username,
            text=getpass.getuser(),
            text_color="#82919A",
            font=("Roboto", 15)
        )
        self.usernameText.place(anchor="center", relx=0.92, rely=0.5)

        # systemRuntime Design 2
        self.systemRuntime = ctk.CTkButton(master=self,
            text="Systemlaufzeit",
            width=788,
            image=ctk.CTkImage(dark_image=Image.open(resourcePath('app/icons/clockIcon.png')), size=(25, 25)),
            height=45,
            fg_color="#18212C",
            border_width=1,
            border_color="#2F3640",
            hover="disabled",
            corner_radius=0,
            anchor="w",
            font=("Arial", 15)
        )
        self.systemRuntime.place(anchor="center", relx=0.5, rely=0.532)

        self.systemText = ctk.CTkLabel(master=self.systemRuntime,
            text_color="#82919A",
            font=("Roboto", 15)
        )
        self.systemText.place(anchor="center", relx=0.92, rely=0.5)

        # date & time Design 3
        self.dateTime = ctk.CTkButton(master=self,
            text="Aktuelle Zeit",
            width=788,
            image=ctk.CTkImage(dark_image=Image.open(resourcePath('app/icons/calendarIcon.png')), size=(25, 25)),
            height=45,
            fg_color="#18212C",
            border_width=1,
            border_color="#2F3640",
            hover="disabled",
            corner_radius=0,
            anchor="w",
            font=("Arial", 15)
        )
        self.dateTime.place(anchor="center", relx=0.5, rely=0.765)
        
        self.dateText = ctk.CTkLabel(master=self.dateTime,
            text_color="#82919A",
            font=("Roboto", 15)
        )
        self.dateText.place(anchor="center", relx=0.9, rely=0.5)

        def updateGUI():
            BOOTTIME = self.getBootTime()
            CURRENTTIME = self.getTime()
            self.systemText.configure(text=BOOTTIME)
            self.dateText.configure(text=CURRENTTIME)
            self.after(1000, updateGUI)
        
        updateGUI()

    def getBootTime(self):
        uptime = int(time.time() - psutil.boot_time())
        result = str(timedelta(seconds=uptime))
        return result
    
    def getTime(self):
        time = datetime.now()
        return time.strftime("%d.%m.%Y %H:%M:%S")