from semana5.ejercicio2 import clasificar_temperatura

def test_fria():
    assert clasificar_temperatura(5) == "Fría", \
        "Recuerda: temperaturas menores a 10°C son Frías."

def test_templada():
    assert clasificar_temperatura(20) == "Templada", \
        "Entre 10 y 25 grados debe clasificarse como Templada."

def test_calurosa():
    assert clasificar_temperatura(30) == "Calurosa", \
        "Temperaturas mayores a 25°C son Calurosas."
