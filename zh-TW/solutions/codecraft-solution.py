#!/bin/python3

#############
# CodeCraft #
#############

#---
＃遊戲功能
#---

#將玩家向左移動一格.
def moveLeft():
  global playerX
  if(drawing == False and playerX > 0):
    oldX = playerX
    playerX -= 1
    drawResource(oldX, playerY)
    drawResource(playerX, playerY)
    
#將玩家向右移動一格.
def moveRight():
  global playerX, MAPWIDTH
  if(drawing == False and playerX < MAPWIDTH - 1):
    oldX = playerX
    playerX += 1
    drawResource(oldX, playerY)
    drawResource(playerX, playerY)
    
#將玩家向上移動一格.
def moveUp():
  global playerY
  if(drawing == False and playerY > 0):
    oldY = playerY
    playerY -= 1
    drawResource(playerX, oldY)
    drawResource(playerX, playerY)
    
#將玩家向下移動一格.
def moveDown():
  global playerY, MAPHEIGHT
  if(drawing == False and playerY < MAPHEIGHT - 1):
    oldY = playerY
    playerY += 1
    drawResource(playerX, oldY)
    drawResource(playerX, playerY)
    
#在玩家的位置撿起資源.
def pickUp():
  global playerX, playerY
  drawing = True
  currentTile = world[playerX][playerY]
  #如果用戶還沒有太多...
  if inventory[currentTile] < MAXTILES:
    #玩家現在有多1個這個資源
    inventory[currentTile] += 1
    #玩家現在站在泥土上
    world[playerX][playerY] = DIRT
    #繪製新的泥土圖塊
    drawResource(playerX, playerY)
    #使用額外的資源重新繪製庫存.
    drawInventory()
    #drawPlayer()

#將一個資源放置在玩家的當前位置
def place(resource):
  print('放置: ', names[resource])
  #僅在玩家有剩餘物品時放置...
  if inventory[resource] > 0:
    #找出玩家當前位置的資源
    currentTile = world[playerX][playerY]
    #在玩家所在的位置撿起資源。
    ＃(如果不是泥土)
    if currentTile is not DIRT:
      inventory[currentTile] += 1
    #將資源放置在玩家的當前位置
    world[playerX][playerY] = resource
    #將新資源添加到庫存中
    inventory[resource] -= 1
    #更新顯示 (世界和庫存)
    drawResource(playerX, playerY)
    drawInventory()
    #drawPlayer()
    print('   放置', names[resource], '完成')
  #...如果沒有資源了...
  else:
    print('   你沒有', names[resource], '了)

#製作新資源
def craft(resource):
  print('製作: ', names[resource])
  #如果可以製作資源...
  if resource in crafting:
    #持續注意我們是否有資源
    #製作這個物品
    canBeMade = True
    #為了所需的物品製作資源
    for i in crafting[resource]:
      #...如果不足夠...
      if crafting[resource][i] > inventory[i]:
      #...我們就不能製作它!
        canBeMade = False
        break
    #如果我們可以製作 (我們擁有所有需要的資源)
    if canBeMade == True:
      #從庫存中取出每個物品
      for i in crafting[resource]:
        inventory[i] -= crafting[resource][i]
      #將新資源添加到庫存中
      inventory[resource] += 1
      print('   放置', names[resource], '完成')
    #...否則將無法製作資源...
    else:
      print('   可以/不可以製作', names[resource])
    #更新顯示的庫存
    drawInventory()

#創建放置每個資源的功能
def makeplace(resource):
  return lambda: place(resource)

#為每個按鍵附加一個“放置”功能
def bindPlacingKeys():
  for k in placekeys:
    screen.onkey(makeplace(k), placekeys[k])

#創建製作每種資源的功能
def makecraft(resource):
  return lambda: craft(resource)

#為每個按鍵附加一個'製作'功能
def bindCraftingKeys():
  for k in craftkeys:
    screen.onkey(makecraft(k), craftkeys[k])

#在(y,x)位置繪製資源
def drawResource(y, x):
  #此變數使其他內容無法被繪製
  global drawing
  #僅在沒有其他內容時繪製
  if drawing == False:
    #有東西正在繪製中
    drawing = True
    #使用正確的圖片在瓦片地圖中繪製資源
    rendererT.goto( (y * TILESIZE) + 20, height - (x * TILESIZE) - 20 )
    #繪製正確紋理的圖塊
    texture = textures[world[y][x]]
    rendererT.shape(texture)
    rendererT.stamp()
    if playerX == y and playerY == x:
      rendererT.shape(playerImg)
      rendererT.stamp()
    screen.update()
    #沒有東西被繪製
    drawing = False
    
#繪製world map
def drawWorld():
  #迴圈每一行
  for row in range(MAPHEIGHT):
    #迴圈行中的每一列
    for column in range(MAPWIDTH):
      #在當前位置繪製圖塊
      drawResource(column, row)

#將庫存繪製到銀幕上
def drawInventory():
  #此變數使其他內容無法被繪製
  global drawing
  #僅在沒有其他內容時繪製
  if drawing == False:
    #有東西正在繪製中
    drawing = True
    #使用矩形覆蓋當前的庫存
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
    rendererT.color('黑色')
    #顯示'放置'和'製作'的文字
    for i in range(1,num_rows+1):
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 20 - (i * 100))
      rendererT.write("放置")
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 40 - (i * 100))
      rendererT.write("製作")
    #設置庫存位置
    xPosition = 70
    yPostition = height - (MAPHEIGHT * TILESIZE) - 60
    itemNum = 0
    for i, item in enumerate(resources):
      #添加圖片
      rendererT.goto(xPosition + 10, yPostition)
      rendererT.shape(textures[item])
      rendererT.stamp()
      #將這個數量添加到庫存中
      rendererT.goto(xPosition, yPostition - TILESIZE)
      rendererT.write(inventory[item])
      #add the name
      rendererT.goto(xPosition, yPostition - TILESIZE - 20)
      rendererT.write('[' + names[item] + ']')
      #增加放置按鍵
      rendererT.goto(xPosition, yPostition - TILESIZE - 40)
      rendererT.write(placekeys[item])
      #增加製作按鍵
      if crafting.get(item) != None:
        rendererT.goto(xPosition, yPostition - TILESIZE - 60)
        rendererT.write(craftkeys[item])     
      #前進以放置下一個庫存物品
      xPosition += 50
      itemNum += 1
      #每10個項目下移至下一行
      if itemNum % INVWIDTH == 0:
        xPosition = 70
        itemNum = 0
        yPostition -= TILESIZE + 80
    drawing = False

