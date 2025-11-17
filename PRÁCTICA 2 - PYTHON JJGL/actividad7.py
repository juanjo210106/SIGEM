# Leer un carácter por teclado e indicar si es una letra mayúscula o no

caracter = input("Dime el caracter: ")
if caracter.islower():
    print("El caracter esta en MINÚSCULAS")
else:
    print("El caracter esta en MAYUSCULAS")