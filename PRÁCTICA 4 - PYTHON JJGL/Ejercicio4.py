from Empleado import Empleado
from Empresa import Empresa


# Lista global para almacenar las instancias de Empresa
empresas = []

def crear_empresa():
    print("\n--- CREAR NUEVA EMPRESA ---")
    nombre = input("Nombre de la empresa: ")
    direccion = input("Dirección: ")
    industria = input("Industria/Sector: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")
    # Creamos la empresa con una lista de empleados vacía inicialmente
    nueva_empresa = Empresa(nombre, direccion, industria, telefono, correo, [])
    empresas.append(nueva_empresa)
    print(f"Empresa '{nombre}' creada correctamente.")

def crear_empleado():
    print("\n--- DATOS DEL NUEVO EMPLEADO ---")
    try:
        id_emp = int(input("ID del empleado (número): "))
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        cargo = input("Cargo: ")
        salario = float(input("Salario: "))
        fecha_con = input("Fecha contratación (YYYY-MM-DD): ")
        correo = input("Correo: ")
        telefono = input("Teléfono: ")
        direccion = input("Dirección: ")
        horario = input("Horario: ")
        # Por defecto contrato True y fecha_salida None al crear
        return Empleado(id_emp, nombre, edad, cargo, salario, fecha_con, correo, telefono, direccion, horario, True, None)
    except ValueError:
        print("[ERROR] Por favor, introduce datos numéricos válidos para ID, edad y salario.")
        return None

def gestionar_empresa(empresa):
    while True:
        print(f"\n=== GESTIONANDO: {empresa.nombre} ===")
        print("1. Listar empleados")
        print("2. Agregar empleado")
        print("3. Despedir empleado (Cambiar estado contrato)")
        print("4. Eliminar empleado (Borrar de la lista)")
        print("5. Calcular costo salarial")
        print("6. Volver al menú principal")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            empresa.listar_empleados()
            
        elif opcion == "2":
            nuevo_emp = crear_empleado()
            if nuevo_emp:
                empresa.agregar_empleado(nuevo_emp)
                
        elif opcion == "3":
            # Buscar empleado para despedir usando el método de la clase Empleado
            id_buscado = int(input("Introduce el ID del empleado a despedir: "))
            encontrado = False
            for emp in empresa.empleados:
                if emp.id_empleado == id_buscado:
                    emp.despedir() # Llama al método despedir de Empleado.py
                    encontrado = True
                    break
            if not encontrado:
                print(f"No se encontró empleado con ID {id_buscado}.")

        elif opcion == "4":
            id_borrar = int(input("Introduce el ID del empleado a eliminar: "))
            empresa.eliminar_empleado(id_borrar) # Llama al método de Empresa.py

        elif opcion == "5":
            total = empresa.calcular_costo_salarial()
            print(f"El costo total salarial es: {total}")

        elif opcion == "6":
            break
        else:
            print("Opción no válida.")

def menu_principal():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Crear nueva empresa")
        print("2. Seleccionar empresa para gestionar")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_empresa()

        elif opcion == "2":
            if not empresas:
                print("[!] No hay empresas creadas. Crea una primero.")
                continue

            print("\n--- SELECCIONAR EMPRESA ---")
            for i, emp in enumerate(empresas):
                print