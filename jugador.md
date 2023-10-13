# Bingo

## Jugador v0.0.1

### (Conectar a servidor)

    * recibe mensaje "servidor_presentacion"
    * si el jugador no soporta la versión del servidor, se desconecta;
      si la soporta, hace:

        * "Ingresar jugador";
        * "Partida dump para jugador"

### Ingresar jugador

#### Mensajes

> > > > > {

    "tipo":"jugador_ingresar",
    "datos": {
        "jugador": {
            "nombre":"jugA"
            "hash_contrasenna":"v1-plana; v2-sha512"
        }
    }

}

<<<<< {
"tipo":"rta_jugador_ingresar",
"resultado": 0 // 0 = exito - 100 = error
}

### Salir jugador

    * Envía mensaje
    * ¿¿Espera respuesta??
    * Cierra conexión

#### Mensajes

> > > > > {

    "tipo":"jugador_salir",

}

<<<<< {
"tipo":"rta_jugador_salir",
"resultado": 0 // 0 = exito - 100 = error
}

#### Partida dump para jugador

##### Mensajes

> > > > > {

    "tipo":"partida_dump_jugador",

}

<<<<< {
"tipo":"rta_partida_dump_jugador",
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
"cartones": { (El jugador recibe sólo su cartón )
@jugador.nombre: [
{
"nums": [
[0,12,0,30,0,56,65,0,0,84],
[5,0,22,0,44,0,0,0,77,86],
[0,0,0,37,40,58,68,79,0,0]
]
},
... (todos los cartones del jugador)
] (se utiliza lista, previendo que en futuras versiones el jugador pueda tener más cartones)
}
}
}

### Escucar mensajes

#### partida_numero_sacado:

    * Actualizar interfaz
    * (ver mensaje en servidor.md)
