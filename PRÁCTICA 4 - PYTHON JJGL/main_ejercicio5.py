from Empleado import Empleado
from Empresa import Empresa

# Lista para guardar las empresas (Pág 18: Listas)
empresas = []

def gestionar_empresa(emp):
    """Submenú para gestionar los empleados de una empresa concreta"""
    while True:
        print(f"\n--- GESTIÓN: {emp.nombre} ---")
        print("1.Agregar 2.Eliminar 3.Despedir 4.Coste 5.Listar 6.FiltroEdad 7.FiltroCargo 8.FiltroSalario 9.Volver")
        opcion = input("Elige opción: ")

        
        match opcion:
            case "1":
                
                id_emp = int(input("ID: "))
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                cargo = input("Cargo: ")
                salario = float(input("Salario: "))
                fecha = input("Fecha: ")

                # Creamos el empleado y lo añadimos
                nuevo = Empleado(id_emp, nombre, edad, cargo, salario, fecha, "", "", "", "", True, None)
                emp.agregar_empleado(nuevo)

            case "2":
                id_borrar = int(input("ID a eliminar: "))
                emp.eliminar_empleado(id_borrar)

            case "3":
                id_desp = int(input("ID a despedir: "))
                
                encontrado = False
                for e in emp.empleados:
                    if e.id_empleado == id_desp:
                        e.despedir()
                        encontrado = True
                        break # Paramos si lo encontramos
                if not encontrado:
                    print("Empleado no encontrado.")

            case "4":
                
                print("Coste total:", emp.calcular_costo_salarial())

            case "5":
                emp.listar_empleados()

            case "6": 
                min_e = int(input("Edad mínima: "))
                max_e = int(input("Edad máxima: "))
                print(f"--- Empleados entre {min_e} y {max_e} años ---")
                for e in emp.empleados:
                    
                    if e.contrato and (e.edad >= min_e and e.edad <= max_e):
                        print(e)

            case "7": 
                buscado = input("Cargo a buscar: ")
                for e in emp.empleados:
                    
                    if e.contrato and buscado in e.cargo:
                        print(e)

            case "8": 
                min_s = float(input("Salario mínimo: "))
                for e in emp.empleados:
                    if e.contrato and e.salario > min_s:
                        print(e)

            case "9":
                break 
            
            case _:
                print("Opción incorrecta")

def menu_principal():
    while True:
        print(f"\n=== EMPRESAS REGISTRADAS: {len(empresas)} ===")
        print("1.Crear 2.Listar 3.Borrar 4.Listar<10 5.Listar>=10 6.Gestionar 0.Salir")
        opcion = input("Elige opción: ")

        match opcion:
            case "1":
                nom = input("Nombre empresa: ")
                dir = input("Dirección: ")
                
                nueva = Empresa(nom, dir, "", "", "", [])
                empresas.append(nueva) # (Pág 18)

            case "2":
                # Usamos range y len para mostrar índice
                for i in range(len(empresas)):
                    print(f"{i}. {empresas[i]}")

            case "3":
                idx = int(input("Nº Empresa a borrar: "))
                if idx >= 0 and idx < len(empresas):
                    empresas.pop(idx) 
                else:
                    print("Número inválido")

            case "4":
                print("--- Empresas pequeñas (<10) ---")
                for emp in empresas:
                    if len(emp.empleados) < 10:
                        print(emp)

            case "5":
                print("--- Empresas grandes (>=10) ---")
                for emp in empresas:
                    if len(emp.empleados) >= 10:
                        print(emp)

            case "6":
                idx = int(input("Nº Empresa a gestionar: "))
                if idx >= 0 and idx < len(empresas):
                    gestionar_empresa(empresas[idx])
                else:
                    print("Empresa no existe")

            case "0":
                print("Saliendo...")
                break 

            case _:
                print("Opción no válida")

if __name__ == "__main__":
    menu_principal()