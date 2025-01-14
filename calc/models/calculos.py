from enum import Enum, auto
from calc.models.keys import Key, TiposTecla
from calc.models.roman_number import Roman_Number

class Operation(Enum):
    ADD = "+"
    SUB = "-"
    DIV = "/"
    MUL = "*"
    MOD = "%"

class Status(Enum):
    VACIO = auto()
    PARCIAL = auto()
    PENDIENTE = auto()
    COMPLETO = auto()
    FINALIZADO = auto()
    

class Calculo():
    def __init__(self, num_1: object=None, num_2:object=None, operation:Operation=None):
        self.num_1 = num_1
        self.num_2 = num_2
        self.operation = operation
        self.__is_finished = False
    
    @property
    def resultado(self) -> object:
        result = None
        if self.estado in (Status.COMPLETO, Status.FINALIZADO):
            if self.operation == Operation.ADD:
                result = self.num_1 + self.num_2
            elif self.operation == Operation.SUB:
                result = self.num_1 - self.num_2
            elif self.operation == Operation.MUL:
                result = self.num_1 * self.num_2
            elif self.operation == Operation.DIV:
                result = self.num_1 / self.num_2        
            elif self.operation == Operation.MOD:
                result = self.num_1 % self.num_2
            self.__is_finished = True
        return result           
        
    @property
    def estado(self) -> Status:
        if self.num_1 is None:
            return Status.VACIO
        elif self.operation is None:
            return Status.PARCIAL
        elif self.num_2 is None:
            return Status.PENDIENTE
        elif not self.__is_finished:
            return Status.COMPLETO
        else:
            return Status.FINALIZADO
        
class RomanCalculo(Calculo):
    __description: str = ""

    def add_key(self, key: Key):
        if key.tipo == TiposTecla.DIGITS:
            self.__description = ""
            if self.estado == Status.VACIO:
                self.num_1 = Roman_Number(key.valor)
            elif self.estado == Status.PARCIAL:
                nuevo_valor = self.num_1.representacion + key.valor 
                self.num_1 = Roman_Number(nuevo_valor)
            elif self.estado == Status.PENDIENTE:
                self.num_2 = Roman_Number(key.valor)
            elif self.estado == Status.COMPLETO:
                nuevo_valor = self.num_2.representacion + key.valor
                self.num_2 = Roman_Number(nuevo_valor)
            elif self.estado == Status.FINALIZADO:
                self.num_1 = None
                self.num_2 = None
                self.operation = None
                self.add_key(key) 
        elif key.tipo == TiposTecla.OPERATIONS:
            if self.estado == Status.PARCIAL:
                self.operation = Operation(key.valor)
            elif self.estado == Status.PENDIENTE:
                self.operation = Operation(key.valor)
            elif self.estado in  (Status.COMPLETO, Status.FINALIZADO):
                res = self.resultado
                super().__init__()
                self.num_1 = res
                self.operation = Operation(key.valor)
        elif key.tipo == TiposTecla.EQUAL:
            if self.estado == Status.COMPLETO:
                self.resultado
        elif key.tipo == TiposTecla.RESET:
            super().__init__()
            self.__description = ""        

    def get_display(self) -> str:
        res = ""
        if self.estado == Status.VACIO:
            res = ""
        elif self.estado == Status.PARCIAL:
            res = self.num_1.representacion
        elif self.estado == Status.PENDIENTE:
            res = self.num_1.representacion
        elif self.estado == Status.COMPLETO:
            res = self.num_2.representacion
        elif self.estado == Status.FINALIZADO:
            res = self.resultado.representacion
        return res      

    def get_resume(self) -> str:
        return self.__description
    
    @property
    def resultado(self):
        res = super().resultado
        if res is not None:
            self.__description = f"{self.num_1} {self.operation.value} {self.num_2} = {res}"
        return res            