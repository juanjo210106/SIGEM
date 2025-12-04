from Empleado import Empleado
from Empresa import Empresa

kirri = Empleado(1, "Kirri", 19, "Informático", 1200, "2024-10-06", "kirri@mail.com", "693", "Calle A", "7h", True, None)
rafa = Empleado(2, "Rafa", 19, "Freelance", 1100, "2023-12-01", "rafa@mail.com", "693", "Calle B", "6h", True, None)


ecentia = Empresa("Ecentia", "Marbella", "Marketing", "900", "mail@ecentia.com", [kirri])



ecentia.agregar_empleado(kirri)
ecentia.agregar_empleado(rafa)


ecentia.listar_empleados()



# Calcular cuánto dinero gastamos en salarios
dinero = ecentia.calcular_costo_salarial()
print(f"Coste total de salarios: {dinero} euros")



alan = Empleado(1, "Alan", 20, "SEO", 1300, "2022-09-5", "alan@mail.com", "691", "Calle C", "8h", False, None)
ecentia.agregar_empleado(alan)
ecentia.listar_empleados()
dinero = ecentia.calcular_costo_salarial()
print(f"... El coste total de salarios es de: {dinero} €")

# Eliminamos a Kirri (ID 1)
ecentia.eliminar_empleado(1)
ecentia.listar_empleados()
dinero = ecentia.calcular_costo_salarial()
print(f".. El coste total de salarios es de: {dinero} €")