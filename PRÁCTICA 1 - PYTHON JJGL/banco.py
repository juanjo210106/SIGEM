capital_inicial = float(input("Introduce el capital inicial (€): "))
tipo_interes = float(input("Introduce el tipo de interés anual (%): "))

interes_obtenido = capital_inicial * (tipo_interes / 100)

print(f"El interés obtenido es: {interes_obtenido} €")