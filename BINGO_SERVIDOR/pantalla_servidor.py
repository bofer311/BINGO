import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import socket
import json

# Configuración del servidor
host = "127.0.0.1"
# Cambié el puerto a un entero, ya que el puerto debe ser un número.
port = 1586
pwd_anfitrion = "abc123"
server_version = "0.0.1"  # Versión del servidor

# Socket del anfitrión
anfitrion_socket = None

# Función para conectar al servidor


def connect_to_server():
    global anfitrion_socket
    ip = ip_entry.get()
    port = int(port_entry.get())
    password = password_entry.get()

    anfitrion_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        anfitrion_socket.connect((ip, port))
        print("Conexión exitosa al servidor")

        # Recibe la presentación del servidor
        data = anfitrion_socket.recv(1024).decode()

        # Verifica si la respuesta no está vacía
        if data:
            presentacion_servidor = json.loads(data)

            if "tipo" in presentacion_servidor and presentacion_servidor["tipo"] == "servidor_presentacion":
                server_version = presentacion_servidor["servidor"]["version"]
                print(
                    f"El servidor está en línea y tiene la versión {server_version}")

                if server_version != "0.0.1":
                    print("Versión de servidor no compatible. Se desconectará.")
                    anfitrion_socket.close()
                    return
            else:
                print("El servidor no envió la presentación esperada.")
        else:
            print("Respuesta vacía del servidor. Verifica la comunicación.")

        # Resto del código para enviar contraseña y recibir respuesta
    except ConnectionRefusedError:
        print("No se pudo establecer la conexión con el servidor")


# Crear la ventana de configuración del servidor
root = tk.Tk()
root.title("Configuración del Servidor")

# Estilo moderno utilizando ttkthemes
style = ThemedStyle(root)
style.set_theme("plastik")

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

ip_label = ttk.Label(frame, text="Dirección IP del Servidor:")
ip_label.grid(row=0, column=0, sticky="w")

ip_entry = ttk.Entry(frame)
ip_entry.grid(row=0, column=1)

port_label = ttk.Label(frame, text="Puerto:")
port_label.grid(row=1, column=0, sticky="w")

port_entry = ttk.Entry(frame)
port_entry.grid(row=1, column=1)
# Rellenar automáticamente con el puerto predeterminado
port_entry.insert(0, str(port))

password_label = ttk.Label(frame, text="Contraseña del Anfitrión:")
password_label.grid(row=2, column=0, sticky="w")

password_entry = ttk.Entry(frame, show="*")  # Para ocultar la contraseña
password_entry.grid(row=2, column=1)

connect_button = ttk.Button(
    frame, text="Conectar al Servidor", command=connect_to_server)
connect_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
