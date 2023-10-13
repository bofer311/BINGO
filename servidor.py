import socket
import sqlite3
import random
import time
import configparser

# Función para crear un cartón de Bingo


def crear_carton():
    carton = []
    numeros_disponibles = list(range(1, 91))

    for _ in range(3):
        fila = random.sample(numeros_disponibles, 5)
        carton.append(fila)
        for num in fila:
            numeros_disponibles.remove(num)

    return carton

# Función para generar un cartón de Bingo para un jugador específico


def generar_carton(jugador_id):
    carton = crear_carton()
    return carton

# Función para simular el sorteo de un número de Bingo


def sacar_numero_aleatorio():
    numero_sorteado = random.randint(1, 90)
    print(f"Sacando el número {numero_sorteado}...")
    time.sleep(2)
    return numero_sorteado

# Función para procesar mensajes del Anfitrión


def procesar_mensaje(mensaje):
    if mensaje.startswith("servidor_presentacion"):
        version_servidor = mensaje.split(":")[1]
        if version_servidor == "1.0":
            return "Aceptado"
        else:
            return "Rechazado: Versión incompatible"

    elif mensaje == f"Ingresar anfitrión:{pwd_anfitrion}":
        return "Acceso permitido"

    elif mensaje == "Comenzar partida bingo":
        if estado_partida == "sin_cargar":
            estado_partida = "por_iniciar"
            return "Partida en espera de inicio"
        else:
            return "No se puede iniciar la partida en este estado"

    else:
        return "Mensaje desconocido"

# Función para inicializar la base de datos


def inicializar_base_de_datos():
    conn = sqlite3.connect(bd)
    cursor = conn.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS jugadores (id INTEGER PRIMARY KEY, nombre TEXT)")

    cursor.execute("SELECT COUNT(*) FROM jugadores")
    if cursor.fetchone()[0] == 0:
        jugadores_ejemplo = [("Jugador1",), ("Jugador2",), ("Jugador3",)]
        cursor.executemany(
            "INSERT INTO jugadores (nombre) VALUES (?)", jugadores_ejemplo)

    conn.commit()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS cartones (id INTEGER PRIMARY KEY, jugador_id INTEGER, contenido TEXT)")

    cursor.execute("SELECT id FROM jugadores")
    jugadores = cursor.fetchall()

    for jugador in jugadores:
        jugador_id = jugador[0]
        carton = generar_carton(jugador_id)
        cursor.execute("INSERT INTO cartones (jugador_id, contenido) VALUES (?, ?)",
                       (jugador_id, str(carton)))

    conn.commit()
    conn.close()


# Variables de estado
estado_partida = "sin_cargar"
config = configparser.ConfigParser()
config.read("servidor.cfg")
ip = config.get("Servidor", "ip")
puerto = int(config.get("Servidor", "puerto"))
pwd_anfitrion = config.get("Servidor", "pwd_anfitrion")
bd = config.get("Servidor", "bd")

# Inicializar el servidor


def inicializar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((ip, puerto))
    servidor.listen(1)
    print(f"Servidor escuchando en {ip}:{puerto}")
    return servidor

# Función principal del servidor


def servidor_principal():
    inicializar_base_de_datos()
    servidor = inicializar_servidor()

    while True:
        conexion, direccion = servidor.accept()
        print(f"Conexión aceptada desde {direccion}")
        mensaje = conexion.recv(1024).decode()
        if mensaje:
            respuesta = procesar_mensaje(mensaje)
            conexion.send(respuesta.encode())
        conexion.close()


if __name__ == "__main__":
    servidor_principal()
