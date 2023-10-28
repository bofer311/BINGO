# Bingo

## Servidor v0.0.1

### Servidor - Inicialización

    * IP, puerto y contraseña de anfitrón, se definen en archivo de configuración: "servidor.cfg".
    (ver sección "servidor.cfg")
    * Si no existe la BD sqlite, la crea (archivo y tablas), si existe, la carga en memoria para eventualmente poder continuarla.
    * Calcula el estado de la partida:

        * sin_cargar: no hay partida cargada (no hay jugadores ni cartones definidos)
        * por_iniciar: hay una partida cargada pero no se ha sacado ningún número
        * iniciada: ya se han sacado números y hay números por sacar
        * finalizada: no hay números por sacar

### archivo servidor.cfg

ip = 0.0.0.0 # todas las ip
puerto = 1586 # ISRG
pwd_anfitrion = "abc123"
bd = "bingo.sqllite"

### Acciones

- La secuencia de mensajes se especifican en el componente que inicia la petición, excepto estas primeras que las realizan tanto el Anfitrión como el Jugador (para especificarlo en un solo lugar)

#### Acciones de Anfitrón y Jugador

##### Conectar a servidor

- Cuando un cliente se conecta, el servidor se "presenta" indicando su versión, para que el cliente evalùe si es compatible...

###### Mensajes

> > > > > {

    "tipo":"servidor_presentacion",
    "servidor": {
        "version": "0.0.1"
    }

}

###### Controles:

    * Conectado o Online

#### Acciones de Anfitrón

- Ver el interacmbio de mensajes en anfitrión.md

<!-- ### (Conectar a servidor) -->

    * Se conecta al servidor
    * Recibe mensaje "servidor_presentacion"
    * Si el anfitrión soporta la versión del servidor, hace "Ingresar anfitrión"; si no, simplemente se desconecta.

- Aqui sólo se hacen algunas observaciones para tener en cuenta desde el punto de vista del servidor.

##### Ingresar anfitrión

    * Acepta si coincide la contraseña
    * Envía un ok/nok

###### Controles:

    * ???

### Cancelar partida

    * Elimina los datos de tablas y memoria de partida, jugador y carton

###### Controles:

    * ???

###### Salir anfitrión

    * Envía ok
    * Cierra conexión
    * Notar que no se elimina la partida. El anfitrión si se conecta, simplemente la cotinua, no es necesario empezar de nuevo.

###### Controles:

    * ???

##### Cargar Partida desde anfitrión

    * Reemplaza la eventual partida actual por la indicada en el mensaje
    * En bd:
        * partida.num_sacados = []
        * elimina cartones y jugadores
        * registra jugadores y cartones indicados en el mensaje

###### Controles:

    * ???

#### Sacar número

    * Define un nuevo número (1-90) que no esté en partida.num_sacados
    * Actualiza partida.num_sacados, agregando el número sacado AL FINAL de la lista
    * Si no quedan números por sacar, se finaliza la partida
    * Notifica al anfitrión
    * Notifica a cada jugador conectado

###### Controles:

    * ???

##### Mensaje a Jugadores

> > > > > {

    "tipo":"partida_numero_sacado",
    "datos": {
        "partida": {
            "num_sacados": [**52,21,73,44,75,56,78,87,90,10**],
            "estado": **"jugando"|"finalizada"**
        }
    }

}

#### Partida dump para anfitrión

    Envía al anfitrión el estado actual de la partida (al menos lo que al anfitrión le concierne)

###### Controles:

    * ???

#### Acciones de Jugador

##### Abrir conexión jugador

    * El jugador y contraseña debe existir en la bd
    * Envía un ok/nok

###### Controles:

    * ???

### Cerrar conexión jugador

    * Envía ok
    * Cierra conexión

###### Controles:

    * ???

#### Partida dump para jugadores

    Envía al jugador el estado actual de la partida (al menos lo que al jugador le concierne)

###### Controles:

    * ???

## Opcional:

### Menú/funcionalidades

    * Ver configuración (muestra en consola los datos del archivo de configuración)
    * Modificar contraseña anfitrión (pide la nueva contraseña y la guarda en servidor.cfg)
    * Ver partida
    * Salir
