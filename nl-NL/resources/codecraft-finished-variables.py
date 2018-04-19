#!/bin/python3

#Spelvariabelen die kunnen worden veranderd!

#spel achtergrondkleur.
ACHTERGRONDKLEUR = 'lightblue'

#kaart variabelen.
MAXTEGELS = 40
MAPBREEDTE = 20
MAPHOOGTE = 15

#variabelen die de verschillende bronnen representeren.
VUIL = 0
GRAS   = 1
WATER   = 2
STEEN   = 3
HOUT = 4
ZAND = 5
PLANK = 6
GLAS = 7

#een lijst van alle spelbronnen.
bronnen = [VUIL, GRAS, WATER, BAKSTEEN, HOUT, ZAND, PLANK, GLAS]

#de namen van de bronnen.
namen = {
  VUIL : 'vuil',
  GRAS : 'gras',
  WATER : 'water',
  STEEN : 'steen',
  HOUT: 'hout',
  ZAND: 'zand',
  PLANK   : 'plank',
  GLAS: 'glas'
}

# een woordenboek dat bronnen koppelt aan afbeeldingen.
materialen = {
  VUIL : 'dirt.gif',
  GRAS : 'grass.gif',
  WATER   : 'water.gif',
  STEEN   : 'brick.gif',
  HOUT: 'wood.gif',
  ZAND    : 'sand.gif',
  PLANK   : 'plank.gif',
  GLAS   : 'glass.gif'
}

#het aantal bronnen dat een speler heeft.
inventaris = {
  VUIL : 10,
  GRAS   : 10,
  WATER   : 10,
  STEEN  : 0,
  HOUT : 5,
  ZAND    : 5,
  PLANK   : 0,
  GLAS   : 0
}

#spelersafbeelding.
spelerImg = 'player.gif'

#de positie van de speler.
spelerX = 0
spelerY = 0

#toetsen om bronnen te plaatsen.
plaatstoetsen = {
  VUIL : '1',
  GRAS : '2',
  WATER : '3',
  STEEN : '4',
  HOUT  : '5,',
  ZAND  : '6',
  PLANK : '7',
  GLAS : '8'
}

#regels om nieuwe bronnen te maken.
maken = {
  STEEN : { WATER : 1, VUIL : 2 },
  PLANK: { HOUT : 3 },
  GLAS    : { ZAND : 3 }
}

#toetsen om tegels te maken.
maaktoetsen= {
  STEEN : 'r',
  PLANK : 'u',
  GLAS : 'i'
}

#te tonen spelinstructies.
instructies = [
  'Instructies:',
  'Gebruik WASD om te bewegen'
]
