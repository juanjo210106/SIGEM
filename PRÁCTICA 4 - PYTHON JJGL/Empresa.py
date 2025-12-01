from Empleado import Empleado

class Empresa:
    contador_empresa = 0

    def __init__(self, nombre, direccion, industria, telefono, correo, lista_empleados):
        self.nombre = nombre
        self.direccion = direccion
        self.industria = industria
        self.telefono = telefono
        self.correo = correo
        self.empleados = lista_empleados
        
        Empresa.contador_empresa = Empresa.contador_empresa + 1

    def __str__(self):
        return f"{self.nombre} | {self.direccion} | {self.industria} | Empleados: {len(self.empleados)}"

    def agregar_empleado(self, nuevo_empleado):
        ya_existe = False
        for e in self.empleados:
            if e.id_empleado == nuevo_empleado.id_empleado:
                ya_existe = True
        
        if ya_existe == True:
            print(f"[ERROR] El empleado {nuevo_empleado.nombre} ya existe.")
        else:
            self.empleados.append(nuevo_empleado)
            print(f"--> Empleado {nuevo_empleado.nombre} agregado correctamente.")


    def eliminar_empleado(self, id_para_borrar):
        empleado_encontrado = None

        for e in self.empleados:
            if e.id_empleado == id_para_borrar:
                empleado_encontrado = e
        
        
        if empleado_encontrado != None:
            self.empleados.remove(empleado_encontrado)
            print(f"--> Empleado con ID {id_para_borrar} eliminado.")
        else:
            print(f"[ERROR] No existe ningún empleado con ID {id_para_borrar}.")

    def calcular_costo_salarial(self):
        suma_total = 0
        for e in self.empleados:
            if e.contrato == True:
                suma_total = suma_total + e.salario
        return suma_total

    def listar_empleados(self):
        print(f"--- Lista de {self.nombre} ---")
        for e in self.empleados:
            print(e)
        print("----------------------------")


# --- ZONA DE PRUEBAS ---
kirri = Empleado(1, "Kirri", 19, "Informático", 1200, "2024-10-06", "kirri@mail.com", "693", "Calle A", "7h", True, None)
rafa = Empleado(2, "Rafa", 19, "Freelance", 1100, "2023-12-01", "rafa@mail.com", "693", "Calle B", "6h", True, None)


ecentia = Empresa("Ecentia", "Marbella", "Marketing", "900", "mail@ecentia.com", [kirri])


ecentia.agregar_empleado(rafa)

# Probamos agregar a Rafa OTRA VEZ (Debe dar error)
ecentia.agregar_empleado(rafa)

# 5. Listamos todos
ecentia.listar_empleados()

# Calcular cuánto dinero gastamos en salarios
dinero = ecentia.calcular_costo_salarial()
print(f"Coste total de salarios: {dinero} euros")

# Eliminamos a Kirri (ID 1)
ecentia.eliminar_empleado(1)

# Vemos que Kirri ya no está
ecentia.listar_empleados()