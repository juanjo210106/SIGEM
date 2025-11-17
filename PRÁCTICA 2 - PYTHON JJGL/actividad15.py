#  Escribir un programa que almacene el abecedario en una lista, elimine de la lista las
# letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(len(abecedario) - 2, 0, -3):
    abecedario.pop(i)

resultado = "" 
longitud = len(abecedario)

for i in range(longitud):
    letra = abecedario[i]
    resultado = resultado + letra 
    
    if i < longitud - 1:
        resultado = resultado + ", "

print(resultado)