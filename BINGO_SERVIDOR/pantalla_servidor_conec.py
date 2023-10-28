import tkinter as tk
import socket

# Configuración del servidor
server_host = "127.0.0.1"
server_port = 1586

# Crear un socket para comunicarse con el servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect((server_host, server_port))

# Función que se ejecutará cuando se haga clic en el botón "Conectar"


def conectar_con_servidor():
    # Enviar una solicitud al servidor para conectar a un anfitrión
    server_socket.send("conectar_anfitrion".encode())

    # Esperar una respuesta del servidor
    respuesta = server_socket.recv(1024).decode()

    # Procesar la respuesta y actualizar la GUI
    etiqueta_respuesta.config(text=respuesta)


# Configura la GUI con el botón "Conectar" y otras interfaces de usuario
ventana = tk.Tk()
ventana.title("GUI del Servidor")

boton_conectar = tk.Button(ventana, text="Conectar",
                           command=conectar_con_servidor)
boton_conectar.pack(padx=20, pady=10)

etiqueta_respuesta = tk.Label(ventana, text="")
etiqueta_respuesta.pack(padx=20, pady=10)

ventana.mainloop()
