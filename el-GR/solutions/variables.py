#!/bin/python3

#Μεταβλητές παιχνιδιού που μπορούν να αλλάξουν!

#χρώμα φόντου παιχνιδιού.
BACKGROUNDCOLOUR = 'lightblue'

#μεταβλητές χάρτη.
MAXTILES  = 40
MAPWIDTH  = 20
MAPHEIGHT = 15

#μεταβλητές που απεικονίζουν τους διάφορους πόρους.
DIRT    = 0
GRASS   = 1
WATER   = 2
BRICK   = 3
WOOD    = 4
SAND    = 5
PLANK   = 6
GLASS   = 7

#μία λίστα με όλους τους πόρους του παιχνιδιού.
resources = [DIRT,GRASS,WATER,BRICK,WOOD,SAND,PLANK,GLASS]

# τα ονόματα των πόρων.
names = {
  DIRT    : 'λάσπη',
  GRASS   : 'γρασίδι',
  WATER   : 'νερό',
  BRICK   : 'τούβλο',
  WOOD    : 'ξύλο',
  SAND    : 'άμμος',
  PLANK   : 'σανίδα',
  GLASS   : 'γυαλί'
}

#ένα dictionary που αντιστοιχεί τους πόρους στις εικόνες.
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

#το πλήθος κάθε πόρου που έχει ο παίκτης.
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

#η εικόνα του παίκτη.
playerImg = 'player.gif'

# η θέση του παίκτη.
playerX = 0
playerY = 0

#πλήκτρα για την τοποθέτηση πόρων.
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

#κανόνες για να δημιουργήσεις νέους πόρους.
crafting = {
  BRICK    : { WATER : 1, DIRT : 2 },
  PLANK    : { WOOD : 3 },
  GLASS    : { SAND : 3 }
}

#πλήκτρα για τη δημιουργία πόρων.
craftkeys = {
  BRICK : 'r',
  PLANK : 'u',
  GLASS : 'i'
}

#οδηγίες παιχνιδιού που εμφανίζονται.
instructions =  [
  'Οδηγίες:',
  'Use WASD to move'
]
