db.juego.insertMany([
    {
        nombre: 'fifa 2022',
        info: {
            tipo: 'deporte',
            costos: [{
                consola: 'xbox',
                valor: 40000
            },
            {
                consola: 'ps5',
                valor: 45000
            },
            {
                consola: 'pc',
                valor: 43000
            }]
        }
    },
    {
        nombre: 'minecraft',
        info: {
            tipo: 'aventura',
            costos: [{
                consola: 'switch',
                valor: 35000
            },
            {
                consola: 'xbox',
                valor: 35000
            }]
        }
    },
    {
        nombre: 'sims 4',
        info: {
            tipo: 'simulacion',
            costos: [{
                consola: 'xbox',
                valor: 29000
            },
            {
                consola: 'ps5',
                valor: 31000
            },
            {
                consola: 'switch',
                valor: 28000
            }]
        }
    },
    {
        nombre: 'jurassic world evolution',
        info: {
            tipo: 'simulacion',
            modo: '1 jugador',
            costos: [{
                consola: 'ps5',
                valor: 23000
            },
            {
                consola: 'xbox',
                valor: 25000
            }]
        }
    }
])

// encontrar juego tipo aventura
db.juego.find({"info.tipo": "aventura"})

// encontrar juegos que tengan soporte para la consola ps5
db.juego.find({"info.costos.consola": "ps5"})

// juegos de xbox cuyos valores se encuentre entre 30000 y 45000
db.juego.find({"info.costos": {$elemMatch: {consola: "xbox", valor: {$gte: 30000, $lte: 45000}}}})

// muestre los juegos que tienen 2 consolas
db.juego.find({"info.costos": {$size: 2}})

// muestre los juegos donde la tercera consola sea switch
db.juego.find({"info.costos.2.consola": "switch"})