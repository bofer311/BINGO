import tkinter as tk
from tkinter import messagebox

# Función para manejar la acción de conexión del servidor


def conectar_servidor():
    ip = ip_entry.get()
    puerto = port_entry.get()
    password = password_entry.get()

    # Aquí puedes agregar la lógica de conexión al servidor
    # utilizando la información ingresada. Esto es un ejemplo
    # simplificado, debes adaptarlo a tu lógica real.

    try:
        # Supongamos que aquí intentamos establecer la conexión.
        # Reemplaza esta parte con tu propia lógica de conexión.
        # Puedes utilizar bibliotecas de red, sockets, etc.
        # Si la conexión es exitosa, muestra un mensaje de éxito.
        messagebox.showinfo("Éxito", "Conexión al servidor exitosa")
    except Exception as e:
        # Si hay un error en la conexión, muestra un mensaje de error.
        messagebox.showerror(
            "Error", f"No se pudo conectar al servidor: {str(e)}")


# Crear la ventana principal
main_window = tk.Tk()
main_window.title("Bingo Server")

# Crear una pestaña "Servidor"
tab_server = tk.Frame(main_window)

# Agregar campos de entrada y botón en la pestaña "Servidor"
ip_label = tk.Label(tab_server, text="IP")
ip_entry = tk.Entry(tab_server)
port_label = tk.Label(tab_server, text="Puerto")
port_entry = tk.Entry(tab_server)
password_label = tk.Label(tab_server, text="Password")
password_entry = tk.Entry(tab_server, show="*")  # Para ocultar la contraseña

connect_button = tk.Button(
    tab_server, text="Conectar", command=conectar_servidor)

# Colocar los widgets en la pestaña "Servidor"
ip_label.grid(row=0, column=0)
ip_entry.grid(row=0, column=1)
port_label.grid(row=1, column=0)
port_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)
connect_button.grid(row=3, column=1)

# Mostrar la pestaña "Servidor"
tab_server.pack()

# Iniciar el bucle principal de Tkinter
main_window.mainloop()
