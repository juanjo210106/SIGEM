from datetime import datetime

class Empleado:
    contador_empleado = 0;

    def __init__(self, id_empleado, nombre, edad, cargo, salario, fecha_contratacion, correo, telefono, direccion, horario, contrato, fecha_salida):
        self.id_empleado = id_empleado
        self.nombre = nombre;
        self.edad = edad;
        self.cargo = cargo;
        self.salario = salario;
        self.fecha_contratacion = fecha_contratacion;
        self.correo = correo;
        self.telefono = telefono;
        self.direccion = direccion;
        self.horario = horario;
        self.contrato = contrato;
        self.fecha_salida = fecha_salida;

    def __str__(self):
        return f"{self.id_empleado} {self.nombre} {self.edad} {self.cargo} {self.salario} {self.fecha_contratacion} {self.correo} {self.telefono} {self.direccion} {self.direccion} {self.horario} {self.contrato} {self.fecha_salida}"
    
    def despedir(e):
        if (e.contrato == True):
            e.contrato = False;
            e.fecha_salida = datetime.now();
            print("El empleado ",e.nombre," ha sido despedido el",e.fecha_salida)
        else:
            print(f"El emplado {e.nombre} ya ha sido despedido el {e.fecha_salida}")

"""
emp1 = Empleado(1, "Kirri", 19, "Informático", 1200, "2024-10-06", "kirriecentia@gmail.com", "693 384 189", "Carretera los olivares", "7 horas", True, None)
emp2 = Empleado(2, "Rafa", 19, "Freelance", 1100, "2023-12-01", "rafaecentia@gmail.com", "693 384 189", "Carretera los olivares", "6 horas", True, None)

print(f"Empleado {emp1.nombre}:")
print(emp1.__str__())

print("")
print("Despidiendo empleados...")
emp1.despedir()
emp2.despedir()

"""



