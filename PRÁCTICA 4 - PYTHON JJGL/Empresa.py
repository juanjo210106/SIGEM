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







