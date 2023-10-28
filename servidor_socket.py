#!/usr/bin/python
# -*- coding: utf-8 -*-

# Programa Servidor
# www.pythondiario.com

import socket
# import sys

# Creando el socket TCP/IP
# Enlace de socket y puerto
serv_socket = socket.socket()
serv_socket.bind(('0.0.0.0', 8000))


# Escuchando conexiones entrantes

serv_socket.listen(5)

while True:
    # Esperando conexion
    conexion, address = serv_socket.accept()
    print("Nueva conexion")
    print(address)

    conexion.send("ingrese usuario y pasword".encode())

    conexion.close()
