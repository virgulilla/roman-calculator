
from __future__ import annotations
from calc.models import a_arabigo, a_romano, RomanNumberError
from typing import Union, Callable

class Roman_Number:
    def __init__(self, value: Union[str, int]):
        if isinstance(value, int):
            self.representacion = a_romano(value)
            self.valor = value
        elif isinstance(value, str):
            self.valor = a_arabigo(value)
            self.representacion = value
        else:
            raise RomanNumberError("Solo se admiten enteros o cadenas")
        
    def __repr__(self):
        return self.representacion
    
    def __str__(self):
        return self.representacion
    
    def __operation(self, other: object, func: Callable, inverse: bool = False) -> Roman_Number:
        """
        1. Validar el tipo de other
        2. Realizar la operacion
        3. Devolver un romano con el valor suma
        """
        ops = {
            "__add__": "+",
            "__sub__": "-",
            "__mul__": "*",
            "__truediv__": "/",
            "__floordiv__": "//",
            "__mod__": "%",
            "__eq__": "==",
            "__lt__": "<",
            "__le__": "<=",
            "__gt__": ">",
            "__ge__": ">=",
            "__ne__": "!=",
        }

        if isinstance(other, int):
            number_value = other
        elif isinstance(other, Roman_Number):
            number_value = other.valor
        else:
            raise TypeError(f"'{ops.get(func.__name__, func.__name__)}' no permitida entre {Roman_Number.__name__} y {other.__class__.__name__}")
        
        res = func(self.valor, number_value) if not inverse else func(number_value, self.valor)

        return Roman_Number(res) if type(res) == int else res

    def __add__(self, other: object) -> Roman_Number:
        return self.__operation(other, int.__add__)
    
    def __radd__(self, other: object):
        return self.__add__(other)
    
    def __sub__(self, other: object):
        return self.__operation(other, int.__sub__)
    
    def __rsub__(self, other: object):
        return self.__operation(other, int.__sub__, inverse=True)
    
    def __mul__(self, other: object):
        return self.__operation(other, int.__mul__)

    def __rmul__(self, other: object):
        return self * other    

    def __truediv__(self, other: object):
        return self.__operation(other, int.__floordiv__)
    
    def __rtruediv__(self, other: object):
        return self.__operation(other, int.__floordiv__, inverse=True)

    def __floordiv__(self, other: object):
        return self.__operation(other, int.__floordiv__)
    
    def __rfloordiv__(self, other: object):
        return self.__operation(other, int.__floordiv__, inverse=True)

    def __mod__(self, other: object):
        return self.__operation(other, int.__mod__)  
        
    def __rmod__(self, other: object):
        return self.__operation(other, int.__mod__, inverse=True)  

    def __eq__(self, other: object) -> bool:
        return self.__operation(other, int.__eq__)
    
    def __lt__(self, other: object) -> bool: #less than
        return self.__operation(other, int.__lt__)
    
    def __le__(self, other: object) -> bool: #less or equal than
        return self.__operation(other, int.__le__)

    def __le__(self, other: object) -> bool: #greater than
        return self.__operation(other, int.__le__)
    
    def __gt__(self, other: object) -> bool: #greater or equal than
        return self.__operation(other, int.__gt__)
    
    def __ge__(self, other: object) -> bool: #greater or equal than
        return self.__operation(other, int.__ge__)
    
    def __ne__(self, other: object) -> bool: # not equal
        return self.__operation(other, int.__ne__)

    def __hash__(self):
        return hash(self.valor)
