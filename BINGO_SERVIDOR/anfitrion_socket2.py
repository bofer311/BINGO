import socket
import json

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

# Recibe el mensaje "servidor_presentacion" del servidor

data = anfitrion_socket.recv(1024).decode()
mensaje_servidor = json.loads(data)

# Verifica la versión del servidor

if "tipo" in mensaje_servidor and mensaje_servidor["tipo"] == "servidor_presentacion":
    if "servidor" in mensaje_servidor and "version" in mensaje_servidor["servidor"]:
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
            "hash_contrasenna": pwd_anfitrion
        }
    }
}

anfitrion_socket.send(json.dumps(mensaje_ingresar).encode())

# Recibe la respuesta del servidor
data = anfitrion_socket.recv(1024).decode()
respuesta_ingresar = json.loads(data)

# Verifica si el resultado es exitoso
if "tipo" in respuesta_ingresar and respuesta_ingresar["tipo"] == "rta_anfitrion_ingresar":
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
data = anfitrion_socket.recv(1024).decode()
respuesta_salir = json.loads(data)

# Verifica si el resultado es exitoso
if "tipo" in respuesta_salir and respuesta_salir["tipo"] == "rta_anfitrion_salir":
    resultado = respuesta_salir.get("resultado", -1)
    if resultado == 0:
        print("Salida exitosa como anfitrión.")
    else:
        print("Error en la salida como anfitrión.")

# Cierra la conexión al servidor
anfitrion_socket.close()
