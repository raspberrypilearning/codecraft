#!/bin/python3

#############
# 代码世界 #
#############

#---
＃游戏功能
#---

＃将玩家向左移动1个图块。
def moveLeft():
  global playerX
  if(drawing == False and playerX > 0):
    oldX = playerX
    playerX -= 1
    drawResource(oldX, playerY)
    drawResource(playerX, playerY)
    
＃将玩家向右移动1个图块。
def moveRight():
  global playerX, MAPWIDTH
  if(drawing == False and playerX < MAPWIDTH - 1):
    oldX = playerX
    playerX += 1
    drawResource(oldX, playerY)
    drawResource(playerX, playerY)
    
＃将玩家向上移动1个图块。
def moveUp():
  global playerY
  if(drawing == False and playerY > 0):
    oldY = playerY
    playerY -= 1
    drawResource(playerX, oldY)
    drawResource(playerX, playerY)
    
＃将玩家向下移动1个图块。
def moveDown():
  global playerY, MAPHEIGHT
  if(drawing == False and playerY < MAPHEIGHT - 1):
    oldY = playerY
    playerY += 1
    drawResource(playerX, oldY)
    drawResource(playerX, playerY)
    
＃在玩家的位置捡起资源。
def pickUp():
  global playerX, playerY
  drawing = True
  currentTile = world[playerX][playerY]
  ＃如果用户还没有太多资源...
  if inventory[currentTile] < MAXTILES:
    #玩家现在有1个此资源
    inventory[currentTile] += 1
    ＃玩家现在站在泥土上
    world[playerX][playerY] = DIRT
    ＃绘制新的泥土图块
    drawResource(playerX, playerY)
    #用额外资源重新绘制。
    drawInventory()
    #drawPlayer()

＃将资源放置在玩家的当前位置
def place(resource):
  print('放置中: ', names[resource])
  ＃仅在玩家有剩余资源时才放置...
  if inventory[resource] > 0:
    ＃找到玩家当前位置的资源
    currentTile = world[playerX][playerY]
    ＃在玩家的位置捡起资源。
    #(如果不是DIRT)
    if currentTile is not DIRT:
      inventory[currentTile] += 1
    ＃将资源放置在玩家的当前位置
    world[playerX][playerY] = resource
    ＃将新资源添加到背包
    inventory[resource] -= 1
    ＃更新显示 (世界和背包)
    drawResource(playerX, playerY)
    drawInventory()
    #drawPlayer()
    print('放置', names[resource], '完成')
  #...如果没有剩余...
  else:
    print('您没有', names[resource], '剩余')

#制作一个新的资源
def craft(resource):
  print('构建中: ', names[resource])
  ＃如果可以制作资源...
  if resource in crafting:
    #保持跟踪我们是否有资源
    #制作这个物品
    canBeMade = True
    ＃针对制作资源所需的每个项目
    for i in crafting[resource]:
      ＃...如果我们没有足够的...
      if crafting[resource][i] > inventory[i]:
      ＃...我们做不到！
        canBeMade = False
        break
    ＃如果我们能制作出来的话 (我们拥有所有需要的资源)
    if canBeMade == True:
      ＃从背包中取出每个物品
      for i in crafting[resource]:
        inventory[i] -= crafting[resource][i]
      ＃将制作的物品添加到库存中
      inventory[resource] += 1
      print('正在构建', names[resource], '完成')
    ＃...否则将无法制作资源...
    else:
      print('不能构建', names[resource])
    ＃更新显示的库存
    drawInventory()

#创建一个用于放置每个资源的函数
def makeplace(resource):
  return lambda: place(resource)

#给按钮事件添加一个 “放置” 函数
def bindPlacingKeys():
  for k in placekeys:
    screen.onkey(makeplace(k), placekeys[k])

＃创建用于制作每个资源的函数
def makecraft(resource):
  return lambda: craft(resource)

＃给按钮事件添加一个 “制作” 函数
def bindCraftingKeys():
  for k in craftkeys:
    screen.onkey(makecraft(k), craftkeys[k])

＃在 (y，x) 位置绘制资源
def drawResource(y, x):
  ＃此变量停止绘制其他内容
  global drawing
  ＃仅在没有其他内容绘制时绘制
  if drawing == False:
    #东西正在绘制中
    drawing = True
    ＃使用正确的图片在tilemap中的该位置绘制资源
    rendererT.goto( (y * TILESIZE) + 20, height - (x * TILESIZE) - 20 )
    ＃绘制纹理正确的图块
    texture = textures[world[y][x]]
    rendererT.shape(texture)
    rendererT.stamp()
    if playerX == y and playerY == x:
      rendererT.shape(playerImg)
      rendererT.stamp()
    screen.update()
    ＃现在什么都没画
    drawing = False
    
