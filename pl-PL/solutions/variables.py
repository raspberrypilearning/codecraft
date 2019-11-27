#!/bin/python3

# zmienne gry, które można modyfikować!

# kolor tła gry
BACKGROUNDCOLOUR = 'lightblue'

# zmienne mapy
MAXTILES  = 40
MAPWIDTH  = 20
MAPHEIGHT = 15

# zmienne reprezentujące różne zasoby
DIRT    = 0
GRASS   = 1
WATER   = 2
BRICK   = 3
WOOD    = 4
SAND    = 5
PLANK   = 6
GLASS   = 7

# lista wszystkich zasobów gry
resources = [DIRT,GRASS,WATER,BRICK,WOOD,SAND,PLANK,GLASS]

# nazwy zasobów
names = {
  DIRT    : 'dirt',
  GRASS   : 'grass',
  WATER   : 'water',
  BRICK   : 'brick',
  WOOD    : 'wood',
  SAND    : 'sand',
  PLANK   : 'plank',
  GLASS   : 'glass'
}

# słownik łączący zasoby z obrazami
textures = {
  DIRT    : 'dirt.gif',
  GRASS   : 'grass.gif',
  WATER   : 'water.gif',
  BRICK   : 'brick.gif',
  WOOD    : 'wood.gif',
  SAND    : 'sand.gif',
  PLANK   : 'plank.gif',
  GLASS   : 'glass.gif'
}

# ilość zasobów posiadanych przez gracza
inventory = {
  DIRT    : 10,
  GRASS   : 10,
  WATER   : 10,
  BRICK   : 0,
  WOOD    : 5,
  SAND    : 5,
  PLANK   : 0,
  GLASS   : 0
}

# obrazek gracza
playerImg = 'player.gif'

#the player position.
playerX = 0
playerY = 0

# klawisze do umieszczania zasobów
placekeys = {
  DIRT  : '1',
  GRASS : '2',
  WATER : '3',
  BRICK : '4',
  WOOD  : '5',
  SAND  : '6',
  PLANK : '7',
  GLASS : '8'
}

# zasady  tworzenia nowych zasobów
crafting = {
  BRICK    : { WATER : 1, DIRT : 2 },
  PLANK    : { WOOD : 3 },
  GLASS    : { SAND : 3 }
}

# klawisze do tworzenia zasobów
craftkeys = {
  BRICK : 'r',
  PLANK : 'u',
  GLASS : 'i'
}

# wyświetlane instrukcje gry
instructions =  [
  'Instrukcje:',
  'Ruchy - WSAD'
]
