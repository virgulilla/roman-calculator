from collections import namedtuple
from typing import List, Tuple

Symbol = namedtuple("Symbol", ("unitario", "quintuple"))
RomanGroup = namedtuple("RomanGroup", ("symbol", "num_miles"))
RomanPosition = namedtuple("RomanPosition", ("valor", "orden", "symbol"))

class RomanNumberError(Exception):
    pass

symbols = [Symbol("I", "V"),
           Symbol("X", "L"),
           Symbol("C", "D"),
           Symbol("M", None)]

def posiciones(n: int):
    resultado = []
    while True:
        resultado.append(n % 10)
        n = n // 10
        if n == 0:
            break
    return resultado

def traduce_a_roman_group(valor: int, orden: int):
    cuenta_miles = 0

    while orden > 3 or (valor > 3 and orden == 3):
        orden -= 3
        cuenta_miles += 1

    if valor < 4:
        resultado = symbols[orden].unitario * valor
    elif valor < 5:
        resultado = symbols[orden].unitario + symbols[orden].quintuple
    elif valor < 9:
        resultado = symbols[orden].quintuple + symbols[orden].unitario * (valor - 5)
    else:
        resultado = symbols[orden].unitario + symbols[orden + 1].unitario
    
    return RomanGroup(resultado, cuenta_miles)

def agrupa_by_orden(digits: List[RomanGroup]) -> List[List[str]]:
    r = []
    for digit in digits:
        if digit.num_miles + 1 > len(r):
            r.append([] * (digit.num_miles + 2 - len(r)))
        r[digit.num_miles].append(digit.symbol)
    return r

def a_romano(n: int) -> str:
    thousand_symbol = "•"
    components = posiciones(n)
    digits = []
    for orden, posicion in enumerate(components):
        digits.append(traduce_a_roman_group(posicion, orden))
        if len(digits) > 1:
            prev_digit = digits[-2]
            if prev_digit.symbol and prev_digit.symbol in "MMM":
                digits[-2] = RomanGroup(prev_digit.symbol.replace("M", "I"), prev_digit.num_miles + 1)
    t = agrupa_by_orden(digits)

    resultado = []
    for num_miles, group in enumerate(t):
        symbol = "".join(group[::-1])
        resultado.append(symbol + thousand_symbol * num_miles if symbol else '')
    
    return "".join(resultado[::-1])

def find_symbol(ch: str) -> Tuple[int, int]:
    for ix, (uno, cinco) in enumerate(symbols):
        if ch == uno:
            return (1, ix)
        elif ch == cinco:
            return (5, ix)
    raise RomanNumberError("Símbolo no válido")

def divide_en_roman_thousands(romano: str) -> List[RomanGroup]:
    resultado = []
    miles = None
    umbral_miles = float("inf")
    symbol = ""
    for cypher in romano:
        if cypher != "•":
            if miles is not None:
                if miles >= umbral_miles:
                    raise RomanNumberError("Orden incorrecto en los indicadores")
                resultado.append(RomanGroup(symbol, miles))
                umbral_miles = miles
                miles = None
                symbol = ""           
            symbol += cypher
        else:
            miles = 1 if miles is None else miles + 1

    if miles and miles >= umbral_miles:
        raise RomanNumberError("Orden incorrecto en los indicadores")        
    resultado.append(RomanGroup(symbol, miles or 0))
    return resultado

def divide_en_roman_positions(romano: str) -> List[RomanPosition]:
    accum = 0
    symbol = ""
    last_order = None
    positions = []
    for cypher in romano:
        valor, orden = find_symbol(cypher)
        if last_order is None or orden == last_order:
            if valor == 5 and accum == 1:
                accum = 4
            elif valor == 5 and accum == 0 or \
                 valor == 1 and (accum < 3 or accum in range(5, 8)):
                accum += valor
            elif valor == 1 and accum == 4:
                raise RomanNumberError(f"Tras resta debe bajar el orden {symbol + cypher}")
            elif valor == 1:
                raise RomanNumberError(f"No mas de 3 repeticiones {symbol + cypher}")
            else:
                raise RomanNumberError(f"No se puede repetir {symbol + cypher}")

            last_order = orden
            symbol += cypher
        elif orden == last_order + 1:
            if accum == 1 and valor == 1:
                accum = 9
            else:
                raise RomanNumberError(f"Resta prohibida {symbol + cypher}")
            symbol += cypher
        elif orden > last_order:
            raise RomanNumberError(f"Los numeros deben ir en secuencia descendente {symbol + cypher}")
        else:
            positions.append(RomanPosition(accum, last_order, symbol))
            symbol = cypher
            accum = valor
            last_order = orden
    positions.append(RomanPosition(accum, last_order, symbol))
    return positions

def a_arabigo(romano: str) -> int:
    groups = divide_en_roman_thousands(romano)
    tot = 0
    for group in groups:
        positions = divide_en_roman_positions(group.symbol)
        accum = 0
        for position in positions:
            accum += position.valor * 10 ** position.orden
        tot += accum * 1000 ** group.num_miles
    return tot 