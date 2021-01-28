#!/bin/python3

#¡Variables del juego que se puede cambiar!

#color del fondo del juego.
COLORDELFONDO = 'lightblue'

#variables del mapa.
MAXCASILLAS  = 40
ANCHOMAPA  = 20
ALTURAMAPA = 15

#variables que representan los diferentes recursos.
TIERRA    = 0
CESPED   = 1
AGUA   = 2
LADRILLO   = 3
MADERA    = 4
ARENA   = 5
TABLON  = 6
CRISTAL   = 7

#una lista de todos recursos del juego.
recursos = [TIERRA,CESPED,AGUA,LADRILLO,MADERA,ARENA,TABLON,CRISTAL]

#los nombres de los recursos.
nombres = {
  TIERRA    : 'tierra',
  CESPED   : 'césped',
  AGUA   : 'agua',
  LADRILLO   : 'ladrillo',
  MADERA    : 'madera',
  ARENA   : 'arena',
  TABLON   : 'tablón',
  CRISTAL   : 'cristal'
}

#un diccionario que conecta los recursos a las imágenes.
texturas = {
  TIERRA    : 'dirt.png',
  CESPED   : 'grass.png',
  AGUA   : 'water.png',
  LADRILLO   : 'brick.png',
  MADERA    : 'wood.png',
  ARENA    : 'sand.png',
  TABLON   : 'plank.png',
  CRISTAL   : 'glass.png'
}

#la cantidad de cada recurso que tiene el jugador.
inventario = {
  TIERRA    : 10,
  CESPED   : 10,
  AGUA   : 10,
  LADRILLO   : 0,
  MADERA    : 5,
  ARENA    : 5,
  TABLON   : 0,
  CRISTAL   : 0
}

#la imagen del jugador.
jugadorImg = 'player.png'

#la posición del jugador.
jugadorX = 0
jugadorY = 0

#las teclas para poner recursos.
teclasParaPoner = {
  TIERRA: '1',
  CESPED: '2',
  AGUA: '3',
  LADRILLO : '4',
  MADERA  : '5',
  ARENA  : '6',
  TABLON : '7',
  CRISTAL : '8'
}

#las reglas para crear nuevos recursos.
crafting = {
  LADRILLO    : { AGUA : 1, TIERRA : 2 },
  TABLON    : { MADERA : 3 },
  CRISTAL    : { ARENA : 3 }
}

#teclas para crear casillas.
teclasParaCrear = {
  LADRILLO : 'r',
  TABLON : 'u',
  CRISTAL : 'i'
}

#instrucciones del juego que se muestran.
instrucciones =  [
  'Instrucciones:',
  'Usa las teclas WASD para moverte'
]
