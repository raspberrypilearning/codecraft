#!/bin/python3

# متغيرات اللعبة التي يمكن تغييرها!

#لون خلفية اللعبة.
BACKGROUNDCOLOUR = 'lightblue'

#متغيرات الخريطة.
MAXTILES  = 40
MAPWIDTH  = 20
MAPHEIGHT = 15

# المتغيرات التي تُمثل الموارد المختلفة.
DIRT    = 0
GRASS   = 1
WATER   = 2
BRICK   = 3
WOOD    = 4
SAND    = 5
PLANK   = 6
GLASS   = 7

# قائمة بموارد اللعبة.
resources = [DIRT,GRASS,WATER,BRICK,WOOD,SAND,PLANK,GLASS]

#أسماء الموارد.
names = {
  DIRT    : 'طين',
  GRASS   : 'حشيش',
  WATER   : 'ماء',
  BRICK   : 'طابوق',
  WOOD    : 'خشب',
  SAND    : 'رمل',
  PLANK   : 'لوح',
  GLASS   : 'زجاج'
}

#قاموس يربط الموارد بالصور.
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

#رقم لكل مورد يملكه اللاعب.
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

# صورة اللاعب.
playerImg = 'player.gif'

# موقع اللاعب.
playerX = 0
playerY = 0

# مفاتيح لوضع الموارد.
placekeys = {
  DIRT  : '١',
  GRASS : '٢',
  WATER : '٣',
  BRICK : '٤',
  WOOD  : '5',
  SAND  : '6',
  PLANK : '7',
  GLASS : '8'
}

# قواعد لصنع موارد جديدة.
crafting = {
  BRICK    : { WATER : 1, DIRT : 2 },
  PLANK    : { WOOD : 3 },
  GLASS    : { SAND : 3 }
}

# مفاتيح لصياغة البلاط.
craftkeys = {
  BRICK : 'r',
  PLANK : 'u',
  GLASS : 'i'
}

# تعليمات اللعبة التي يتم عرضها.
instructions =  [
  'التعليمات:',
  'استخدم W-A-S-D للتحرك'
]
