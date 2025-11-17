# Amplia el ejercicio anterior, y pide por pantalla 2 números. Comprueba si la suma de los
# dos números es positiva, negativa o cero.

num1 = int(input("1. Introduce un número: "))
num2 = int(input("2. Introduce un número: "))

num = num1+num2

if num > 0:
    print(f": EL NÚMERO {num} ES POSITIVO")
elif num == 0:
    print(f": EL NÚMERO {num} ES 0")
else:
    print(f": EL NÚMERO {num} ES NEGATIVO")