import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import socket
import json

# Configuración del servidor
host = "127.0.0.1"
port = 1586
pwd_anfitrion = "abc123"

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
    except ConnectionRefusedError:
        print("No se pudo establecer la conexión con el servidor")
        return

    # Envía el mensaje "anfitrion_ingresar" con la contraseña del anfitrión
    mensaje_ingresar = {
        "tipo": "anfitrion_ingresar",
        "datos": {
            "anfitrion": {
                "hash_contrasenna": password
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
            return

    # Cierra la ventana de configuración del servidor
    root.destroy()


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

password_label = ttk.Label(frame, text="Contraseña del Anfitrión:")
password_label.grid(row=2, column=0, sticky="w")

password_entry = ttk.Entry(frame, show="*")  # Para ocultar la contraseña
password_entry.grid(row=2, column=1)

connect_button = ttk.Button(
    frame, text="Conectar al Servidor", command=connect_to_server)
connect_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
