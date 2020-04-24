#!/bin/python3

＃可以更改的游戏变量！

#游戏背景颜色。
BACKGROUNDCOLOUR = 'white'

#地图变量。
MAXTILES  = 20
MAPWIDTH  = 10
MAPHEIGHT = 10

#代表不同资源的变量。
DIRT    = 0
GRASS   = 1
WATER   = 2
BRICK   = 3

＃所有游戏资源的列表。
resources = [DIRT,GRASS,WATER,BRICK]

＃资源名称。
names = {
  DIRT    : 'dirt',
  GRASS   : 'grass',
  WATER   : 'water',
  BRICK   : 'brick'
}

#将资源链接到图像的数据字典。
textures = {
  DIRT    : 'dirt.gif',
  GRASS   : 'grass.gif',
  WATER   : 'water.gif',
  BRICK   : 'brick.gif'
}

＃玩家拥有的每种资源的数量。
inventory = {
  DIRT    : 10,
  GRASS   : 10,
  WATER   : 10,
  BRICK   : 0
}

#玩家图像
playerImg = 'player.gif'

#玩家位置
playerX = 0
playerY = 0

#用于创建新资源的规则。
crafting = {
  BRICK    : { WATER : 1, DIRT : 2 }
}

＃用于放置资源的键。
placekeys = {
  DIRT  : '1',
  GRASS : '2',
  WATER : '3',
  BRICK : '4'
}

#制作图块的 key
craftkeys = {
  BRICK : 'r'
}

#游戏说明显示。
instructions =  [
  'Instructions:',
  使用W-A-S-D快捷键 移动。
]
