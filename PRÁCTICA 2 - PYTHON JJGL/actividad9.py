# Crea una aplicación que pida un número y calcule su factorial. El factorial de un número
# es el producto de todos los números enteros entre 1 y el ese número y se representa por
# el número seguido de un signo de exclamación. P. ej. 6! = 1x2x3x4x5x6=720. Realiza una
# propuesta con while y otra con for.

numero = int(input("Introduce un número entero positivo para calcular su factorial: "))
factorial = 1
contador = 1

if numero < 0:
    print("El factorial no está disponible para números negativos.")
elif numero == 0:
    print("El factorial de 0 es 1")
else:
    while contador <= numero:
        factorial = factorial * contador
        contador += 1
    print(f"El factorial de {numero} ({numero}!) es: {factorial}")



## ------------------------------

numero = int(input("Introduce un número entero positivo para calcular su factorial: "))
factorial = 1

if numero < 0:
    print("El factorial no está disponible para números negativos.")
elif numero == 0:
    print("El factorial de 0 es 1")
else:
    for i in range(1, numero + 1):
        factorial = factorial * i
    print(f"El factorial de {numero} ({numero}!) es: {factorial}")