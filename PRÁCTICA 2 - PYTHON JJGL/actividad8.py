# Pedir un número por teclado y mostrar la tabla de multiplicar. Realiza una solución con
# while y otra con for

numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
i = 1

print("Tabla de multiplicar del", numero, "con for:")
## Si ponemos en el range 3, 11 --> Empieza por el tres
for i in range(11):
    print(f"{numero} x {i} = {numero * i}")
    i += 1


print(" ")
i = 1

print("Tabla de multiplicar del", numero, "con while:")
while i <= 10:
    print(f"{numero} x {i} = {numero * i}")
    i += 1
