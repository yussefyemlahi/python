# ahorcado.py

import mysql.connector
import random
import hashlib

def seleccionar_palabra():
    palabras = ["python", "programacion", "tecnologia", "computadora", "algoritmo"]
    return random.choice(palabras)

def mostrar_palabra(palabra, letras_adivinadas):
    palabra_mostrada = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_mostrada += letra
        else:
            palabra_mostrada += "_ "
    return palabra_mostrada

def jugar_ahorcado():
    palabra_secreta = seleccionar_palabra()
    letras_adivinadas = []
    intentos_maximos = 6
    intentos = 0

    while intentos < intentos_maximos:
        letra = input("Ingresa una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya adivinaste esta letra antes.")
            continue

        letras_adivinadas.append(letra)

        if letra not in palabra_secreta:
            intentos += 1
            print(f"Letra incorrecta. Te quedan {intentos_maximos - intentos} intentos.")
        else:
            print("¡Adivinaste una letra!")

        palabra_actual = mostrar_palabra(palabra_secreta, letras_adivinadas)
        print(palabra_actual)

        if palabra_actual == palabra_secreta:
            print("¡Ganaste! Has adivinado la palabra.")
            break

    if intentos == intentos_maximos:
        print(f"Perdiste. La palabra secreta era: {palabra_secreta}")

if __name__ == "__main__":
    jugar_ahorcado()



def conectar():
    # Modifica estos valores según tu configuración de MySQL
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='ahorcado'
    )
    return conexion

def crear_tabla(conexion):
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255),
            intentos INT,
            contraseña_hash VARCHAR(64) -- Almacenará el hash de la contraseña
        )
    ''')
    conexion.commit()

def insertar_usuario(conexion, nombre, intentos, contraseña):
    cursor = conexion.cursor()
    # Obtener el hash de la contraseña
    contraseña_hash = hashlib.sha256(contraseña.encode()).hexdigest()
    cursor.execute('''
        INSERT INTO usuarios (nombre, intentos, contraseña_hash)
        VALUES (%s, %s, %s)
    ''', (nombre, intentos, contraseña_hash))
    conexion.commit()

if __name__ == "__main__":
    jugar_ahorcado()

    conexion_mysql = conectar()
    crear_tabla(conexion_mysql)

    # Ejemplo de inserción de usuario después de jugar el ahorcado
    nombre_usuario = input("Ingresa tu nombre: ")
    intentos_usuario = 6  # Ajusta según los intentos del usuario en el juego
    contraseña_usuario = input("Ingresa tu contraseña: ")

    insertar_usuario(conexion_mysql, nombre_usuario, intentos_usuario, contraseña_usuario)

    # Cierra la conexión a MySQL
    conexion_mysql.close()