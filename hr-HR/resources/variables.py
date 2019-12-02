#!/bin/python3

#Varijable u igri koje se mogu mijenjati!

#boja pozadine u igri.
BACKGROUNDCOLOUR = 'white'

#varijable mape.
MAXTILES  = 20
MAPWIDTH  = 10
MAPHEIGHT = 10

#varijable koje predstavljaju različite resurse.
DIRT    = 0
GRASS   = 1
WATER   = 2
BRICK   = 3

#popis svih resursa u igri.
resources = [DIRT,GRASS,WATER,BRICK]

#nazivi resursa.
names = {
  DIRT    : 'zemlja',
  GRASS   : 'trava',
  WATER   : 'voda',
  BRICK   : 'cigla'
}

#rječnik koji povezuje resurse sa slikama.
textures = {
  DIRT    : 'dirt.gif',
  GRASS   : 'grass.gif',
  WATER   : 'water.gif',
  BRICK   : 'brick.gif'
}

#broj svih resursa kojeg igrač posjeduje.
inventory = {
  DIRT    : 10,
  GRASS   : 10,
  WATER   : 10,
  BRICK   : 0
}

#slika igrača.
playerImg = 'player.gif'

#položaj igrača.
playerX = 0
playerY = 0

#pravila za stvaranje novih resursa.
crafting = {
  BRICK    : { WATER : 1, DIRT : 2 }
}

#tipke za postavljanje resursa.
placekeys = {
  DIRT  : '1',
  GRASS : '2',
  WATER : '3',
  BRICK : '4'
}

#tipke za stvaranje cigli.
craftkeys = {
  BRICK : 'r'
}

#upute igre koje su prikazane.
instructions =  [
  'Upute:',
  'Koristite WASD za kretanje'
]
