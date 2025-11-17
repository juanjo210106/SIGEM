# Pedir una palabra por teclado e imprimirla 1000 veces por pantalla con espacios
# intermedios.


palabra = input("Introduce una palabra...: ")
interacciones = 0


while interacciones != 1000:
    print(f"{palabra} ", end="")
    interacciones += 1