import tkinter as tk
from typing import Callable

BUTTON_WIDTH = 90
BUTTON_HEIGHT = 50

class CalcButton(tk.Frame):
    def __init__(self, parent, text:str, delegada: Callable):
        super().__init__(parent, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        self.pack_propagate(False)
        btn = tk.Button(self, text=text, command=self.handle_click)
        btn.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.text = text
        self.delegada = delegada

    def handle_click(self):
        self.delegada(self.text)


class KeyBoard(tk.Frame):
    def __init__(self, parent, command: Callable):
        super().__init__(parent, width=BUTTON_WIDTH * 3, height=BUTTON_HEIGHT * 5)
        self.grid_propagate(False)
        
        self.buttons = []
        text_buttons = ("clear","%", "/",
                        "I", "V", "*",
                        "X", "L", "-",
                        "C", "D", "+",
                        "M", ".", "=")
        
        ix = 0
        for row in range(5):
            for col in range(3):
                btn = CalcButton(self, text_buttons[ix], command)
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
        
        self.display = Display(self)
        self.display.pack(side=tk.TOP, expand=False, fill=tk.BOTH)
        
        self.keyboard = KeyBoard(self, command)
        self.keyboard.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        
    def show(self, text: str):
        self.display.show(text)

        
