#!/bin/python3

#Variablen des Spiels, die geändert werden können!

#Hintergrundfarbe des Spiels.
HINTERGRUNDFARBE = 'lightblue'

#Variablen für die Welt.
MAXELEMENTE = 40
WELTBREITE = 20
WELTHOEHE = 15

#Diese Variablen stellen die verschiedenen Ressourcen dar.
ERDE = 0
GRAS = 1
WASSER = 2
ZIEGEL = 3
HOLZ = 4
SAND = 5
BRETT = 6
GLAS = 7

#Eine Liste mit allen Ressourcen des Spiels.
ressourcen = [ERDE,GRAS,WASSER,ZIEGEL,HOLZ,SAND,BRETT,GLAS]

#Die namen der Ressourcen.
namen = {
ERDE : 'Erde',
GRAS : 'Gras',
WASSER : 'Wasser',
ZIEGEL : 'Ziegel',
HOLZ : 'Holz',
SAND : 'Sand',
BRETT : 'Brett',
GLAS : 'Glas'
}

#Ein Dictionary (Wörterbuch) verknüpft Ressourcen und Bilder.
texturen = {
ERDE : 'dirt.gif',
GRAS : 'grass.gif',
WASSER : 'water.gif',
ZIEGEL: 'brick.gif',
HOLZ : 'wood.gif',
SAND : 'sand.gif',
BRETT : 'plank.gif',
GLAS : 'glass.gif'
}

#Ressourcen des Spielers bei Spielstart.
inventar = {
ERDE : 10,
GRAS : 10,
WASSER : 10,
ZIEGEL : 0,
HOLZ : 5,
SAND : 5,
BRETT : 0,
GLAS : 0
}

#Das Spielerbild.
spielerBild = 'player.gif'

#Spielerposition.
spielerX = 0
spielerY = 0

#Tasten zum Ablegen von Ressourcen.
tastenZumAblegen = {
ERDE : '1',
GRAS : '2',
WASSER : '3',
ZIEGEL : '4',
HOLZ : '5',
SAND : '6',
BRETT : '7',
GLAS : '8'
}

#Regeln zur Herstellung neuer Ressourcen.
herstellenMit = {
ZIEGEL : { WASSER : 1, ERDE : 2 },
BRETT : { HOLZ : 3 },
GLAS : { SAND : 3 }
}

#Tasten für die Herstellung von Elementen einer Ressource.
tastenZumHerstellen = {
ZIEGEL : 'z',
BRETT : 'b',
GLAS : 'g'
}

#Spielanleitung zum Anzeigen.
anleitungen = [
'Anleitungen:',
'Bewege dich mit den Tasten WASD'
]