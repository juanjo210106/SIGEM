# Crea una aplicación que permita adivinar un número. En primer lugar, la aplicación
# solicita un número entero por teclado, que será el número que debe adivinarse. A
# continuación, va pidiendo números y va indicando por pantalla, si el número a adivinar
# es mayor o menor que el introducido. El programa termina cuando se acierta el número.


numero_secreto = int(input("Introduce el número secreto (entero): "))

# acertado = False

print("\n" * 50) 
print("¡Adivina el número!")

intento = -1
intentos = 0

while intento != numero_secreto:
    intento = int(input("Introduce tu intento: "))
    intentos += 1
    
    if intento < numero_secreto:
        print("El número secreto es MAYOR que", intento)
    elif intento > numero_secreto:
        print("El número secreto es MENOR que", intento)
    else:
        print(f"\n¡ENHORABUENA! ¡ADIVINASTE EL NÚMERO {numero_secreto}!")
        print(f"Te tomó {intentos} intentos.")