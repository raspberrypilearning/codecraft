#!/bin/python3

#Spelvariabelen die kunnen worden veranderd!

#spel achtergrondkleur.
ACHTERGRONDKLEUR = 'white'

#kaart variabelen.
MAXTEGELS = 20
KAARTBREEDTE = 10
KAARTHOOGTE = 10

#variabelen die de verschillende bronnen representeren.
VUIL = 0
GRAS   = 1
WATER   = 2
STEEN   = 3

#een lijst van alle spelbronnen.
bronnen = [VUIL,GRAS,WATER,STEEN]

#de namen van de bronnen.
namen = {
  VUIL : 'vuil',
  GRAS : 'gras',
  WATER : 'water',
  STEEN : 'steen'
}

# een woordenboek dat bronnen koppelt aan afbeeldingen.
materialen = {
  VUIL : 'dirt.png',
  GRAS : 'grass.png',
  WATER   : 'water.png',
  STEEN   : 'brick.png'
}

#het aantal bronnen dat een speler heeft.
inventaris = {
  VUIL : 10,
  GRAS   : 10,
  WATER   : 10,
  STEEN  : 0
}

#spelersafbeelding.
spelerImg = 'player.png'

#de positie van de speler.
spelerX = 0
spelerY = 0

#regels om nieuwe bronnen te maken.
maken = {
  STEEN : { WATER : 1, VUIL : 2 }
}

#toetsen om bronnen te plaatsen.
plaatstoetsen = {
  VUIL : '1',
  GRAS : '2',
  WATER : '3',
  STEEN : '4'
}

#toetsen om tegels te maken.
maaktoetsen= {
  STEEN : 'r',
}

#te tonen spelinstructies.
instructies = [
  'Instructies:',
  'Gebruik WASD om te bewegen'
]
