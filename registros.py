import mysql.connector

# Configuración de la conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ahorcado"
)

cursor = conexion.cursor()

def mostrar_registros():
    cursor.execute("SELECT * FROM ahorcado")
    registros = cursor.fetchall()

    print("Registros en la tabla:")
    for registro in registros:
        print(registro)

def modificar_registro():
    id_modificar = int(input("Ingrese el ID del registro que desea modificar: "))
    nuevo_nombre = input("Ingrese el nuevo nombre: ")
    nuevos_intentos = int(input("Ingrese los nuevos intentos: "))
    nueva_contrasena = input("Ingrese la nueva contraseña hash: ")

    cursor.execute("UPDATE usuarios SET nombre=%s, intentos=%s, contraseña_hash=%s WHERE id=%s",
                   (nuevo_nombre, nuevos_intentos, nueva_contrasena, id_modificar))
    conexion.commit()

    print("Registro modificado exitosamente.")

def borrar_registro():
    id_borrar = int(input("Ingrese el ID del registro que desea borrar: "))

    cursor.execute("DELETE FROM usuarios WHERE id=%s", (id_borrar,))
    conexion.commit()

    print("Registro borrado exitosamente.")

# Menú principal
while True:
    print("\n1. Mostrar registros")
    print("2. Modificar registro")
    print("3. Borrar registro")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        mostrar_registros()
    elif opcion == "2":
        modificar_registro()
    elif opcion == "3":
        borrar_registro()
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")

# Cerrar conexión
conexion.close()
