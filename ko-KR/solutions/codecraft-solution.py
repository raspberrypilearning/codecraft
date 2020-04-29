#!/bin/python3

#############
# 코드크래프트 #
#############

#---
#게임 함수
#---

#플레이어가 왼쪽으로 1칸 이동
def moveLeft():
  global playerX
  if(drawing == False and playerX > 0):
    oldX = playerX
    playerX -= 1
    drawResource(oldX, playerY)
    drawResource(playerX, playerY)
    
#플레이어가 오른쪽으로 1칸 이동
def moveRight():
  global playerX, MAPWIDTH
  if(drawing == False and playerX < MAPWIDTH - 1):
    oldX = playerX
    playerX += 1
    drawResource(oldX, playerY)
    drawResource(playerX, playerY)
    
#플레이어가 위쪽으로 1칸 이동
def moveUp():
  global playerY
  if(drawing == False and playerY > 0):
    oldY = playerY
    playerY -= 1
    drawResource(playerX, oldY)
    drawResource(playerX, playerY)
    
#플레이어가 아래쪽으로 1칸 이동
def moveDown():
  global playerY, MAPHEIGHT
  if(drawing == False and playerY < MAPHEIGHT - 1):
    oldY = playerY
    playerY += 1
    drawResource(playerX, oldY)
    drawResource(playerX, playerY)
    
#플레이어의 위치에서 아이템을 줍는 코드
def pickUp():
  global playerX, playerY
  drawing = True
  currentTile = world[playerX][playerY]
  #만약 플레이어가 이미 너무 많은 자원을 지니고 있지 않다면...
  if inventory[currentTile] < MAXTILES:
    #플레이어는 이제 자원을 1개 더 얻음
    inventory[currentTile] += 1
    #플레이어가 흙 위에 서 있도록 함
    world[playerX][playerY] = DIRT
    #새로운 흙 타일 그리기
    drawResource(playerX, playerY)
    #인벤토리 업데이트
    drawInventory()
    #drawPlayer()

#플레이어의 위치에 자원을 배치
def place(resource):
  print('배치 중: ', names[resource])
  #이 위치에 플레이어에게 남은 자원이 있다면...
  if inventory[resource] > 0:
    #플레이어의 위치에 배치된 자원 탐색
    currentTile = world[playerX][playerY]
    #플레이어의 위치에서 자원을 줍는 코드
    #(만약 흙이 아닌 경우)
    if currentTile is not DIRT:
      inventory[currentTile] += 1
    #플레이어의 위치에 자원을 배치
    world[playerX][playerY] = resource
    #새 자원을 인벤토리에 추가
    inventory[resource] -= 1
    #디스플레이 업데이트(월드 및 인벤토리)
    drawResource(playerX, playerY)
    drawInventory()
    #drawPlayer()
    print(names[resource], ' 제작 완료')
  #...그리고 남은 것이 하나도 없다면...
  else:
    print('당신은', names[resource], ' 자원을 가지고 있지 않습니다.')

#새로운 자원 제작
def craft(resource):
  print('제작 중: ', names[resource])
  #만약 만들 수 있는 자원이라면
  if resource in crafting:
    #자원이 있는지의 여부를 계속 추적
    #이 아이템을 제작하기 위해
    canBeMade = True
    #자원을 만드는 데 필요한 각 항목의 수
    for i in crafting[resource]:
      #만약 충분하지 못하다면
      if crafting[resource][i] > inventory[i]:
      #만들 수 없습니다!
        canBeMade = False
        break
    #만약 만들 수 있다면 (우리가 필요한 자원을 모두 가지고 있는 경우)
    if canBeMade == True:
      #각 자원을 인벤토리에서 빼냄
      for i in crafting[resource]:
        inventory[i] -= crafting[resource][i]
      #새 자원을 인벤토리에 추가
      inventory[resource] += 1
      print(names[resource], ' 설치 완료')
    #만약 만들 수 없는 자원이라면
    else:
      print(names[resource], ' 을(를) 제작 할 수 없습니다.')
    #디스플레이 업데이트(월드 및 인벤토리)
    drawInventory()

#각 자원을 배치하기 위한 함수 만들기
def makeplace(resource):
  return lambda: place(resource)

#각 키에 해당하는 함수를 연결
def bindPlacingKeys():
  for k in placekeys:
    screen.onkey(makeplace(k), placekeys[k])

#각 자원을 제작하기 위한 함수
def makecraft(resource):
  return lambda: craft(resource)

#제작 함수를 각 키 누름에 연결ㅁ
def bindCraftingKeys():
  for k in craftkeys:
    screen.onkey(makecraft(k), craftkeys[k])

#(y,x) 포지션에 자원 그리기
def drawResource(y, x):
  #이 변수는 다른 물건이 그려지는 것을 방지함
  global drawing
  #만약 다른 물건이 그려지는 중이 아니라면
  if drawing == False:
    #그려지고 있다는 플래그를 True로 설정
    drawing = True
    #적절한 이미지를 사용하여 타일 맵에 자원을 그림
    rendererT.goto( (y * TILESIZE) + 20, height - (x * TILESIZE) - 20 )
    #올바른 텍스쳐로 타일을 그림
    texture = textures[world[y][x]]
    rendererT.shape(texture)
    rendererT.stamp()
    if playerX == y and playerY == x:
      rendererT.shape(playerImg)
      rendererT.stamp()
    screen.update()
    #그리는 중인 것이 없음
    drawing = False
    
