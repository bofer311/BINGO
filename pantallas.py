from customtkinter import CustomTkinter
import tkinter.messagebox as messagebox

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


# Crear una instancia de CustomTkinter
app = CustomTkinter()

# Crear la ventana principal
main_window = app.create_window("Bingo Server", (800, 600))

# Crear una pestaña "Servidor"
tab_server = app.create_tab("Servidor")

# Agregar campos de entrada y botón en la pestaña "Servidor"
ip_entry = app.create_input(tab_server, "IP")
port_entry = app.create_input(tab_server, "Puerto")
password_entry = app.create_input(
    tab_server, "Password", password=True)  # Para ocultar la contraseña

connect_button = app.create_button(
    tab_server, "Conectar", command=conectar_servidor)

# Personalizar la apariencia de la interfaz (opcional)
main_window.set_bg_color("lightgray")
tab_server.set_bg_color("lightblue")
ip_entry.set_width(20)
port_entry.set_width(20)
password_entry.set_width(20)

# Mostrar la ventana
main_window.run()