#生成指令，包括製作規則
def generateInstructions():
  instructions.append('製作規則:')
  #針對可以製作的每種資源...
  for rule in crafting:
    #創建製作規則
    craftrule = names[rule] + ' = '
    for resource, number in crafting[rule].items():
      craftrule += str(number) + ' ' + names[resource] + ' '
    #將製作規則添加到說明中
    instructions.append(craftrule)
  #顯示說明
  yPos = height - 20
  for item in instructions:
    rendererT.goto( MAPWIDTH*TILESIZE + 40, yPos)
    rendererT.write(item)
    yPos-=20

#生成一個隨機的世界
def generateRandomWorld():
  #迴圈每一行
  for row in range(MAPHEIGHT):
    #迴圈行中的每一列
    for column in range(MAPWIDTH):
      #在 0 到 9 之間隨機選取一個數字
      randomNumber = random.randint(0,10)
      #如果隨機數是1或2是水
      if randomNumber in [1,2]:
        tile = WATER
      #如果隨機數是3或4的話就是草地
      elif randomNumber in [3,4]:
        tile = GRASS
      #如果是5的或是木頭
      elif randomNumber == 5:
        tile = WOOD
      #如果是6的話是沙
      elif randomNumber == 6:
        tile = SAND
      #否則就是泥土
      else:
        tile = DIRT
      #將瓦片地圖中的位置設置在隨機選擇的瓦片上
      world[column][row] = tile

#---
#代碼從此處開始運行
#---

#導入所需的模組和變量
import turtle
import random
from variables import *
from math import ceil

TILESIZE = 20
#每行的庫存資源數量
INVWIDTH = 8
drawing = False

#創建一個新的'銀幕'物件
screen = turtle.Screen()
#計算寬度和高度
width = (TILESIZE * MAPWIDTH) + max(200,INVWIDTH * 50)
num_rows = int(ceil((len(resources) / INVWIDTH)))
inventory_height =  num_rows * 120 + 40
height = (TILESIZE * MAPHEIGHT) + inventory_height

screen.setup(width, height)
screen.setworldcoordinates(0,0,width,height)
screen.bgcolor(BACKGROUNDCOLOUR)
screen.listen()

#註冊玩家的照片  
screen.register_shape(playerImg)
#註冊每個資源的圖片
for texture in textures.values():
  screen.register_shape(texture)

＃創建另一個turtle進行圖形繪製
rendererT = turtle.Turtle()
rendererT.hideturtle()
rendererT.penup()
rendererT.speed(0)
rendererT.setheading(90)

#創建一個有隨機資源的世界.
world = [ [DIRT for w in range(MAPHEIGHT)] for h in range(MAPWIDTH) ]

#設定對應移動及拾取功能的按鍵
screen.onkey(moveUp, 'w')
screen.onkey(moveDown, 's')
screen.onkey(moveLeft, 'a')
screen.onkey(moveRight, 'd')
screen.onkey(pickUp, 'space')

#設定用於放置和製作每個資源的按鍵
bindPlacingKeys()
bindCraftingKeys()

#這些功能如上述定義
generateRandomWorld()
drawWorld()
drawInventory()
generateInstructions()


