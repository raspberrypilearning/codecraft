#!/bin/python3

#गेम वेरिएबल्स जिन्हें बदला जा सकता है!

#गेम पृष्ठभूमि का रंग।
BACKGROUNDCOLOUR = 'lightblue'

#मंच वेरिएबल।
MAXTILES  = 40
MAPWIDTH  = 20
MAPHEIGHT = 15

#विभिन्न संसाधनों का प्रतिनिधित्व करने वाले वेरिएबल।
DIRT    = 0
GRASS   = 1
WATER   = 2
BRICK   = 3
WOOD    = 4
SAND    = 5
PLANK   = 6
GLASS   = 7

#सभी खेल संसाधनों की सूची।
resources = [DIRT,GRASS,WATER,BRICK,WOOD,SAND,PLANK,GLASS]

#संसाधनों के नाम।
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

#संसाधनों को चित्रों से जोड़ता हुआ एक शब्दकोश।
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

#खिलाड़ी के पास प्रत्येक संसाधन की संख्या।
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

#खिलाड़ी का चित्र।
playerImg = 'player.gif'

#खिलाड़ी की स्थिति।
playerX = 0
playerY = 0

#संसाधन रखने की कुंजियाँ।
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

#नियम नए संसाधन बनाने के लिए।
crafting = {
  BRICK    : { WATER : 1, DIRT : 2 },
  PLANK    : { WOOD : 3 },
  GLASS    : { SAND : 3 }
}

#टाइल बनाने की कुंजियाँ।
craftkeys = {
  BRICK : 'r',
  PLANK : 'u',
  GLASS : 'i'
}

#गेम निर्देश जो प्रदर्शित होते हैं।
instructions = [
  'Instructions:',
  'Use WASD to move'
]
