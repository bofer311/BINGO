import socket

anfitrion_socket = socket.socket()

# Puerto donde me conecto

anfitrion_socket.connect(('127.0.0.1', 8000))


# Mensaje al servidor

anfitrion_socket.send("Hola permiso para conectar".encode())


# Respuesta servidor

respuesta = anfitrion_socket.recv(1024)


print(respuesta)
anfitrion_socket.close()
