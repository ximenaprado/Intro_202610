'''#Realice un ejercicio que permita la validación de contraseña simple
#La contraseña correcta es "abc123".
#Tarea
#Solicita la contraseña al usuario hasta que sea correcta
# si la contraseña es correcta muestra "Acceso concedido".
# sino muestra "Contraseña incorrecta, ingrese contraseña nuevamente por favor."
'''
#Codigo de ejemplo...
clave ="abc123"
ingreso = "algo"
while clave != ingreso:
    ingreso = input("Ingrese clave por favor")

print("Clave ingresada corretamente, Hasta luego")
