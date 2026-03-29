from src.ejercicio3 import validar_retiro

def test_valido():
    assert validar_retiro([5, 12, 50]) == "Retiro exitoso", \
        "El monto válido debe ser mayor a 0 y múltiplo de 10."

def test_invalido():
    assert validar_retiro([7, -10, 3]) == "Monto inválido", \
        "Si ningún monto cumple la condición, debe informarse como inválido."
