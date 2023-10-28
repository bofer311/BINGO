from tkinter import *
from customtkinter import CustomTkinter

# Inicializa la ventana del servidor
root = Tk()
root.title("Servidor de Bingo")
root.geometry("400x300")

# Inicializa CustomTkinter
ctk = CustomTkinter(root)

# Crea una etiqueta para mostrar el estado de la partida
estado_label = Label(root, text="Estado de la partida: sin_cargar")
estado_label.pack()

# Crea un botón para cargar la partida


def cargar_partida():
    # Aquí puedes implementar la lógica para cargar la partida
    estado_label.config(text="Estado de la partida: iniciada")


cargar_button = ctk.create_button("Cargar Partida", command=cargar_partida)
cargar_button.pack()

# Crea un botón para sacar un número


def sacar_numero():
    # Aquí puedes implementar la lógica para sacar un número
    pass


sacar_button = ctk.create_button("Sacar Número", command=sacar_numero)
sacar_button.pack()

# Ejecuta la aplicación
root.mainloop()
