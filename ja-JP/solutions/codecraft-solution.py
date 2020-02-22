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
  #ユーザーのリソース数が多すぎない場合...
  if inventory[currentTile] < MAXTILES:
    #プレイヤーにリソースが1つ追加されます
    inventory[currentTile] += 1
    #プレイヤーの立っているマスは土になります
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
    #プレイヤーの位置にあるリソースを見ます
    currentTile = world[playerX][playerY]
    #プレイヤーの位置にあるリソースをとる。
    #（もし土ではない場合）
    if currentTile is not DIRT:
      inventory[currentTile] += 1
    #プレーヤーの現在の位置にリソースを置く
    world[playerX][playerY] = resource
    #新しいリソースを持ち物リストに追加する
    inventory[resource] -= 1
    #ゲーム画面を更新（ゲームワールドと持ち物リスト）
    drawResource(playerX, playerY)
    drawInventory()
    #drawPlayer()
    print(u'   配置', names[resource], u'完了')
  #。。。もし何もなければ
  else:
    print(u'   あなたは', names[resource], u'を持っていません')

#新しいリソースを作成
def craft(resource):
  print('Crafting: ', names[resource])
  #if the resource can be crafted...
  if resource in crafting:
    #keeps track of whether we have the resources
    #to craft this item
    canBeMade = True
    #for each item needed to craft the resource
    for i in crafting[resource]:
      #...if we don't have enough...
      if crafting[resource][i] > inventory[i]:
      #...we can't craft it!
        canBeMade = False
        break
    #if we can craft it (we have all needed resources)
    if canBeMade == True:
      #take each item from the inventory
      for i in crafting[resource]:
        inventory[i] -= crafting[resource][i]
      #add the crafted item to the inventory
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

#draws a resource at the position (y,x)
def drawResource(y, x):
  #this variable stops other stuff being drawn
  global drawing
  #only draw if nothing else is being drawn
  if drawing == False:
    #描画中にします
    drawing = True
    #対応する画像を使用して、タイルマップ内のその位置にリソースを描画する
    rendererT.goto( (y * TILESIZE) + 20, height - (x * TILESIZE) - 20 )
    #対応するテクスチャーでタイルを描く
    texture = textures[world[y][x]]
    rendererT.shape(texture)
    rendererT.stamp()
    if playerX == y and playerY == x:
      rendererT.shape(playerImg)
      rendererT.stamp()
    screen.update()
    #描画完了にします
    drawing = False
    
#ワールドを描く
def drawWorld():
  #地図上の行をループする
  for row in range(MAPHEIGHT):
    #地図上の列をループする
    for column in range(MAPWIDTH):
      #現在の位置にタイルを表示する
      drawResource(column, row)

#持ち物リストを画面に表示する
def drawInventory():
  #この変数は他のものを描画しないようにします
  global drawing
  #他に何も描画されていない場合描画します
  if drawing == False:
    #描画中にします
    drawing = True
    #四角形を使用して持ち物リストをカバーしてください
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
    #「場所」と「リソース」の文字を表示する
    for i in range(1,num_rows+1):
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 20 - (i * 100))
      rendererT.write(u"置く")
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 40 - (i * 100))
      rendererT.write(u"クラフト（作成）")
    #持ち物リストの位置を設定する
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
      #もしランダムに選ばれた数字が3か4だったら草
      elif randomNumber in [3,4]:
        tile = GRASS
      #もしランダムに選ばれた数字が5だったら木
      elif randomNumber == 5:
        tile = WOOD
      #もしランダムに選ばれた数字が6だったら木
      elif randomNumber == 6:
        tile = SAND
      #他の数字だったら土
      else:
        tile = DIRT
      #地図上の位置に選ばれたリソースをセットする（置く）
      world[column][row] = tile

#---
#コードはここから実行を開始します
#---

#必要なモジュールと変数をインポート
import turtle
import random
from variables import *
from math import ceil

TILESIZE = 20
#各行にあるリソースの数
INVWIDTH = 8
drawing = False

#新しい「スクリーン」オブジェクトを作成する
screen = turtle.Screen()
#幅と高さを計算する
width = (TILESIZE * MAPWIDTH) + max(200,INVWIDTH * 50)
num_rows = int(ceil((len(resources) / INVWIDTH)))
inventory_height =  num_rows * 120 + 40
height = (TILESIZE * MAPHEIGHT) + inventory_height

screen.setup(width, height)
screen.setworldcoordinates(0,0,width,height)
screen.bgcolor(BACKGROUNDCOLOUR)
screen.listen()

#プレーヤーの画像を登録する  
screen.register_shape(playerImg)
#各リソースの画像を登録する
for texture in textures.values():
  screen.register_shape(texture)

#グラフィックを描くために別のカメを作成する
rendererT = turtle.Turtle()
rendererT.hideturtle()
rendererT.penup()
rendererT.speed(0)
rendererT.setheading(90)

#ランダムにリソースが散らばっているワールド（地図）を作成
world = [ [DIRT for w in range(MAPHEIGHT)] for h in range(MAPWIDTH) ]

#プレイヤーを移動させるキーを設定
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


