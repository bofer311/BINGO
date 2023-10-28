import socket
import json

# Configuración del servidor
host = "127.0.0.1"
port = 1586
pwd_anfitrion = "abc123"

# Crea el socket del anfitrión
anfitrion_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conéctate al servidor
try:
    anfitrion_socket.connect((host, port))
    print("Conexión exitosa al servidor")
except ConnectionRefusedError:
    print("No se pudo establecer la conexión con el servidor")
    exit(1)

# Recibe el mensaje "servidor_presentacion" del servidor
mensaje_servidor = anfitrion_socket.recv(1024).decode()
mensaje_servidor = json.loads(mensaje_servidor)

# Verifica la versión del servidor
if mensaje_servidor["tipo"] == "servidor_presentacion":
    version_servidor = mensaje_servidor["servidor"]["version"]
    if version_servidor == "0.0.1":
        print("Versión del servidor compatible: ", version_servidor)
    else:
        print("Versión del servidor no es compatible. Se desconectará.")
        anfitrion_socket.close()
        exit(1)

# Envía el mensaje "anfitrion_ingresar" con la contraseña del anfitrión
mensaje_ingresar = {
    "tipo": "anfitrion_ingresar",
    "datos": {
        "anfitrion": {
            "contrasenna_hash": pwd_anfitrion
        }
    }
}
anfitrion_socket.send(json.dumps(mensaje_ingresar).encode())

# Recibe la respuesta del servidor
respuesta_ingresar = anfitrion_socket.recv(1024).decode()
respuesta_ingresar = json.loads(respuesta_ingresar)

# Verifica si el resultado es exitoso
if respuesta_ingresar["tipo"] == "rta_anfitrion_ingresar":
    resultado = respuesta_ingresar.get("resultado", -1)
    if resultado == 0:
        print("Ingreso exitoso como anfitrión.")
    else:
        print("Error en el ingreso como anfitrión. Se desconectará.")
        anfitrion_socket.close()
        exit(1)

# Envía el mensaje "anfitrion_salir"
mensaje_salir = {
    "tipo": "anfitrion_salir"
}
anfitrion_socket.send(json.dumps(mensaje_salir).encode())

# Recibe la respuesta del servidor
respuesta_salir = anfitrion_socket.recv(1024).decode()
respuesta_salir = json.loads(respuesta_salir)

# Verifica si el resultado es exitoso
if respuesta_salir["tipo"] == "rta_anfitrion_salir":
    resultado = respuesta_salir.get("resultado", -1)
    if resultado == 0:
        print("Salida exitosa como anfitrión.")
    else:
        print("Error en la salida como anfitrión.")

# Cierra la conexión al servidor
anfitrion_socket.close()
