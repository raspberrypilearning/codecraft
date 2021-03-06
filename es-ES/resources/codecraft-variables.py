#!/bin/python3

#¡Variables del juego que se puede cambiar!

#color del fondo del juego.
COLORDELFONDO = 'white'

#variables del mapa.
MAXCASILLAS  = 20
ANCHURAMAPA  = 10
ALTURAMAPA = 10

#variables que representan los distintos recursos.
TIERRA    = 0
CESPED   = 1
AGUA   = 2
LADRILLO   = 3

#una lista de todos recursos del juego.
recursos = [TIERRA,CESPED,AGUA,LADRILLO]

#los nombres de los recursos.
nombres = {
  TIERRA    : 'tierra',
  CESPED   : 'césped',
  AGUA   : 'agua',
  LADRILLO   : 'ladrillo'
}

#un diccionario que vincula recursos a imágenes.
texturas = {
  TIERRA    : 'dirt.gif',
  CESPED   : 'grass.gif',
  AGUA   : 'water.gif',
  LADRILLO   : 'brick.gif'
}

#la cantidad de cada recurso que tiene el jugador.
inventario = {
  TIERRA    : 10,
  CESPED   : 10,
  AGUA   : 10,
  LADRILLO   : 0
}

#la imagen del jugador.
imgJugador = 'player.gif'

#la posición del jugador.
juagdorX = 0
jugadorY = 0

#las reglas para crear nuevos recursos.
crafting = {
  LADRILLO    : { AGUA : 1, TIERRA : 2 }
}

#las teclas para poner recursos.
teclasParaColocar = {
  TIERRA  : '1',
  CESPED : '2',
  AGUA : '3',
  LADRILLO : '4'
}

#las teclas para crear fichas.
teclasParaCrear = {
  LADRILLO : 'r'
}

#instrucciones del juego que se muestran.
instrucciones =  [
  'Instrucciones:',
  'Usa las teclas WASD para moverte'
]
