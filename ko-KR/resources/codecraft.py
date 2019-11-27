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
  #만약 플레이어가 너무 많이 아이템을 소지하지 않은 경우...
  if inventory[currentTile] < MAXTILES:
    #플레이어에게 자원 +1
    inventory[currentTile] += 1
    #플레이어가 흙 위에 서있는 것으로 변경
    world[playerX][playerY] = DIRT
    #새로운 흙 아이템 그리기
    drawResource(playerX, playerY)
    #인벤토리 업데이트
    drawInventory()
    #drawPlayer()

#플레이어의 위치에 아이템을 배치
def place(resource):
  print('제작 중: ', names[resource])
  #플레어어가 아이템이 조금이라도 남은 경우...
  if inventory[resource] > 0:
    #플레이어의 위치에 배치된 아이템 검색
    currentTile = world[playerX][playerY]
    #플레이어의 위치에서 아이템을 줍는 코드
    #(만약 흙이 아닌 경우)
    if currentTile is not DIRT:
      inventory[currentTile] += 1
    #플레이어의 위치에 아이템을 배치
    world[playerX][playerY] = resource
    #새 자원을 인벤토리에 추가
    inventory[resource] -= 1
    #디스플레이 업데이트(월드 및 인벤토리)
    drawResource(playerX, playerY)
    drawInventory()
    #drawPlayer()
    print(names[resource], ' 설치 완료')
  #만약 남지 않은 경우...
  else:
    print(names[resource], ' 자원이 없습니다!')

#새로운 아이템 생성
def craft(resource):
  print('조합 중: ', names[resource])
  #만약 만들 수 있는 아이템이라면
  if resource in crafting:
    #리소스가 있는지의 여부를 추적
    #아이템을 만들 수 있는지 알기 위해
    canBeMade = True
    #자원을 만드는 데 필요한 각 항목의 수
    for i in crafting[resource]:
      #만약 충분하지 못하다면
      if crafting[resource][i] > inventory[i]:
      #만들 수 없습니다!
        canBeMade = False
        break
    #만약 만들 수 있다면
    if canBeMade == True:
      #각 아이템을 인벤토리에서 빼냄
      for i in crafting[resource]:
        inventory[i] -= crafting[resource][i]
      #새 자원을 인벤토리에 추가
      inventory[resource] += 1
      print(names[resource], ' 설치 완료')
    #만약 만들 수 없는 아이템이라면
    else:
      print(names[resource], ' 를 만들 수 없습니다!')
    #디스플레이 업데이트(월드 및 인벤토리)
    drawInventory()

#각 리소스를 배치하기위한 함수
def makeplace(resource):
  return lambda: place(resource)

#키 누름 함수
def bindPlacingKeys():
  for k in placekeys:
    screen.onkey(makeplace(k), placekeys[k])

#각 리소스를 제작하기 위한 함수
def makecraft(resource):
  return lambda: craft(resource)

#제작 키 누름 함수
def bindCraftingKeys():
  for k in craftkeys:
    screen.onkey(makecraft(k), craftkeys[k])

#(y,x) 포지션에 아이템 설치
def drawResource(y, x):
  #다른 곳에서 작동 중인 함수를 멈춤
  global drawing
  #만약 다른 곳에서 그리고 있지 않다면
  if drawing == False:
    #그려지고 있다는 플래그를 True로 설정
    drawing = True
    #올바른 리소스를 사용하여 타일 맵에 이미지를 배치함
    rendererT.goto( (y * TILESIZE) + 20, height - (x * TILESIZE) - 20 )
    #올바른 텍스쳐 사용
    texture = textures[world[y][x]]
    rendererT.shape(texture)
    rendererT.stamp()
    if playerX == y and playerY == x:
      rendererT.shape(playerImg)
      rendererT.stamp()
    screen.update()
    #그려지고 있다는 플래그를 False로 설정
    drawing = False
    
#월드 내 맵을 그리는 함수
def drawWorld():
  #각 행을 반복
  for row in range(MAPHEIGHT):
    #해당 행의 각 열을 반복
    for column in range(MAPWIDTH):
      #현재 위치에서 타일을 그리기
      drawResource(column, row)

#인벤토리를 화면에 표시
def drawInventory():
  #다른 곳에서 작동 중인 함수를 멈춤
  global drawing
  #만약 다른 곳에서 그리고 있지 않다면
  if drawing == False:
    #그려지고 있다는 플래그를 True로 설정
    drawing = True
    # 배경 색상 설정
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
    #'설치 단축키' 및 '조합 단축키' 텍스트 표시
    for i in range(1,num_rows+1):
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 20 - (i * 100))
      rendererT.write("설치 단축키")
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 40 - (i * 100))
      rendererT.write("조합 단축키")
    #인벤토리 포지션 설정
    xPosition = 70
    yPostition = height - (MAPHEIGHT * TILESIZE) - 80
    itemNum = 0
    for i, item in enumerate(resources):
      #이미지 추가
      rendererT.goto(xPosition, yPostition)
      rendererT.shape(textures[item])
      rendererT.stamp()
      #새롭게 카운트를 인벤토리에 추가
      rendererT.goto(xPosition, yPostition - TILESIZE)
      rendererT.write(inventory[item])
      #설치 단축키
      rendererT.goto(xPosition, yPostition - TILESIZE - 20)
      rendererT.write(placekeys[item])
      #조합 단축키
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

#게임 플레이 방법, 조합법
def generateInstructions():
  instructions.append('제작 방법:')
  #만들 수 있는 아이템만큼 반복
  for rule in crafting:
    #조합 규칙 텍스트 작성
    craftrule = names[rule] + ' = '
    for resource, number in crafting[rule].items():
      craftrule += str(number) + ' ' + names[resource] + ' '
    #조합법 추가
    instructions.append(craftrule)
  #조합법 표시
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
#행당 인벤토리 리소스 수
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
#각 아이템 이미지 등록
for texture in textures.values():
  screen.register_shape(texture)

#Turtle 생성
rendererT = turtle.Turtle()
rendererT.hideturtle()
rendererT.penup()
rendererT.speed(0)
rendererT.setheading(90)

#무작위로 월드에 자원 배치
world = [ [DIRT for w in range(MAPHEIGHT)] for h in range(MAPWIDTH) ]

#단축키
screen.onkey(moveUp, 'w')
screen.onkey(moveDown, 's')
screen.onkey(moveLeft, 'a')
screen.onkey(moveRight, 'd')
screen.onkey(pickUp, 'space')

#자원 배치 및 제작을 위한 키 설정
bindPlacingKeys()
bindCraftingKeys()

#함수 불러오기
generateRandomWorld()
drawWorld()
drawInventory()
generateInstructions()


