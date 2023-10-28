import socket

# Configuración del servidor
host = "127.0.0.1"  # La dirección IP del servidor
port = 1586  # El puerto del servidor
pwd_anfitrion = "abc123"  # La contraseña del anfitrión

# Crea el socket del anfitrión
anfitrion_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conéctate al servidor
try:
    anfitrion_socket.connect((host, port))
    print("Conexión exitosa al servidor")
except ConnectionRefusedError:
    print("No se pudo establecer la conexión con el servidor")
    exit(1)

# Envía la contraseña del anfitrión
anfitrion_socket.send(pwd_anfitrion.encode())

# Implementa el resto de la lógica de comunicación con el servidor aquí

# Cierra la conexión al servidor cuando sea necesario
anfitrion_socket.close()
