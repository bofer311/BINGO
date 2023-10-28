import tkinter as tk
from tkinter import messagebox
import socket
import sqlite3
import random
import time
import configparser

# La lógica del servidor se copia aquí (desde 'import socket' hasta 'conexion.close()')
# ...

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

# Función para manejar la acción de conexión del servidor


def conectar_servidor():
    ip = ip_entry.get()
    puerto = port_entry.get()
    password = password_entry.get()
    try:
        # Supongamos que aquí intentamos establecer la conexión con la lógica del servidor.
        respuesta = procesar_mensaje(f"Ingresar anfitrión:{password}")
        if respuesta == "Acceso permitido":
            messagebox.showinfo("Éxito", "Conexión al servidor exitosa")
        else:
            messagebox.showerror(
                "Error", f"No se pudo conectar al servidor: {respuesta}")
    except Exception as e:
        messagebox.showerror(
            "Error", f"No se pudo conectar al servidor: {str(e)}")


# Crear la ventana principal
main_window = tk.Tk()
main_window.title("Bingo Server")

# Crear una pestaña "Servidor"
tab_server = tk.Frame(main_window)

# Agregar campos de entrada y botón en la pestaña "Servidor"
ip_label = tk.Label(tab_server, text="IP")
ip_entry = tk.Entry(tab_server)
port_label = tk.Label(tab_server, text="Puerto")
port_entry = tk.Entry(tab_server)
password_label = tk.Label(tab_server, text="Password")
password_entry = tk.Entry(tab_server, show="*")  # Para ocultar la contraseña

connect_button = tk.Button(
    tab_server, text="Conectar", command=conectar_servidor)

# Colocar los widgets en la pestaña "Servidor"
ip_label.grid(row=0, column=0)
ip_entry.grid(row=0, column=1)
port_label.grid(row=1, column=0)
port_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)
connect_button.grid(row=3, column=1)

# Mostrar la pestaña "Servidor"
tab_server.pack()

# Iniciar el bucle principal de Tkinter
main_window.mainloop()
