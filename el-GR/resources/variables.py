#!/bin/python3

#Μεταβλητές παιχνιδιού που μπορούν να αλλάξουν!

#χρώμα φόντου παιχνιδιού.
BACKGROUNDCOLOUR = 'white'

#μεταβλητές χάρτη.
MAXTILES  = 20
MAPWIDTH  = 10
MAPHEIGHT = 10

#μεταβλητές που απεικονίζουν τους διάφορους πόρους.
DIRT    = 0
GRASS   = 1
WATER   = 2
BRICK   = 3

#μία λίστα με όλους τους πόρους του παιχνιδιού.
resources = [DIRT,GRASS,WATER,BRICK]

# τα ονόματα των πόρων.
names = {
  DIRT    : 'λάσπη',
  GRASS   : 'γρασίδι',
  WATER   : 'νερό',
  BRICK   : 'τούβλο'
}

#ένα dictionary που αντιστοιχεί τους πόρους στις εικόνες.
textures = {
  DIRT    : 'dirt.gif',
  GRASS   : 'grass.gif',
  WATER   : 'water.gif',
  BRICK   : 'brick.gif'
}

#το πλήθος κάθε πόρου που έχει ο παίκτης.
inventory = {
  DIRT    : 10,
  GRASS   : 10,
  WATER   : 10,
  BRICK   : 0
}

#η εικόνα του παίκτη.
playerImg = 'player.gif'

# η θέση του παίκτη.
playerX = 0
playerY = 0

#κανόνες για να δημιουργήσεις νέους πόρους.
crafting = {
  BRICK    : { WATER : 1, DIRT : 2 }
}

#πλήκτρα για την τοποθέτηση πόρων.
placekeys = {
  DIRT  : '1',
  GRASS : '2',
  WATER : '3',
  BRICK : '4'
}

#πλήκτρα για τη δημιουργία πόρων.
craftkeys = {
  BRICK : 'r'
}

#οδηγίες παιχνιδιού που εμφανίζονται.
instructions =  [
  'Οδηγίες:',
  'Use WASD to move'
]
