# Bingo v0.0.1

    # Juego de bingo en red.

    # Un "anfitrión" se conecta a un servidor, carga la partida (jugadores y cartones) y va sacando números.

    # Cada "Jugador" se conecta al servidor, recibe su cartón y espera notificaciones del estado de la partida.

    # El servidor va actualizando y notificando al anfitrión y a los jugadores.

### Servidor

    # * Gestiona una única partida a la vez.
    # * Sólo puede haber un anfitrión conectado
    # * Sólo pueden conectarse los jugadores de la partida.
    # * Interfaz de consola

### Anfitrión

    # * Inicia la partida cargando los jugadores y cartones.
    # * Saca números
    # * GUI - ver imagen en "todas las pantallas.png"

### Jugador

    # * Recibe notificaciones del estado de la partida
    # * GUI - ver imagen en "todas las pantallas.png"

### Otras funcionalidades opcionales:

# \* "Crear suspenso" (notificar a los jugadores que se está sacando un número, esperar unos segundos y luego notificar el número sacado)

# \* Cliente "visor" (visualiza la partida, pensando en pantallas gigantes por ejemplo).

# \* El cartón se genera automáticamente al ingresar un jugador.

# \* Gestión de jugadores.

# \* Gestión de anfitriones.

# \* Gestión de partidas.

# \* Multiples cartones por jugador.

# \* Chat entre jugadores.
