import customtkinter as ctk

from PIL import Image
from app.src.resourcePath import resourcePath

class MainFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent,
            fg_color="#131D27",
            width=850,
            height=725,
            corner_radius=0
        )

        self.icon = ctk.CTkButton(master=self,
            text="",
            image=ctk.CTkImage(dark_image=Image.open(resourcePath('app/icons/app.ico')), size=(60,60)),
            hover="disabled",
            fg_color="#1B242F",
            border_width=1,
            border_color="#222A34",
            width=75,
            height=75
        )
        self.icon.place(anchor="center", relx=0.08, rely=0.1)

        self.title = ctk.CTkLabel(master=self,
            text="System Monitor",
            text_color="#E4EFF1",
            font=("Poppins", 32)
        )
        self.title.place(anchor="center", relx=0.28, rely=0.08)

        self.text = ctk.CTkLabel(master=self,
            text="Überwache die Systemleistung in Echtzeit.",
            text_color="#8996A0",
            font=("Segoe UI", 15)
        )
        self.text.place(anchor="center", relx=0.315, rely=0.12)