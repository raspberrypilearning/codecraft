#!/bin/python3

#गेम वेरिएबल्स जिन्हें बदला जा सकता है!

#गेम पृष्ठभूमि का रंग।
BACKGROUNDCOLOUR = 'white'

#मंच वेरिएबल।
MAXTILES  = 20
MAPWIDTH  = 10
MAPHEIGHT = 10

#विभिन्न संसाधनों का प्रतिनिधित्व करने वाले वेरिएबल।
DIRT    = 0
GRASS   = 1
WATER   = 2
BRICK   = 3

#सभी खेल संसाधनों की सूची।
resources = [DIRT,GRASS,WATER,BRICK]

#संसाधनों के नाम।
names = {
  DIRT    : 'dirt',
  GRASS   : 'grass',
  WATER   : 'water',
  BRICK   : 'brick'
}

#संसाधनों को चित्रों से जोड़ता हुआ एक शब्दकोश।
textures = {
  DIRT    : 'dirt.gif',
  GRASS   : 'grass.gif',
  WATER   : 'water.gif',
  BRICK   : 'brick.gif'
}

#खिलाड़ी के पास प्रत्येक संसाधन की संख्या।
inventory = {
  DIRT    : 10,
  GRASS   : 10,
  WATER   : 10,
  BRICK   : 0
}

#खिलाड़ी का चित्र।
playerImg = 'player.gif'

#खिलाड़ी की स्थिति।
playerX = 0
playerY = 0

#नियम नए संसाधन बनाने के लिए।
crafting = {
  BRICK    : { WATER : 1, DIRT : 2 }
}

#संसाधन रखने की कुंजियाँ।
placekeys = {
  DIRT  : '1',
  GRASS : '2',
  WATER : '3',
  BRICK : '4'
}

#टाइल बनाने की कुंजियाँ।
craftkeys = {
  BRICK : 'r'
}

#गेम निर्देश जो प्रदर्शित होते हैं।
instructions = [
  'Instructions:',
  'Use WASD to move'
]
