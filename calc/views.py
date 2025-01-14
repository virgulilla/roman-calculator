import tkinter as tk
from typing import Callable
from enum import Enum
from calc.models.keys import TiposTecla, Key

BUTTON_WIDTH = 90
BUTTON_HEIGHT = 50

class CalcButton(tk.Frame):
    def __init__(self, parent, key:Key, delegada: Callable):
        super().__init__(parent, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        self.pack_propagate(False)
        btn = tk.Button(self, text=key.valor, command=self.handle_click)
        btn.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.key = key
        self.delegada = delegada

    def handle_click(self):
        self.delegada(self.key)


class KeyBoard(tk.Frame):
    key_buttons = (Key("clear", TiposTecla.RESET), Key("%", TiposTecla.OPERATIONS), 
                   Key("/", TiposTecla.OPERATIONS),
                   Key("I", TiposTecla.DIGITS), Key("V", TiposTecla.DIGITS), Key("*", 
                    TiposTecla.OPERATIONS), Key("X", TiposTecla.DIGITS), Key("L", TiposTecla.DIGITS),
                    Key("-", TiposTecla.OPERATIONS), Key("C", TiposTecla.DIGITS), Key("D", TiposTecla.DIGITS),
                    Key("+", TiposTecla.OPERATIONS), Key("M", TiposTecla.DIGITS), 
                    Key("•", TiposTecla.DIGITS), Key("=", TiposTecla.EQUAL))      
   
    def __init__(self, parent, command: Callable):
        super().__init__(parent, width=BUTTON_WIDTH * 3, height=BUTTON_HEIGHT * 5)
        self.grid_propagate(False)
        
        self.buttons = []        
        
        ix = 0
        for row in range(5):
            for col in range(3):                
                btn = CalcButton(self, self.key_buttons[ix], command)
                btn.grid(column=col, row=row)
                ix += 1    
                    

class Display(tk.Frame):
    def __init__(self, parent, text: str=""):
        super().__init__(parent, width=BUTTON_WIDTH * 3, height=BUTTON_HEIGHT)
        self.pack_propagate(False)
        self.display = tk.Label(self, text=text, fg="white", bg="black", anchor="e", font=("Arial", 18))
        self.display.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        
    def show(self, text: str):
        self.display.config(text=text)    

class Calculator(tk.Frame):
    def __init__(self, parent, command: Callable):        
        super().__init__(parent)        
        frmLeft = tk.Frame(self)
        frmLeft.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        frmRight = tk.Frame(self)
        frmRight.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)        
        self.display = Display(frmLeft)
        self.display.pack()        
        self.keyboard = KeyBoard(frmLeft, command)
        self.keyboard.pack()
        self.history = ResumePanel(frmRight)
        self.history.pack()
        
    def show(self, text: str):
        self.display.show(text)

        
class ResumePanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=BUTTON_WIDTH*3, height=BUTTON_HEIGHT*6)
        self.pack_propagate(False)
        frm = tk.Frame(self, bd=2, relief="groove")
        frm.pack(side=tk.TOP, expand=True, fill=tk.X)
        tk.Label(frm, text="RESUMEN", anchor=tk.W).pack(side=tk.LEFT, expand=True, fill=tk.X)
        tk.Button(frm, text="Borrar", command=self.__reset).pack(side=tk.LEFT)

        self.__panel = tk.Text(self, state="disabled")
        self.__panel.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

    def __reset(self):
        self.__panel.config(state="normal")
        self.__panel.delete("1.0", "end")
        self.__panel.config(state="disabled")

    def addline(self, value: str):
        self.__panel.config(state="normal")
        self.__panel.insert("end", f"{value}\n")
        self.__panel.config(state="disabled")