import customtkinter as ctk

#from src.resourcePath import resourcePath

calculatorText = ''
calculation = ()

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.setGeometry(450, 400)
        self.resizable(False, False)
        #self.iconbitmap(resourcePath('icons\calculator.ico'))
        self.title('Taschenrechner')

        # background color
        self.bg = ctk.CTkFrame(master=self,
            fg_color="#181A1F",
            width=450,
            height=400,
            corner_radius=0,
            border_width=0
        )
        self.bg.place(anchor="center", relx=0.5, rely=0.5)

        # calculator Text
        self.calcText = ctk.CTkButton(master=self.bg,
            fg_color="#1E1F24",
            width=415,
            height=85,
            border_width=1,
            border_color="#0A0B0F",
            hover="disabled",
            text=0,
            text_color="#F29925",
            font=("Roboto", 40),
            anchor="e"
        )
        self.calcText.place(anchor="center", relx=0.5, rely=0.13)

        # first Layer
        self.buttonZero = ctk.CTkButton(master=self.bg,
            text="0",
            width=205,
            height=50,
            text_color="#FFFFFF",
            fg_color="#22242A",
            border_width=1,
            border_color="#282A32",
            font=("Roboto Medium", 16),
            hover_color="#282A32",
            command=lambda: self.calculator("0")
        )
        self.buttonZero.place(anchor="center", relx=0.268, rely=0.88)

        self.buttonComma = ctk.CTkButton(master=self.bg,
            text=",",
            width=100,
            height=50,
            text_color="#FFFFFF",
            fg_color="#22242A",
            border_width=1,
            border_color="#282A32",
            font=("Roboto Medium", 16),
            hover_color="#282A32",
            command=lambda: self.calculator(".")
        )
        self.buttonComma.place(anchor="center", relx=0.62, rely=0.88)

        self.buttonEqual = ctk.CTkButton(master=self.bg,
            text="=",
            width=100,
            height=50,
            text_color="#FFFFFF",
            fg_color="#B66117",
            border_width=1,
            border_color="#A55E1C",
            font=("Roboto Medium", 16),
            hover_color="#A55E1C",
            command=lambda: self.calculator("=")
        )
        self.buttonEqual.place(anchor="center", relx=0.855, rely=0.88)

        # second Layer
        self.buttonOne = ctk.CTkButton(master=self.bg,
            text="1",
            width=100,
            height=50,
            text_color="#FFFFFF",
            fg_color="#22242A",
            border_width=1,
            border_color="#282A32",
            font=("Roboto Medium", 16),
            hover_color="#282A32",
            command=lambda: self.calculator("1")
        )
        self.buttonOne.place(anchor="center", relx=0.15, rely=0.74)

        self.buttonTwo = ctk.CTkButton(master=self.bg,
            text="2",
            width=100,
            height=50,
            text_color="#FFFFFF",
            fg_color="#22242A",
            border_width=1,
            border_color="#282A32",
            font=("Roboto Medium", 16),
            hover_color="#282A32",
            command=lambda: self.calculator("2")
        )
        self.buttonTwo.place(anchor="center", relx=0.385, rely=0.74)

        self.buttonThree = ctk.CTkButton(master=self.bg,
            text="3",
            width=100,
            height=50,
            text_color="#FFFFFF",
            fg_color="#22242A",
            border_width=1,
            border_color="#282A32",
            font=("Roboto Medium", 16),
            hover_color="#282A32",
            command=lambda: self.calculator("3")
        )
        self.buttonThree.place(anchor="center", relx=0.62, rely=0.74)

        self.buttonPlus = ctk.CTkButton(master=self.bg,
            text="+",
            width=100,
            height=50,
            text_color="#EB8719",
            fg_color="#523018",
            border_width=1,
            border_color="#4B3420",
            font=("Roboto", 20),
            hover_color="#4B3420",
            command=lambda: self.calculator("+")
        )
        self.buttonPlus.place(anchor="center", relx=0.855, rely=0.74)

        # third Layer
        self.buttonFour = ctk.CTkButton(master=self.bg,
            text="4",
            width=100,
            height=50,
            text_color="#FFFFFF",
            fg_color="#22242A",
            border_width=1,
            border_color="#282A32",
            font=("Roboto Medium", 16),
            hover_color="#282A32",
            command=lambda: self.calculator("4")
        )
        self.buttonFour.place(anchor="center", relx=0.15, rely=0.6)

        self.buttonFive = ctk.CTkButton(master=self.bg,
            text="5",
            width=100,
            height=50,
            text_color="#FFFFFF",
            fg_color="#22242A",
            border_width=1,
            border_color="#282A32",
            font=("Roboto Medium", 16),
            hover_color="#282A32",
            command=lambda: self.calculator("5")
        )
        self.buttonFive.place(anchor="center", relx=0.385, rely=0.6)

        self.buttonSix = ctk.CTkButton(master=self.bg,
            text="6",
            width=100,
            height=50,
            text_color="#FFFFFF",
            fg_color="#22242A",
            border_width=1,
            border_color="#282A32",
            font=("Roboto Medium", 16),
            hover_color="#282A32",
            command=lambda: self.calculator("6")
        )
        self.buttonSix.place(anchor="center", relx=0.62, rely=0.6)

        self.buttonMinus = ctk.CTkButton(master=self.bg,
            text="−",
            width=100,
            height=50,
            text_color="#EB8719",
            fg_color="#523018",
            border_width=1,
            border_color="#4B3420",
            font=("Roboto", 20),
            hover_color="#4B3420",
            command=lambda: self.calculator("−")
        )
        self.buttonMinus.place(anchor="center", relx=0.855, rely=0.6)

        # fourth Layer
        self.buttonSeven = ctk.CTkButton(master=self.bg,
            text="7",
            width=100,
            height=50,
            text_color="#FFFFFF",
            fg_color="#22242A",
            border_width=1,
            border_color="#282A32",
            font=("Roboto Medium", 16),
            hover_color="#282A32",
            command=lambda: self.calculator("7")
        )
        self.buttonSeven.place(anchor="center", relx=0.15, rely=0.46)

        self.buttonEight = ctk.CTkButton(master=self.bg,
            text="8",
            width=100,
            height=50,
            text_color="#FFFFFF",
            fg_color="#22242A",
            border_width=1,
            border_color="#282A32",
            font=("Roboto Medium", 16),
            hover_color="#282A32",
            command=lambda: self.calculator("8")
        )
        self.buttonEight.place(anchor="center", relx=0.385, rely=0.46)

        self.buttonNine = ctk.CTkButton(master=self.bg,
            text="9",
            width=100,
            height=50,
            text_color="#FFFFFF",
            fg_color="#22242A",
            border_width=1,
            border_color="#282A32",
            font=("Roboto Medium", 16),
            hover_color="#282A32",
            command=lambda: self.calculator("9")
        )
        self.buttonNine.place(anchor="center", relx=0.62, rely=0.46)

        self.buttonMultiply = ctk.CTkButton(master=self.bg,
            text="×",
            width=100,
            height=50,
            text_color="#EB8719",
            fg_color="#523018",
            border_width=1,
            border_color="#4B3420",
            font=("Roboto", 20),
            hover_color="#4B3420",
            command=lambda: self.calculator("×")
        )
        self.buttonMultiply.place(anchor="center", relx=0.855, rely=0.46)

        # fifth Layer
        self.buttonAC = ctk.CTkButton(master=self.bg,
            text="AC",
            width=100,
            height=50,
            text_color="#9E9CE6",
            fg_color="#22242A",
            border_width=1,
            border_color="#282A32",
            font=("Roboto Medium", 18),
            hover_color="#282A32",
            command=lambda: self.calculator("AC")
        )
        self.buttonAC.place(anchor="center", relx=0.15, rely=0.32)

        self.buttonDelete = ctk.CTkButton(master=self.bg,
            text="⌫",
            width=100,
            height=50,
            text_color="#A4A5AB",
            fg_color="#22242A",
            border_width=1,
            border_color="#282A32",
            font=("Roboto Medium", 18),
            hover_color="#282A32",
            command=lambda: self.calculator("⌫")
        )
        self.buttonDelete.place(anchor="center", relx=0.385, rely=0.32)

        self.buttonPercent = ctk.CTkButton(master=self.bg,
            text="%",
            width=100,
            height=50,
            text_color="#A4A5AB",
            fg_color="#22242A",
            border_width=1,
            border_color="#282A32",
            font=("Roboto Medium", 18),
            hover_color="#282A32",
            command=lambda: self.calculator("%")
        )
        self.buttonPercent.place(anchor="center", relx=0.62, rely=0.32)

        self.buttonDivide = ctk.CTkButton(master=self.bg,
            text="÷",
            width=100,
            height=50,
            text_color="#EB8719",
            fg_color="#523018",
            border_width=1,
            border_color="#4B3420",
            font=("Roboto", 20),
            hover_color="#4B3420",
            command=lambda: self.calculator("÷")
        )
        self.buttonDivide.place(anchor="center", relx=0.855, rely=0.32)

    def setGeometry(self, width: int, height: int):
        x = int((self.winfo_screenwidth() / 2) - (width / 2))
        y = int((self.winfo_screenheight() / 2) - (height / 2))
        self.geometry(f"{width}x{height}+{x}+{y}")
    
    def checkLength(self):
        if len(calculatorText) < 10:
            self.calcText.configure(font=("Roboto", 40))
        elif len(calculatorText) < 15:
            self.calcText.configure(font=("Roboto", 35))
        elif len(calculatorText) < 20:
            self.calcText.configure(font=("Roboto", 30))
        elif len(calculatorText) < 30:
            self.calcText.configure(font=("Roboto", 20))
        elif len(calculatorText) < 40:
            self.calcText.configure(font=("Roboto", 15))
        elif len(calculatorText) < 65:
            self.calcText.configure(font=("Roboto", 10))
        elif len(calculatorText) < 100:
            self.calcText.configure(font=("Roboto", 5))
        elif len(calculatorText) < 120:
            self.calcText.configure(font=("Roboto", 1))

    def calculator(self, button: str):
        try:
            global calculatorText, calculation
            operators = ["+", "-", "*", "/"]

            if button == 'AC':
                self.calcText.configure(text=0, font=("Roboto", 40))
                calculatorText = ''
                calculation = tuple()
                return 
            
            if button == '⌫':
                removeLastIndex = calculatorText[:-1]
                calculatorText = removeLastIndex
                calculation = tuple(removeLastIndex)

                if len(calculatorText) == 0:
                    self.calcText.configure(text=0)

                else:
                    self.calcText.configure(text=calculatorText)
                return
            
            if button == '0':
                calculation += tuple("0")

            elif button == '1':
                calculation += tuple("1")

            elif button == '2':
                calculation += tuple("2")

            elif button == '3':
                calculation += tuple("3")

            elif button == '4':
                calculation += tuple("4")

            elif button == '5':
                calculation += tuple("5")

            elif button == '6':
                calculation += tuple("6")

            elif button == '7':
                calculation += tuple("7")

            elif button == '8':
                calculation += tuple("8")

            elif button == '9':
                calculation += tuple("9")

            elif button == '+':
                if calculation[-1] in operators: return
                calculation += tuple("+")

            elif button == '−':
                if calculation[-1] in operators: return
                calculation += tuple("-")

            elif button == '×':
                if calculation[-1] in operators: return
                calculation += tuple("*")

            elif button == '÷':
                if calculation[-1] in operators: return
                calculation += tuple("/")

            elif button == '.':
                if calculation[-1] == ".": return
                calculation += tuple(".")

            elif button == '%':
                if calculation[-1] == 0: return
                x = list(calculation)
                number = "".join(x)
                result = str(eval(number) / 100)
                calculation = tuple(result)
                calculatorText = result
                self.calcText.configure(text=calculatorText)
                self.checkLength()
                return

            elif button == '=':
                x = list(calculation)
                result = "".join(x)
                result = eval(result)
                result = round(result, 2)
                calculatorText = str(result)
                calculation = tuple(calculatorText)
                self.calcText.configure(text=calculatorText)
                self.checkLength()
                return
            
        except ZeroDivisionError:
            print("Du kannst nicht durch 0 teilen")
            self.calcText.configure(text="Du kannst nicht durch 0 dividieren", font=("Roboto", 25))
            calculatorText = ''
            calculation = ()
            return
        except IndexError: pass

        self.checkLength()
        calculatorText += button
        self.calcText.configure(text=calculatorText)