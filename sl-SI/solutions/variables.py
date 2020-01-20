#!/bin/python3

#Game variables that can be changed!

#barva ozadja igre.
BARVAOZADJA = 'svetlo modra'

#spremenljivke mape.
MAKSIMALNOŠTEVILOPLOŠČ = 40
MAKSIMALNAŠIRINA = 20
VIŠINAMAPE = 15

#spremenljivke, ki predstavljajo različna sredstva.
ZEMLJA = 0
TRAVA     = 1
VODA = 2
OPEKA = 3
LES  = 4
PESEK = 5
DESKA = 6
STEKLO = 7

#seznam vseh sredstev v igri.
sredstva = [ZEMLJA,TRAVA,VODA,OPEKA,LES,PESEK,DESKA,STEKLO]

#imena sredstev.
imena = {
  ZEMLJA : 'zemlja',
  TRAVA : 'trava',
  VODA :'voda',
  OPEKA :'opeka',
  LES :'les',
  PESEK :'pesek',
  DESKA :'deska',
  STEKLO :'steklo',
}

#slovar, povezav sredstev s slikami.
teksture = {
  ZEMLJA : 'dirt.gif',
  TRAVA : 'dirt.gif',
  VODA  : 'water.gif',
  OPEKA  : 'brick.gif',
  LES  : 'wood.gif',
  PESEK : 'sand.gif',
  DESKA : 'plank.gif',
  STEKLO  : 'glass.gif'
}

#vsota sredstev, ki jih ima igralec v inventarju.
inventar = {
  ZEMLJA : 10,
  TRAVA : 10,
  VODA : 10,
  OPEKA : 0,
  LES      : 5,
  PESEK : 5,
  DESKA : 0,
  STEKLO : 0
}

#the player image.
playerImg = 'player.gif'

#the player position.
playerX = 0
playerY = 0

#keys for placing resources.
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

#rules to make new resources.
crafting = {
  BRICK    : { WATER : 1, DIRT : 2 },
  PLANK    : { WOOD : 3 },
  GLASS    : { SAND : 3 }
}

#keys for crafting tiles.
craftkeys = {
  BRICK : 'r',
  PLANK : 'u',
  GLASS : 'i'
}

#game instructions that are displayed.
navodila =  [
  'Navodila:',
  'Use WASD to move'
]
