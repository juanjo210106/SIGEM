# Escribe un programa que diga si un número introducido por teclado es o no primo. Un
# número primo es aquel que sólo es divisible entre él mismo y la unidad.

numero = int(input("Introduce un número entero para comprobar si es primo: "))

if numero <= 1:
    print(f"El número {numero} NO es primo.")

elif numero == 2:
    print(f"El número {numero} ES primo.")

else:
    es_primo = True 
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
    
    if es_primo:
        print(f"El número {numero} ES primo.")
    else:
        print(f"El número {numero} NO es primo.")