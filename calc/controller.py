import tkinter as tk
from models import RomanNumberError
from models.roman_number import Roman_Number
from views import Display, KeyBoard

class RomanCalculatorController:
    def __init__(self, root):
        self.root = root
        self.display = Display(root)
        self.display.grid(row=0, column=0)
        self.keyboard = KeyBoard(root, self.on_button_click)
        self.keyboard.grid(row=1, column=0)

        self.current_input = ""  # Almacena la entrada actual
        self.first_operand = None  # Almacena el primer operando
        self.operator = None  # Almacena el operador seleccionado

    def on_button_click(self, text):
        if text.isdigit() or text in ("I", "V", "X", "L", "C", "D", "M"):
            # Concatenar la entrada
            self.current_input += text
            self.display.set_text(self.current_input)
        elif text in ("+", "-", "*", "/", "%"):
            # Manejar operadores
            self._handle_operator(text)
        elif text == "=":
            # Realizar el cálculo
            self._calculate_result()
        elif text == "clear":
            # Limpiar la pantalla
            self._clear_display()
        else:
            # Mostrar error para botones desconocidos
            self.display.set_text("Error")

    def _handle_operator(self, operator):
        if self.current_input:
            try:
                self.first_operand = Roman_Number(self.current_input)
                self.operator = operator
                self.current_input = ""
                self.display.set_text("")
            except RomanNumberError:
                self.display.set_text("Error")
        else:
            self.display.set_text("Error")

    def _calculate_result(self):
        if self.first_operand and self.current_input:
            try:
                second_operand = Roman_Number(self.current_input)
                if self.operator == "+":
                    result = self.first_operand + second_operand
                elif self.operator == "-":
                    result = self.first_operand - second_operand
                elif self.operator == "*":
                    result = self.first_operand * second_operand
                elif self.operator == "/":
                    result = self.first_operand / second_operand
                elif self.operator == "%":
                    result = self.first_operand % second_operand
                else:
                    raise ValueError("Operador desconocido")
                
                self.display.set_text(str(result))
                self.first_operand = None
                self.current_input = ""
                self.operator = None
            except RomanNumberError:
                self.display.set_text("Error")
            except ZeroDivisionError:
                self.display.set_text("Div/0 Error")
        else:
            self.display.set_text("Error")

    def _clear_display(self):
        self.current_input = ""
        self.first_operand = None
        self.operator = None
        self.display.set_text("")


# Iniciar la calculadora
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Roman Calculator")
    controller = RomanCalculatorController(root)
    root.mainloop()
