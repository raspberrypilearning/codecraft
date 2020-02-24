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

#플레이어의 위치에 아이템을 배치
def place(resource):
  print('제작 중: ', names[resource])
  #이 위치에 플레이어에게 남은 자원이 있다면...
  if inventory[resource] > 0:
    #플레이어의 위치에 배치된 자원 탐색
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
      #각 아이템을 인벤토리에서 빼냄
      for i in crafting[resource]:
        inventory[i] -= crafting[resource][i]
      #새 자원을 인벤토리에 추가
      inventory[resource] += 1
      print(names[resource], ' 설치 완료')
    #만약 만들 수 없는 자원이라면
    else:
      print(names[resource], ' 를 만들 수 없습니다!')
    #디스플레이 업데이트(월드 및 인벤토리)
    drawInventory()

#각 자원을 배치하기 위한 함수 만들기
def makeplace(resource):
  return lambda: place(resource)

#attaches a 'placing' function to each key press
def bindPlacingKeys():
  for k in placekeys:
    screen.onkey(makeplace(k), placekeys[k])

#creates a function for crafting each resource
def makecraft(resource):
  return lambda: craft(resource)

#attaches a 'crafting' function to each key press
def bindCraftingKeys():
  for k in craftkeys:
    screen.onkey(makecraft(k), craftkeys[k])

#draws a resource at the position (y,x)
def drawResource(y, x):
  #this variable stops other stuff being drawn
  global drawing
  #only draw if nothing else is being drawn
  if drawing == False:
    #something is now being drawn
    drawing = True
    #draw the resource at that position in the tilemap, using the correct image
    rendererT.goto( (y * TILESIZE) + 20, height - (x * TILESIZE) - 20 )
    #draw tile with correct texture
    texture = textures[world[y][x]]
    rendererT.shape(texture)
    rendererT.stamp()
    if playerX == y and playerY == x:
      rendererT.shape(playerImg)
      rendererT.stamp()
    screen.update()
    #nothing is now being drawn
    drawing = False
    
#draws the world map
def drawWorld():
  #loop through each row
  for row in range(MAPHEIGHT):
    #loop through each column in the row
    for column in range(MAPWIDTH):
      #draw the tile at the current position
      drawResource(column, row)

#draws the inventory to the screen
def drawInventory():
  #this variable stops other stuff being drawn
  global drawing
  #only draw if nothing else is being drawn
  if drawing == False:
    #something is now being drawn
    drawing = True
    #use a rectangle to cover the current inventory
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
    #display the 'place' and 'craft' text
    for i in range(1,num_rows+1):
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 20 - (i * 100))
      rendererT.write("place")
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 40 - (i * 100))
      rendererT.write("craft")
    #set the inventory position
    xPosition = 70
    yPostition = height - (MAPHEIGHT * TILESIZE) - 80
    itemNum = 0
    for i, item in enumerate(resources):
      #add the image
      rendererT.goto(xPosition, yPostition)
      rendererT.shape(textures[item])
      rendererT.stamp()
      #add the number in the inventory
      rendererT.goto(xPosition, yPostition - TILESIZE)
      rendererT.write(inventory[item])
      #add key to place
      rendererT.goto(xPosition, yPostition - TILESIZE - 20)
      rendererT.write(placekeys[item])
      #add key to craft
      if crafting.get(item) != None:
        rendererT.goto(xPosition, yPostition - TILESIZE - 40)
        rendererT.write(craftkeys[item])     
      #move along to place the next inventory item
      xPosition += 50
      itemNum += 1
      #drop down to the next row every 10 items
      if itemNum % INVWIDTH == 0:
        xPosition = 70
        itemNum = 0
        yPostition -= TILESIZE + 80
    drawing = False

#generate the instructions, including crafting rules
def generateInstructions():
  instructions.append('Crafting rules:')
  #for each resource that can be crafted...
  for rule in crafting:
    #create the crafting rule text
    craftrule = names[rule] + ' = '
    for resource, number in crafting[rule].items():
      craftrule += str(number) + ' ' + names[resource] + ' '
    #add the crafting rule to the instructions
    instructions.append(craftrule)
  #display the instructions
  yPos = height - 20
  for item in instructions:
    rendererT.goto( MAPWIDTH*TILESIZE + 40, yPos)
    rendererT.write(item)
    yPos-=20

#generate a random world
def generateRandomWorld():
  #loop through each row
  for row in range(MAPHEIGHT):
    #loop through each column in that row
    for column in range(MAPWIDTH):
      #pick a random number between 0 and 10
      randomNumber = random.randint(0,10)
      #WATER if the random number is a 1 or a 2
      if randomNumber in [1,2]:
        tile = WATER
      #GRASS if the random number is a 3 or a 4
      elif randomNumber in [3,4]:
        tile = GRASS
      #otherwise it's DIRT
      else:
        tile = DIRT
      #set the position in the tilemap to the randomly chosen tile
      world[column][row] = tile

#---
#Code starts running here
#---

#import the modules and variables needed
import turtle
import random
from variables import *
from math import ceil

TILESIZE = 20
#the number of inventory resources per row
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


