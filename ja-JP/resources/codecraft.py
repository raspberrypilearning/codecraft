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
    #(もし土ではない場合)
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
      print(u'   作成', names[resource], u'完了')
    #。。。リソースを作成できない場合
    else:
      print(u'   作成できない', names[resource])
    #表示されている持ち物リストを更新
    drawInventory()

#各リソースを配置するための関数を作成します
def makeplace(resource):
  return lambda: place(resource)

#各キーに「配置」機能を割り当てます
def bindPlacingKeys():
  for k in placekeys:
    screen.onkey(makeplace(k), placekeys[k])

#リソースを作成する関数を作成する
def makecraft(resource):
  return lambda: craft(resource)

#各キーに「作成」機能を割り当てます
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

#持ち物リストを画面に表示する
def drawInventory():
  #この変数は他のものを描画しないようにします
  global drawing
  #他に何も描画されていない場合描画します
  if drawing == False:
    #何かが現在描画されています。
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
    #「場所」と「リソース」テキストを表示する
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
      #画像を追加する
      rendererT.goto(xPosition, yPostition)
      rendererT.shape(textures[item])
      rendererT.stamp()
      #リソースの数を持ち物リストに追加
      rendererT.goto(xPosition, yPostition - TILESIZE)
      rendererT.write(inventory[item])
      #キーを追加する
      rendererT.goto(xPosition, yPostition - TILESIZE - 20)
      rendererT.write(placekeys[item])
      #キーをリソースに追加する
      if crafting.get(item) != None:
        rendererT.goto(xPosition, yPostition - TILESIZE - 40)
        rendererT.write(craftkeys[item])     
      #移動して次のアイテムを配置
      xPosition += 50
      itemNum += 1
      #10個のアイテムごとに次の行に移動
      if itemNum % INVWIDTH == 0:
        xPosition = 70
        itemNum = 0
        yPostition -= TILESIZE + 80
    drawing = False

#作成ルールを含む説明書きの生成
def generateInstructions():
  instructions.append('作成ルール:')
  #もしリソースを作成できる場合
  for rule in crafting:
    #作成ルール本文を作成
    craftrule = names[rule] + ' = '
    for resource, number in crafting[rule].items():
      craftrule += str(number) + ' ' + names[resource] + ' '
    #作成ルールをゲーム説明書きに追加
    instructions.append(craftrule)
  #説明書きを表示
  yPos = height - 20
  for item in instructions:
    rendererT.goto( MAPWIDTH*TILESIZE + 40, yPos)
    rendererT.write(item)
    yPos-=20

#ワールド（地図）をランダムに作成
def generateRandomWorld():
  #地図上の行をループする
  for row in range(MAPHEIGHT):
    #地図上の列をループする
    for column in range(MAPWIDTH):
      #0から10の数字をランダムに選ぶ
      randomNumber = random.randint(0,10)
      #もしランダムに選ばれた数字が1か2だったら水
      if randomNumber in [1,2]:
        tile = WATER
      #もしランダムに選ばれた数字が3か4だったら草
      elif randomNumber in [3,4]:
        tile = GRASS
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
#各列にあるリソースの数
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

#リソースを作成する、リソースを置くキーの設定
bindPlacingKeys()
bindCraftingKeys()

#これらの関数は上で定義されています
generateRandomWorld()
drawWorld()
drawInventory()
generateInstructions()


