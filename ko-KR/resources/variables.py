#!/bin/python3

#게임에 사용되는 변수는 바꿀 수 있습니다.

#게임 배경 색깔
BACKGROUNDCOLOUR = 'white'

#map 변수
MAXTILES  = 20
MAPWIDTH  = 10
MAPHEIGHT = 10

#각 자원을 표현하는 변수들
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

#자원을 이미지에 연결해주는 딕셔너리
textures = {
  DIRT    : 'dirt.gif',
  GRASS   : 'grass.gif',
  WATER   : 'water.gif',
  BRICK   : 'brick.gif'
}

#플레이어가 가지고 있는 자원의 수
inventory = {
  DIRT    : 10,
  GRASS   : 10,
  WATER   : 10,
  BRICK   : 0
}

#플레이어 이미지
playerImg = 'player.gif'

#플레이어의 위치
playerX = 0
playerY = 0

#새로운 자원을 만드는 규칙
crafting = {
  BRICK    : { WATER : 1, DIRT : 2 }
}

#블럭 배치 단축키
placekeys = {
  DIRT  : '1',
  GRASS : '2',
  WATER : '3',
  BRICK : '4'
}

#제작 단축키
craftkeys = {
  BRICK : 'r'
}

#표시할 게임 방법
instructions =  [
  '플레이 방법:',
  'WASD로 조작'
]
