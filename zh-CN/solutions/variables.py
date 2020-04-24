#!/bin/python3

＃游戏变量是可以更改的！

#游戏背景颜色。
BACKGROUNDCOLOUR = 'lightblue'

#地图变量。
MAXTILES  = 40
MAPWIDTH  = 20
MAPHEIGHT = 15

#代表不同资源的变量。
DIRT    = 0
GRASS   = 1
WATER   = 2
BRICK   = 3
WOOD    = 4
SAND    = 5
PLANK   = 6
GLASS   = 7

＃所有游戏资源的列表。
resources = [DIRT,GRASS,WATER,BRICK,WOOD,SAND,PLANK,GLASS]

＃资源名称。
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

#一个数据字典用来保存资源和图像的关联。
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

＃玩家拥有的每种资源的数量。
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

#玩家图像
playerImg = 'player.gif'

#玩家位置
playerX = 0
playerY = 0

＃用于放置资源的按键。
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

#用于创建新资源的规则。
crafting = {
  BRICK    : { WATER : 1, DIRT : 2 },
  PLANK    : { WOOD : 3 },
  GLASS    : { SAND : 3 }
}

#制作资源的按键。
craftkeys = {
  BRICK : 'r',
  PLANK : 'u',
  GLASS : 'i'
}

#游戏说明显示。
instructions =  [
  'Instructions:',
  使用W-A-S-D快捷键 移动。
]
