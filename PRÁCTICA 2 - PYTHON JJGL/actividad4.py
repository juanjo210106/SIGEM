# Recoge por teclado un número que represente un número del mes del año, y que indique
# por pantalla el número de días que tiene dicho mes. Incluye la validación necesaria para
# que el usuario introduzca un mes válido y en caso contrario, deberás avisar por pantalla.


import sys
numero = int(input("Dime el numero del mes del que quieres saber los dias: "))

if numero < 1 and numero > 12:
    print("Mes mal introducido")
    sys.exit()

if numero == 2:
    print("Tiene 28 dias")
    sys.exit()

if numero < 8 and numero % 2 == 0:
    print("Tiene 30 dias")

elif numero > 7 and numero % 2 != 0:
    print("Tiene 30 dias")
else :
    print("Tiene 31 dias")
