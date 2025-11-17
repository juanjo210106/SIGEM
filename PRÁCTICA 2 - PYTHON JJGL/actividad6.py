# Leer un año por teclado e indicar si es bisiesto o no. Un año es bisiesto si es divisible por
# 4 y no es divisible por 100, o aquellos que son divisibles por 400

anio = input("Introduce el año: ")

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400):
    print("El año es bisiesto")
else: 
    print("El año no es bisiesto")