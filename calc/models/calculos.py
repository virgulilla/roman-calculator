from enum import Enum

class Operation(Enum):
    ADD = "sumar"
    SUB = "restar"
    MUL = "multiplicar"
    DIV = "dividir"

class Calculo():
    def __init__(self, num_1, num_2, operation):
        self.num_1 = num_1
        self.num_2 = num_2
        self.operation = operation
        self.resultado = self.calcular()
    
    def calcular(self):
        if self.operation == Operation.ADD:
            return self.num_1 + self.num_2
        elif self.operation == Operation.SUB:
            return self.num_1 - self.num_2
        elif self.operation == Operation.MUL:
            return self.num_1 * self.num_2
        elif self.operation == Operation.DIV:
            if self.num_2 == 0:
                raise ValueError("Division by zero is not allowed.")
            return self.num_1 / self.num_2        
        else:
            raise ValueError(f"Operacion no permitida: {self.operation}")
