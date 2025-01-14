import tkinter as tk
from calc.views import Calculator
from calc.models.calculos import RomanCalculo, Status
from calc.models.roman_number import Roman_Number
from calc.models.keys import Key, TiposTecla

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Romana")
        self.calc = Calculator(self, self.handle_button_click)
        self.calc.pack()
        self.calculo = RomanCalculo()

    def handle_button_click(self, key: Key):
        self.calculo.add_key(key)
        self.calc.show(self.calculo.get_display())
        history = self.calculo.get_resume()
        if history:
            self.calc.history.addline(history)
           

    def run (self):
        self.mainloop()