import random

# Función para generar una tarjeta de bingo


def generar_tarjeta():
    tarjeta = []
    for _ in range(5):
        columna = random.sample(range(1, 16), 5)
        tarjeta.append(columna)
    tarjeta[2][2] = "X"  # El centro es gratis
    return tarjeta

# Función para mostrar una tarjeta de bingo


def mostrar_tarjeta(tarjeta):
    for fila in tarjeta:
        for numero in fila:
            print(f"{numero:2}", end=" ")
        print()

# Función para llamar números aleatorios


def llamar_numero():
    return random.randint(1, 75)

# Función para verificar si hay un ganador


def verificar_ganador(tarjeta):
    # Verificar filas y columnas
    for i in range(5):
        if all(tarjeta[i][j] == "X" for j in range(5)):
            return True
        if all(tarjeta[j][i] == "X" for j in range(5)):
            return True

    # Verificar diagonales
    if all(tarjeta[i][i] == "X" for i in range(5)) or all(tarjeta[i][4 - i] == "X" for i in range(5)):
        return True

    return False

# Juego de Bingo


def jugar_bingo():
    print("¡Bienvenido al juego de Bingo!")
    tarjeta = generar_tarjeta()
    mostrar_tarjeta(tarjeta)

    llamados = set()
    while True:
        input("Presiona Enter para llamar un número...")
        numero_llamado = llamar_numero()
        print(f"Número llamado: {numero_llamado}")
        llamados.add(numero_llamado)

        for i in range(5):
            for j in range(5):
                if tarjeta[i][j] == numero_llamado:
                    tarjeta[i][j] = "X"

        mostrar_tarjeta(tarjeta)

        if verificar_ganador(tarjeta):
            print("¡Bingo! Tienes una tarjeta ganadora.")
            break


if __name__ == "__main__":
    jugar_bingo()
