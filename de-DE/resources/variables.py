#!/bin/python3

#Variablen des Spiels, die geändert werden können!

#Hintergrundfarbe des Spiels.
HINTERGRUNDFARBE = 'white'

#Variablen für die Welt.
MAXELEMENTE = 20
WELTBREITE = 10
WELTHOEHE = 10

#Diese Variablen stellen die verschiedenen Ressourcen dar.
ERDE = 0
GRAS   = 1
WASSER = 2
ZIEGEL = 3

#Eine Liste mit allen Ressourcen des Spiels.
ressourcen = [ERDE, GRASS, WASSER, ZIEGEL]

#Die namen der Ressourcen.
namen = {
  ERDE : 'Erde',
  GRAS   : 'Gras',
  WASSER : 'Wasser',
  ZIEGEL: 'Ziegel'
}

#Ein Dictionary (Wörterbuch) verknüpft Ressourcen und Bilder.
texturen = {
  ERDE : 'dirt.gif',
  GRAS : 'grass.gif',
  WASSER : 'water.gif',
  ZIEGEL: 'brick.gif'
}

#Ressourcen des Spielers bei Spielstart.
inventar = {
  ERDE : 10,
  GRAS : 10,
  WASSER : 10,
  ZIEGEL: 0,
}

#Das Spielerbild.
spielerBild = 'player.gif'

#Spielerposition.
spielerX = 0
spielerY = 0

#Regeln zur Herstellung neuer Ressourcen.
herstellenMit = {
  ZIEGEL    : { WASSER : 1, ERDE : 2 }
}

#Tasten zum Ablegen von Ressourcen.
tastenZumAblegen = {
  ERDE : '1',
  GRAS : '2',
  WASSER : '3',
  ZIEGEL: '4'
}

#Tasten für die Herstellung von Elementen einer Ressource.
tastenZumHerstellen = {
  ZIEGEL : 'z'
}

#Spielanleitung zum Anzeigen.
anleitungen = [
  'Anleitungen:',
  'Bewege dich mit den Tasten WASD'
]
