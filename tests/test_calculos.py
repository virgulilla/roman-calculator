from calc.models.calculos import Calculo, Operation, Status, RomanCalculo
from calc.models.roman_number import Roman_Number   
from calc.models.keys import Key, TiposTecla



def test_create_calculo():
    calculo = Calculo(1, 2, Operation.ADD)
    assert calculo.num_1 == 1
    assert calculo.num_2 == 2
    assert calculo.operation == Operation.ADD
    assert calculo.resultado == 3

    calculo = Calculo(1, 2, Operation.SUB)
    assert calculo.num_1 == 1
    assert calculo.num_2 == 2
    assert calculo.operation == Operation.SUB
    assert calculo.resultado == -1

def test_crear_calculos_incompletos():
    calculo = Calculo()
    assert calculo.num_1 is None    
    assert calculo.num_2 is None    
    assert calculo.operation is None    
    assert calculo.resultado is None   

    assert calculo.estado == Status.VACIO 

def test_crear_calculo_con_op1():
    calculo = Calculo(1)
    assert calculo.num_1 == 1    
    assert calculo.num_2 is None    
    assert calculo.operation is None    
    assert calculo.resultado is None   
    assert calculo.estado == Status.PARCIAL

def test_crear_calculo_con_operacion():
    calculo = Calculo(1, operation=Operation.ADD)
    assert calculo.num_1 == 1    
    assert calculo.num_2 is None    
    assert calculo.operation is Operation.ADD
    assert calculo.resultado is None   
    assert calculo.estado == Status.PENDIENTE    

def test_crear_calculo_completo():
    calculo = Calculo(1, 2, Operation.SUB)
    assert calculo.num_1 == 1    
    assert calculo.num_2 == 2    
    assert calculo.operation is Operation.SUB
    assert calculo.estado == Status.COMPLETO
    assert calculo.resultado == -1
    assert calculo.estado == Status.FINALIZADO

def test_add_digits_to_rc_vacio():
    rc = RomanCalculo()
    rc.add_key(Key("I", TiposTecla.DIGITS))

    assert rc.num_1 == Roman_Number("I")
    assert rc.operation is None
    assert rc.num_2 is None
    assert rc.estado == Status.PARCIAL

def test_add_digits_to_rc_parcial():
    rc = RomanCalculo(Roman_Number(1))
    rc.add_key(Key("V", TiposTecla.DIGITS))    
    assert rc.num_1 == Roman_Number(4)
    assert rc.operation is None
    assert rc.num_2 is None
    assert rc.estado == Status.PARCIAL

def test_add_digits_to_rc_pendiente():
    rc = RomanCalculo(Roman_Number(1), Operation.ADD)
    rc.add_key(Key("V", TiposTecla.DIGITS))    
    assert rc.num_1 == Roman_Number(1)
    assert rc.operation is Operation.ADD
    assert rc.num_2 == Roman_Number(5)
    assert rc.estado == Status.COMPLETO   

def test_add_digits_to_rc_completo():
    rc = RomanCalculo(Roman_Number(1), Roman_Number(5), Operation.ADD)
    rc.add_key(Key("I", TiposTecla.DIGITS))    
    assert rc.num_1 == Roman_Number(1)
    assert rc.operation is Operation.ADD
    assert rc.num_2 == Roman_Number(6)
    assert rc.estado == Status.COMPLETO    

def test_add_digits_to_rc_finalizado():
    rc = RomanCalculo(Roman_Number(1), Roman_Number(6), Operation.ADD)
    rc.resultado
    rc.add_key(Key("I", TiposTecla.DIGITS))    
    assert rc.num_1 == Roman_Number(1)
    assert rc.operation is None
    assert rc.num_2 is None
    assert rc.estado == Status.PARCIAL    