#월드 맵을 그림
def drawWorld():
  #각 행을 반복
  for row in range(MAPHEIGHT):
    #해당 행의 각 열을 반복
    for column in range(MAPWIDTH):
      #현재 위치에서 타일을 그리기
      drawResource(column, row)

#인벤토리를 화면에 표시
def drawInventory():
  #이 변수는 다른 물건이 그려지는 것을 방지함
  global drawing
  #다른 곳에서 그려지지 않을 때만 그림
  if drawing == False:
    #그려지고 있다는 플래그를 True로 설정
    drawing = True
    # 사각형을 이용하여 현재 인벤토리를 덮음
    rendererT.color(BACKGROUNDCOLOUR)
    rendererT.goto(0,0)
    rendererT.begin_fill()
    #rendererT.setheading(0)
    for i in range(2):
      rendererT.forward(inventory_height - 60)
      rendererT.right(90)
      rendererT.forward(width)
      rendererT.right(90)
    rendererT.end_fill()
    rendererT.color('black')
    #'설치' 및 '제작' 문자열 표시
    for i in range(1,num_rows+1):
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 20 - (i * 100))
      rendererT.write("설치")
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 40 - (i * 100))
      rendererT.write("제작")
    #인벤토리 위치 설정
    xPosition = 70
    yPostition = height - (MAPHEIGHT * TILESIZE) - 80
    itemNum = 0
    for i, item in enumerate(resources):
      #이미지 추가
      rendererT.goto(xPosition, yPostition)
      rendererT.shape(textures[item])
      rendererT.stamp()
      #숫자를 인벤토리에 추가
      rendererT.goto(xPosition, yPostition - TILESIZE)
      rendererT.write(inventory[item])
      #배치 키 추가
      rendererT.goto(xPosition, yPostition - TILESIZE - 20)
      rendererT.write(placekeys[item])
      #제작키 추가
      if crafting.get(item) != None:
        rendererT.goto(xPosition, yPostition - TILESIZE - 40)
        rendererT.write(craftkeys[item])     
      #다음 인벤토리 아이템 배치
      xPosition += 50
      itemNum += 1
      #10개 항목마다 다음 행
      if itemNum % INVWIDTH == 0:
        xPosition = 70
        itemNum = 0
        yPostition -= TILESIZE + 80
    drawing = False

#게임 플레이 방법과 가공 규칙을 생성
def generateInstructions():
  instructions.append('가공 규칙:')
  #만들 수 있는 각 자원 마다 반복
  for rule in crafting:
    #가공 규칙 문자열 작성
    craftrule = names[rule] + ' = '
    for resource, number in crafting[rule].items():
      craftrule += str(number) + ' ' + names[resource] + ' '
    #게임 방법에 가공 규칙 추가
    instructions.append(craftrule)
  #규칙을 표시
  yPos = height - 20
  for item in instructions:
    rendererT.goto( MAPWIDTH*TILESIZE + 40, yPos)
    rendererT.write(item)
    yPos-=20

#임의로 블럭 배치
def generateRandomWorld():
  #각 행을 반복
  for row in range(MAPHEIGHT):
    #해당 행의 각 열을 반복
    for column in range(MAPWIDTH):
      #0부터 10까지의 임의의 숫자를 뽑음
      randomNumber = random.randint(0,10)
      #1 또는 2일 경우 물
      if randomNumber in [1,2]:
        tile = WATER
      #3 또는 4일 경우 초원
      elif randomNumber in [3,4]:
        tile = GRASS
      #5일 경우 나무
      elif randomNumber == 5:
        tile = WOOD
      #6일 경우 모래
      elif randomNumber == 6:
        tile = SAND
      #이외는 흙
      else:
        tile = DIRT
      #무작위로 선정된 타일로 타일 맵의 위치 선정
      world[column][row] = tile

#---
#코드는 여기서부터 실행됨!
#---

#필요한 모듈과 변수 가져오기
import turtle
import random
from variables import *
from math import ceil

TILESIZE = 20
#행당 인벤토리 자원의 갯수
INVWIDTH = 8
drawing = False

#'screen' 오브젝트 생성
screen = turtle.Screen()
#너비와 높이 계산
width = (TILESIZE * MAPWIDTH) + max(200,INVWIDTH * 50)
num_rows = int(ceil((len(resources) / INVWIDTH)))
inventory_height =  num_rows * 120 + 40
height = (TILESIZE * MAPHEIGHT) + inventory_height

screen.setup(width, height)
screen.setworldcoordinates(0,0,width,height)
screen.bgcolor(BACKGROUNDCOLOUR)
screen.listen()

#플레이어 이미지 등록  
screen.register_shape(playerImg)
#각 자원의 이미지 등록
for texture in textures.values():
  screen.register_shape(texture)

#그래픽을 그리기 위해 다른 Turtle 생성
rendererT = turtle.Turtle()
rendererT.hideturtle()
rendererT.penup()
rendererT.speed(0)
rendererT.setheading(90)

#무작위로 월드에 자원 배치
world = [ [DIRT for w in range(MAPHEIGHT)] for h in range(MAPWIDTH) ]

#옮기고 집기 위한 키를 적절한 함수와 연결
screen.onkey(moveUp, 'w')
screen.onkey(moveDown, 's')
screen.onkey(moveLeft, 'a')
screen.onkey(moveRight, 'd')
screen.onkey(pickUp, 'space')

#자원 배치 및 제작을 위한 키 설정
bindPlacingKeys()
bindCraftingKeys()

#이 함수들은 위에서 정의 됨.
generateRandomWorld()
drawWorld()
drawInventory()
generateInstructions()


