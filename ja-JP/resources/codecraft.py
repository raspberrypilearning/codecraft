#!/bin/python3

#############
# コードクラフト #
#############

#---
#ゲーム用の関数
#---

#プレイヤーを左に1マス動かす
def moveLeft():
  global playerX
  if(drawing == False and playerX > 0):
    oldX = playerX
    playerX -= 1
    drawResource(oldX, playerY)
    drawResource(playerX, playerY)
    
#プレイヤーを右に1マス動かす
def moveRight():
  global playerX, MAPWIDTH
  if(drawing == False and playerX < MAPWIDTH - 1):
    oldX = playerX
    playerX += 1
    drawResource(oldX, playerY)
    drawResource(playerX, playerY)
    
#プレイヤーを上にに1マス動かす
def moveUp():
  global playerY
  if(drawing == False and playerY > 0):
    oldY = playerY
    playerY -= 1
    drawResource(playerX, oldY)
    drawResource(playerX, playerY)
    
#プレイヤーを下に1マス動かす
def moveDown():
  global playerY, MAPHEIGHT
  if(drawing == False and playerY < MAPHEIGHT - 1):
    oldY = playerY
    playerY += 1
    drawResource(playerX, oldY)
    drawResource(playerX, playerY)
    
#プレイヤーの位置にあるリソースをとる。
def pickUp():
  global playerX, playerY
  drawing = True
  currentTile = world[playerX][playerY]
  #ユーザーにはあまりにも多くのリソースがない場合...
  if inventory[currentTile] < MAXTILES:
    #プレイヤーにリソースが1つ追加されました
    inventory[currentTile] += 1
    #プレイヤーが土の上に立っている場合
    world[playerX][playerY] = DIRT
    #新しい土のマスを描く
    drawResource(playerX, playerY)
    #持ち物リストにリソースを追加して描き直す
    drawInventory()
    #drawPlayer()

#プレーヤーの現在の位置にリソースを置く
def place(resource):
  print(u'置く', names[resource])
  #もしプレイヤーがすでにリソースを持っている場合。。。
  if inventory[resource] > 0:
    #プレイヤーの位置にあるリソースを見つけ出す
    currentTile = world[playerX][playerY]
    #プレイヤーの位置にあるリソースをとる。
    #(if it's not DIRT)
    if currentTile is not DIRT:
      inventory[currentTile] += 1
    #プレーヤーの現在の位置にリソースを置く
    world[playerX][playerY] = resource
    #新しいリソースを持ち物リストに追加します
    inventory[resource] -= 1
    #ゲーム画面を更新(ゲームワールドと持ち物リスト)
    drawResource(playerX, playerY)
    drawInventory()
    #drawPlayer()
    print(u'   配置', names[resource], u'完了')
  #。。。もし何もなければ
  else:
    print(u'   あなたは', names[resource], u'を持っていません')

#新しいリソースを作成
def craft(resource):
  print(u'作成：', names[resource])
  #もしリソースを作成できる場合
  if resource in crafting:
    #新たに作成するのに必要なリソースがあるかを
    #確認します
    canBeMade = True
    #リソースの作成に必要な各アイテムについて
    for i in crafting[resource]:
      #。。。もしアイテムが足りなければ。。。
      if crafting[resource][i] > inventory[i]:
      #。。。変数にリソースを作れないと設定する
        canBeMade = False
        break
    #もし作成できる場合(作成するために必要なアイテムがある場合)
    if canBeMade == True:
      #持ち物リストからアイテムを取り出します
      for i in crafting[resource]:
        inventory[i] -= crafting[resource][i]
      #新しいリソースを持ち物リストに追加します
      inventory[resource] += 1
      print('   Crafting', names[resource], 'complete')
    #...otherwise the resource can't be crafted...
    else:
      print('   Can\'t craft', names[resource])
    #update the displayed inventory
    drawInventory()

#creates a function for placing each resource
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

#位置(y,x)のリソースを描画します。
def drawResource(y, x):
  #この変数は他のものが描画できないようにします
  global drawing
  #他に何も描画されていない場合描画します
  if drawing == False:
    #何かが描画されます
    drawing = True
    #正しいイメージを使用して、タイルマップ内のその位置にリソースを描画します
    rendererT.goto( (y * TILESIZE) + 20, height - (x * TILESIZE) - 20 )
    #正しいテクスチャーでタイルを描きます
    texture = textures[world[y][x]]
    rendererT.shape(texture)
    rendererT.stamp()
    if playerX == y and playerY == x:
      rendererT.shape(playerImg)
      rendererT.stamp()
    screen.update()
    #何も描画されていません
    drawing = False
    
#ワールドを描く
def drawWorld():
  #地図上の行をループします
  for row in range(MAPHEIGHT):
    #地図上の列をループします
    for column in range(MAPWIDTH):
      #現在の位置にタイルを表示します
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

#create a new 'screen' object
screen = turtle.Screen()
#calculate the width and height
width = (TILESIZE * MAPWIDTH) + max(200,INVWIDTH * 50)
num_rows = int(ceil((len(resources) / INVWIDTH)))
inventory_height =  num_rows * 120 + 40
height = (TILESIZE * MAPHEIGHT) + inventory_height

screen.setup(width, height)
screen.setworldcoordinates(0,0,width,height)
screen.bgcolor(BACKGROUNDCOLOUR)
screen.listen()

#register the player image  
screen.register_shape(playerImg)
#register each of the resource images
for texture in textures.values():
  screen.register_shape(texture)

#create another turtle to do the graphics drawing
rendererT = turtle.Turtle()
rendererT.hideturtle()
rendererT.penup()
rendererT.speed(0)
rendererT.setheading(90)

#create a world of random resources.
world = [ [DIRT for w in range(MAPHEIGHT)] for h in range(MAPWIDTH) ]

#map the keys for moving and picking up to the correct functions.
screen.onkey(moveUp, 'w')
screen.onkey(moveDown, 's')
screen.onkey(moveLeft, 'a')
screen.onkey(moveRight, 'd')
screen.onkey(pickUp, 'space')

#set up the keys for placing and crafting each resource
bindPlacingKeys()
bindCraftingKeys()

#these functions are defined above
generateRandomWorld()
drawWorld()
drawInventory()
generateInstructions()


