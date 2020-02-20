#!/bin/python3

#게임에 사용되는 변수는 변경될 수 있습니다.

#게임 배경 색깔
BACKGROUNDCOLOUR = 'lightblue'

#map 변수
MAXTILES  = 40
MAPWIDTH  = 20
MAPHEIGHT = 15

#자원들에 대한 분류 코드
DIRT    = 0
GRASS   = 1
WATER   = 2
BRICK   = 3
WOOD    = 4
SAND    = 5
PLANK   = 6
GLASS   = 7

#게임에 사용되는 자원 리스트
resources = [DIRT,GRASS,WATER,BRICK,WOOD,SAND,PLANK,GLASS]

#리소스의 이름
names = {
  DIRT    : '흙 블록',
  GRASS   : '초원 블록',
  WATER   : '물 블록',
  BRICK   : '벽돌 블록',
  WOOD    : '나무',
  SAND    : '모래',
  PLANK   : '나무판',
  GLASS   : '유리'
}

#이미지 이름을 담고 있는 딕셔너리
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

#플레이어가 가지고 시작하는 초기 아이템 수
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

#플레이어 이미지
playerImg = 'player.gif'

#플레이어의 위치
playerX = 0
playerY = 0

#블럭 배치 단축키
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

#새로운 조합법
crafting = {
  BRICK    : { WATER : 1, DIRT : 2 },
  PLANK    : { WOOD : 3 },
  GLASS    : { SAND : 3 }
}

#제작 단축키
craftkeys = {
  BRICK : 'r',
  PLANK : 'u',
  GLASS : 'i'
}

#게임 플레이 방법 표시
설명 =  [
  '플레이 방법:',
  'WASD로 조작'
]