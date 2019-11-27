#!/bin/python3

# متغيرات اللعبة التي يمكن تغييرها!

#لون خلفية اللعبة.
BACKGROUNDCOLOUR = 'white'

#متغيرات الخريطة.
MAXTILES  = 20
MAPWIDTH  = 10
MAPHEIGHT = 10

# المتغيرات التي تُمثل الموارد المختلفة.
DIRT    = 0
GRASS   = 1
WATER   = 2
BRICK   = 3

# قائمة بموارد اللعبة.
resources = [DIRT,GRASS,WATER,BRICK]

#أسماء الموارد.
names = {
  DIRT    : 'طين',
  GRASS   : 'حشيش',
  WATER   : 'ماء',
  BRICK   : 'طابوق'
}

#قاموس يربط الموارد بالصور.
textures = {
  DIRT    : 'dirt.gif',
  GRASS   : 'grass.gif',
  WATER   : 'water.gif',
  BRICK   : 'brick.gif'
}

#رقم لكل مورد يملكه اللاعب.
inventory = {
  DIRT    : 10,
  GRASS   : 10,
  WATER   : 10,
  BRICK   : 0
}

# صورة اللاعب.
playerImg = 'player.gif'

# موقع اللاعب.
playerX = 0
playerY = 0

# قواعد لصنع موارد جديدة.
crafting = {
  BRICK    : { WATER : 1, DIRT : 2 }
}

# مفاتيح لوضع الموارد.
placekeys = {
  DIRT  : '١',
  GRASS : '٢',
  WATER : '٣',
  BRICK : '٤'
}

# مفاتيح لصياغة البلاط.
craftkeys = {
  BRICK : 'r'
}

# تعليمات اللعبة التي يتم عرضها.
instructions =  [
  'التعليمات:',
  'استخدم W-A-S-D للتحرك'
]