＃绘制世界地图
def drawWorld():
  ＃循环遍历每一行
  for row in range(MAPHEIGHT):
    #循环行中的每一列
    for column in range(MAPWIDTH):
      ＃在当前位置绘制图块
      drawResource(column, row)

#将背包里的资源放到屏幕上
def drawInventory():
  #此变量停止正在绘制的其他内容
  global drawing
  ＃仅在没有其他内容绘制时绘制
  if drawing == False:
    #东西正在绘制中
    drawing = True
    #使用矩形来覆盖当前物品栏
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
    #显示 '位置' 和 '组件' 文本
    for i in range(1,num_rows+1):
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 20 - (i * 100))
      rendererT.write("位置")
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 40 - (i * 100))
      rendererT.write("组件")
    ＃设置库存位置
    xPosition = 70
    yPostition = height - (MAPHEIGHT * TILESIZE) - 60
    itemNum = 0
    for i, item in enumerate(resources):
      ＃添加图片
      rendererT.goto(xPosition + 10, yPostition)
      rendererT.shape(textures[item])
      rendererT.stamp()
      # 将物品加入玩家的物品清单
      rendererT.goto(xPosition, yPostition - TILESIZE)
      rendererT.write(inventory[item])
      #add the name
      rendererT.goto(xPosition, yPostition - TILESIZE - 20)
      rendererT.write('[' + names[item] + ']')
      #添加 key 到位置
      rendererT.goto(xPosition, yPostition - TILESIZE - 40)
      rendererT.write(placekeys[item])
      #添加 key 到组件
      if crafting.get(item) != None:
        rendererT.goto(xPosition, yPostition - TILESIZE - 60)
        rendererT.write(craftkeys[item])     
      #移动以放置下一个物品栏
      xPosition += 50
      itemNum += 1
      ＃每10个项目下移至下一行
      if itemNum % INVWIDTH == 0:
        xPosition = 70
        itemNum = 0
        yPostition -= TILESIZE + 80
    drawing = False

#生成指令，包括制造规则
def generateInstructions():
  instructions.append('建造规则:')
  ＃针对可以制作的每种资源...
  for rule in crafting:
    #创建制造规则文本
    craftrule = names[rule] + ' = '
    for resource, number in crafting[rule].items():
      craftrule += str(number) + ' ' + names[resource] + ' '
    #将制造规则添加到说明中
    instructions.append(craftrule)
  ＃显示说明
  yPos = height - 20
  for item in instructions:
    rendererT.goto( MAPWIDTH*TILESIZE + 40, yPos)
    rendererT.write(item)
    yPos-=20

＃生成随机世界
def generateRandomWorld():
  ＃循环遍历每一行
  for row in range(MAPHEIGHT):
    #循环行中的每一列
    for column in range(MAPWIDTH):
      ＃选择0到10之间的随机数
      randomNumber = random.randint(0,10)
      #如果随机数是1或2 创建 WATER 水
      if randomNumber in [1,2]:
        tile = WATER
      #随机数是3或4 创建 GRASS 草皮
      elif randomNumber in [3,4]:
        tile = GRASS
      ＃否则就是 DIRT 泥土
      else:
        tile = DIRT
      #将层图中的位置设置为随机选择的图块
      world[column][row] = tile

#---
＃代码从此处开始运行
#---

＃导入所需的模块和变量
import turtle
import random
from variables import *
from math import ceil

TILESIZE = 20
＃每行的物品栏资源数量
INVWIDTH = 8
drawing = False

＃创建一个新的“屏幕”对象
screen = turtle.Screen()
＃计算宽度和高度
width = (TILESIZE * MAPWIDTH) + max(200,INVWIDTH * 50)
num_rows = int(ceil((len(resources) / INVWIDTH)))
inventory_height =  num_rows * 120 + 40
height = (TILESIZE * MAPHEIGHT) + inventory_height

screen.setup(width, height)
screen.setworldcoordinates(0,0,width,height)
screen.bgcolor(BACKGROUNDCOLOUR)
screen.listen()

＃注册玩家图像  
screen.register_shape(playerImg)
#注册每个资源图像
for texture in textures.values():
  screen.register_shape(texture)

#创建另一个海龟来绘制图形
rendererT = turtle.Turtle()
rendererT.hideturtle()
rendererT.penup()
rendererT.speed(0)
rendererT.setheading(90)

#创建一个随机资源的世界。
world = [ [DIRT for w in range(MAPHEIGHT)] for h in range(MAPWIDTH) ]

#映射移动和提取到正确函数的键值。
screen.onkey(moveUp, 'w')
screen.onkey(moveDown, 's')
screen.onkey(moveLeft, 'a')
screen.onkey(moveRight, 'd')
screen.onkey(pickUp, 'space')

#设置放置和制造每个资源的密钥
bindPlacingKeys()
bindCraftingKeys()

#这些函数已在上面定义
generateRandomWorld()
drawWorld()
drawInventory()
generateInstructions()
