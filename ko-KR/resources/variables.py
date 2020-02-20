#!/bin/python3

#게임에 사용되는 변수는 변경될 수 있습니다.

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

#게임에 사용되는 자원 리스트
resources = [DIRT,GRASS,WATER,BRICK]

#리소스의 이름
names = {
  DIRT    : '흙 블록',
  GRASS   : '초원 블록',
  WATER   : '물 블록',
  BRICK   : '벽돌 블록'
}

#이미지 이름을 담고 있는 딕셔너리
textures = {
  DIRT    : 'dirt.gif',
  GRASS   : 'grass.gif',
  WATER   : 'water.gif',
  BRICK   : 'brick.gif'
}

#플레이어가 가지고 시작하는 초기 아이템 수
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

#새로운 조합법
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

#게임 플레이 방법 표시
설명 =  [
  '플레이 방법:',
  'WASD로 조작'
]