from semana5.ejercicio1 import validar_contraseña

def test_contraseña_correcta():
    assert validar_contraseña(["123", "abc123"]) == "Acceso concedido", \
        "Revisa el ciclo while: debe continuar hasta encontrar la contraseña correcta."

def test_contraseña_incorrecta():
    assert validar_contraseña(["111", "222"]) == \
        "Contraseña incorrecta, ingrese contraseña nuevamente por favor.", \
        "Si nunca se ingresa la clave correcta, debe mostrarse el mensaje de error."
