# Bingo

## Anfitrión v0.0.1

### Descripción

    * Inicia la partida cargando los jugadores y cartones.
    * Saca números

### (Conectar a servidor)

    * Se conecta al servidor
    * Recibe mensaje "servidor_presentacion"
    * Si el anfitrión soporta la versión del servidor, hace "Ingresar anfitrión"; si no, simplemente se desconecta.

### Ingresar anfitrión

#### Mensajes

> > > > > {

    "tipo":"anfitrion_ingresar",
    "datos": {
        "anfitrion": {
            "hash_contrasenna":"**contraseña-plana**"
        }
    }

}

<<<<< {
"tipo":"rta_anfitrion_ingresar",
"resultado": **0** // 0 = exito - 100 = error
}

### Salir anfitrión

    * Envía mensaje
    * ¿¿Espera respuesta??
    * Cierra conexión

#### Mensajes

> > > > > {

    "tipo":"anfitrion_salir",

}

<<<<< {
"tipo":"rta_anfitrion_salir",
"resultado": **0** // 0 = exito - 100 = error
}

### Cargar Partida desde anfitrión

    * Los datos se importan desde csv (tendrá dos tipo de líneas con los datos correspondientes: jugador y cartón).
    * El usuario debe indicar la ruta del archivo.

#### Mensajes

> > > > > {

    "tipo":"partida_cargar_partida",
    "datos": {
        "jugadores": {
            @jugador.nombre: {
                "hash_contrasenna":"v1-plana"
            },
            ... (más jugadores)
        },
        "cartones": {
            @jugador.nombre: [
                {
                    "nums": [
                        [**0,12,0,30,0,56,65,0,0,84**],
                        [**5,0,22,0,44,0,0,0,77,86**],
                        [**0,0,0,37,40,58,68,79,0,0**]
                    ]
                },
                ... (futura versión: más cartones del jugador)
            ],
            ... (más cartones de jugadores)
        }
    }

}

<<<<< {
"tipo":"rta_partida_cargar_partida",
"resultado": **0** // 0 = exito - 100 = error
"datos": { (sólo si fue exitoso)
"partida" = {
"id": @partida.id
"estado": "**por_iniciar**"
}
}
}

### Cancelar partida

#### Mensajes

> > > > > {

    "tipo":"partida_cancelar_partida",

}

<<<<< {
"tipo":"rta_partida_cancelar_partida",
"resultado": 0 // 0 = exito - 100 = error
"datos": { (sólo si fue exitoso)
"partida" = {
"estado": "cancelada"
}
}
}

### Sacar Número

#### Mensajes

> > > > > {

    "tipo":"partida_numero_sacar",

}

<<<<< {
"tipo":"rta_partida_numero_sacar",
"resultado": 0 // 0 = exito
// 100 = error
// 101 = la partida está finalizada
"datos": { (sólo si fue exitoso)
"partida": {
"num_sacados": [52,21,73,44,75,56,78,87,90,10],
"estado": "jugando"|"finalizada"
}
}
}

### Partida dump para anfitrión

#### Mensajes

> > > > > {

    "tipo":"partida_dump_anfitrion",

}

<<<<< {
"tipo":"rta_partida_dump_anfitrion",
"resultado": 0 // 0 = exito - 100 = error
"datos": { (sólo si fue exitoso)
"partida": {
"num_sacados": [52,21,73,44,75,56,78,87,90,10],
"estado": "por_iniciar"|"jugando"|"finalizada"
}
"jugadores": {
@jugador.nombre: {
"estado": "no_ingreso"|"jugando"|"salio"
},
... (más jugadores)
},
"cartones": {
@jugador.nombre: [
{
"nums": [
[0,12,0,30,0,56,65,0,0,84],
[5,0,22,0,44,0,0,0,77,86],
[0,0,0,37,40,58,68,79,0,0]
]
},
... (todos los cartones del jugador)
],
... (más jugadores)
}
}
}
