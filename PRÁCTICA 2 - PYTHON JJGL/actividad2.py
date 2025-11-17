#  Pedir un número por teclado, e indicar por pantalla, si es positivo, negativo o cero.

num = int(input("Introduce un número: "))

if num > 0:
    print(f": EL NÚMERO {num} ES POSITIVO")
elif num == 0:
    print(f": EL NÚMERO {num} ES 0")
else:
    print(f": EL NÚMERO {num} ES NEGATIVO")