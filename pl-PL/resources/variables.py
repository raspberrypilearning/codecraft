#!/bin/python3

# zmienne gry, które można modyfikować!

# kolor tła gry
BACKGROUNDCOLOUR = 'white'

# zmienne mapy
MAXTILES  = 20
MAPWIDTH  = 10
MAPHEIGHT = 10

# zmienne reprezentujące różne zasoby
DIRT    = 0
GRASS   = 1
WATER   = 2
BRICK   = 3

# lista wszystkich zasobów gry
resources = [DIRT,GRASS,WATER,BRICK]

# nazwy zasobów
names = {
  DIRT    : 'dirt',
  GRASS   : 'grass',
  WATER   : 'water',
  BRICK   : 'brick'
}

# słownik łączący zasoby z obrazami
textures = {
  DIRT    : 'dirt.gif',
  GRASS   : 'grass.gif',
  WATER   : 'water.gif',
  BRICK   : 'brick.gif'
}

# ilość zasobów posiadanych przez gracza
inventory = {
  DIRT    : 10,
  GRASS   : 10,
  WATER   : 10,
  BRICK   : 0
}

# obrazek gracza
playerImg = 'player.gif'

#the player position.
playerX = 0
playerY = 0

# zasady  tworzenia nowych zasobów
crafting = {
  BRICK    : { WATER : 1, DIRT : 2 }
}

# klawisze do umieszczania zasobów
placekeys = {
  DIRT  : '1',
  GRASS : '2',
  WATER : '3',
  BRICK : '4'
}

# klawisze do tworzenia zasobów
craftkeys = {
  BRICK : 'r'
}

# wyświetlane instrukcje gry
instructions =  [
  'Instrukcje:',
  'Ruchy - WSAD'
]
