import tkinter as tk
from calc.views import Calculator


def fn_delegada(btn_clickado: str):
    calc.show(btn_clickado)

root = tk.Tk()
root.pack_propagate(True)

calc = Calculator(root, fn_delegada)
calc.pack()


root.mainloop()