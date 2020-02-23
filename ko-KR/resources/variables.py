#!/bin/python3

#게임에 사용되는 변수는 바꿀 수 있습니다.

#게임 배경 색깔
BACKGROUNDCOLOUR = 'white'

#map 변수
MAXTILES  = 20
MAPWIDTH  = 10
MAPHEIGHT = 10

#자원들에 대한 분류 코드
DIRT    = 0
GRASS   = 1
WATER   = 2
BRICK   = 3

#게임에서 사용하는 모든 자원의 리스트
resources = [DIRT,GRASS,WATER,BRICK]

#자원의 이름
names = {
  DIRT    : '흙 블록',
  GRASS   : '초원 블록',
  WATER   : '물 블록',
  BRICK   : '벽돌 블록'
}

#a dictionary linking resources to images.
textures = {
  DIRT    : 'dirt.gif',
  GRASS   : 'grass.gif',
  WATER   : 'water.gif',
  BRICK   : 'brick.gif'
}

#the number of each resource the player has.
inventory = {
  DIRT    : 10,
  GRASS   : 10,
  WATER   : 10,
  BRICK   : 0
}

#the player image.
playerImg = 'player.gif'

#the player position.
playerX = 0
playerY = 0

#rules to make new resources.
crafting = {
  BRICK    : { WATER : 1, DIRT : 2 }
}

#keys for placing resources.
placekeys = {
  DIRT  : '1',
  GRASS : '2',
  WATER : '3',
  BRICK : '4'
}

#keys for crafting tiles.
craftkeys = {
  BRICK : 'r'
}

#표시되는 게임 방법
instructions =  [
  '플레이 방법:',
  'WASD로 조작'
]
