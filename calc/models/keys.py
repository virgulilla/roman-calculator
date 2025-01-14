from enum import Enum

class TiposTecla(Enum):
    RESET = 1
    EQUAL = 2
    DIGITS = 3
    OPERATIONS = 4

class Key:
    def __init__(self, text:str, tipo:TiposTecla):
        self.valor = text
        self.tipo = tipo    