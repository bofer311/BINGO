import socket
import sqlite3

# Cargar configuración desde el archivo "servidor.cfg"
config = {}
with open("servidor.cfg", "r") as cfg_file:
    for line in cfg_file:
        key, value = line.strip().split(" = ")
        config[key] = value

# Configuración del servidor
host = config.get("ip", "0.0.0.0")
port = int(config.get("puerto", 1586))
pwd_anfitrion = config.get("pwd_anfitrion", "abc123")
db_file = config.get("bd", "bingo.sqlite")

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

    # Implementa el manejo de la conexión y comunicación con el anfitrión aquí
    # Asegúrate de verificar la contraseña del anfitrión y manejar las acciones necesarias

# Cierra la conexión al servidor cuando sea necesario
server_socket.close()
