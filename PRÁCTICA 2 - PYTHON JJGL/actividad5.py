#  Establece dos valores, uno para usuario y otro para contraseña. Solicita por pantalla dos
# palabras para que el usuario introduzca el usuario y la contraseña, y realiza la validación
# correspondiente.

usuario= "prueba"
contraseña = "1234"

txtUsuario = input("Introduce usuario: ")
txtContraseña = input("Introduce contraseña: ")

if txtUsuario == usuario and txtContraseña == contraseña:
    print("Has accedido con éxito")
else:
    print("[ERROR]: Credenciales incorrectas")