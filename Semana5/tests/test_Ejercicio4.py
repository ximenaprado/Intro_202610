from Semana5.Ejercicio4 import contar_asistencias

def test_asistencias():
    assert contar_asistencias([1, 1, 0]) == 2, \
        "Debes contar solo los valores 1 hasta que aparezca el 0."

def test_sin_asistencia():
    assert contar_asistencias([0]) == 0, \
        "Si el primer valor es 0, el total de asistencias debe ser 0."
