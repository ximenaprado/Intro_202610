from semana5.ejercicio1 import validar_contraseña

def test_contraseña_correcta():
    assert validar_contraseña(["123", "abc123"]) == "Acceso concedido", \
        "Revisa el while: debe repetirse hasta que la contraseña sea correcta."
