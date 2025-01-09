from calc.models.calculos import Calculo, Operation


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