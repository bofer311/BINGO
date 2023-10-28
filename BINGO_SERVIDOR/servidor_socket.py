import socket
import sqlite3
import json

# Cargar configuración desde el archivo "servidor.cfg"

# config = {
#     "ip": "0.0.0.0",
#     "puerto": 1586,
#     "pwd_anfitrion": "abc123",
#     "bd": "bingo.sqlite",
# }

config = {

}

with open("servidor.cfg", "r", encoding="utf-8") as cfg_file:
    for line in cfg_file:
        parts = line.strip().split(" = ")
        if len(parts) == 2:
            key, value = parts
            config[key] = value

# Configuración del servidor

host = config.get("ip", "0.0.0.0")
port = int(config.get("puerto", 1586))
pwd_anfitrion = config.get("pwd_anfitrion", "abc123")
db_file = config.get("bd", "bingo.sqlite")
server_version = ['0.0.1']

# Inicializar la base de datos o cargarla si existe

connection = sqlite3.connect(db_file)
cursor = connection.cursor()

# Verificar si la tabla existe en la base de datos

cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table' AND name='partida';")
table_exists = cursor.fetchone() is not None

if not table_exists:
    # Si la tabla "partida" no existe, créala

    cursor.execute(
        "CREATE TABLE partida (id INTEGER PRIMARY KEY, estado TEXT, num_sacados TEXT);")
    connection.commit()

# Calcular el estado de la partida

cursor.execute("SELECT estado FROM partida;")
estado_partida = cursor.fetchone()
if estado_partida:
    estado_partida = estado_partida[0]
else:
    estado_partida = "sin_cargar"

# Inicializar el servidor

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

print(f"Servidor de Bingo escuchando en {host}: {port}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Nueva conexión desde {client_address}")

    # Cuando un cliente se conecta, el servidor se "presenta" con su versión

    presentacion_servidor = {
        "tipo": "servidor_presentacion",
        "servidor": {
            "version": "0.0.1"  # Versión del servidor
        }
    }

    # Serializa la presentación como JSON y envía al cliente
    presentacion_json = json.dumps(presentacion_servidor)
    client_socket.send(presentacion_json.encode())

    # Agrega un carácter de nueva línea para indicar el final de la respuesta
    client_socket.send("\n".encode())

    # Recibe la contraseña enviada por el anfitrión
    anfitrion_password = client_socket.recv(1024).decode()

    if anfitrion_password == pwd_anfitrion:
        # Contraseña correcta, puedes enviar una respuesta al anfitrión
        response = "Contraseña correcta. Conexión exitosa."
        client_socket.send(response.encode())
        print("Conexión exitosa con el anfitrión")
    else:
        # Contraseña incorrecta, puedes enviar una respuesta de error al anfitrión
        response = "Contraseña incorrecta. Conexión fallida."
        client_socket.send(response.encode())
        print("Conexión fallida con el anfitrión")

    # Implementa el resto de la lógica de comunicación con el anfitrión aquí
    # Asegúrate de manejar las acciones necesarias

    # Cierra la conexión con el anfitrión cuando sea necesario
    client_socket.close()
