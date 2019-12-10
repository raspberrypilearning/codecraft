#!/bin/python3

#############
# صناعة الأكواد #
#############

#---
وظائف اللعبة#
#---

#تحريك اللاعب بلاطه واحده إلى اليسار.
def moveLeft():
  global playerX
  if(drawing == False and playerX > 0):
    oldX = playerX
    playerX -= 1
    drawResource(oldX, playerY)
    drawResource(playerX, playerY)
    
#تحريك اللاعب بلاطه واحده إلى اليمين.
def moveRight():
  global playerX, MAPWIDTH
  if(drawing == False and playerX < MAPWIDTH - 1):
    oldX = playerX
    playerX += 1
    drawResource(oldX, playerY)
    drawResource(playerX, playerY)
    
#تحريك اللاعب بلاطه واحده إلى الأعلى.
def moveUp():
  global playerY
  if(drawing == False and playerY > 0):
    oldY = playerY
    playerY -= 1
    drawResource(playerX, oldY)
    drawResource(playerX, playerY)
    
#تحريك اللاعب بلاطه واحده إلى الأسفل.
def moveDown():
  global playerY, MAPHEIGHT
  if(drawing == False and playerY < MAPHEIGHT - 1):
    oldY = playerY
    playerY += 1
    drawResource(playerX, oldY)
    drawResource(playerX, playerY)
    
#جمع الموارد من منطقة اللاعب.
def pickUp():
  global playerX, playerY
  drawing = True
  currentTile = world[playerX][playerY]
  #إذا المستخدم لا يملك موارد كافية...
  if inventory[currentTile] < MAXTILES:
    #يملك اللاعب الان واحد اضافي من هذا المورد
    inventory[currentTile] += 1
    #اللاعب الان يقف على الطين
    world[playerX][playerY] = DIRT
    #رسم منطقة من الطين جديدة
    drawResource(playerX, playerY)
    #إعادة رسم المخزون بالموارد الإضافية.
    drawInventory()
    #drawPlayer()

#ضع موردًا في مكان اللاعب حاليًا
def place(resource):
  print('وضع: ', names[resource])
  #ضع موردا في مكان اللاعب في حال إمتلاكه أحدها...
  if inventory[resource] > 0:
    #اكتشف الموارد في منطقة اللاعب الحاليه
    currentTile = world[playerX][playerY]
    #جمع الموارد من منطقة اللاعب
    #(إذا لم يكن طين)
    if currentTile is not DIRT:
      inventory[currentTile] += 1
    #ضع موردًا في مكان اللاعب حاليًا
    world[playerX][playerY] = resource
    #اضف المورد الجديد إلى المخزون
    inventory[resource] -= 1
    #تحديث مظهر(العالم و المخزون)
    drawResource(playerX, playerY)
    drawInventory()
    #drawPlayer()
    print('   صناعة', names[resource], 'اكتملت')
  #... في حال لم يعد يمتلك مورد...
  else:
    print('   ليس لديك', names[resource], 'متبقي')

#إنشاء مورد جديد
def craft(resource):
  print('صناعة: ', names[resource])
  #اذا كان بالامكان انشاء المورد...
  if resource in crafting:
    #يتتبع في حال وجود الموارد
    #لإنشاء هذا العنصر
    canBeMade = True
    #لكل عنصر يلزمة إنشاء مورد
    for i in crafting[resource]:
      #... إذا لم يمتلك ما يكفيه...
      if crafting[resource][i] > inventory[i]:
      #...لا تستطيع إنشائه!
        canBeMade = False
        break
    #إذا يمكن إنشائه(فإنه يملك جميع الموارد اللازمة)
    if canBeMade == True:
      #خذ كل عنصر من المخزون
      for i in crafting[resource]:
        inventory[i] -= crafting[resource][i]
      #اضف العنصر الجديد إلى المخزون
      inventory[resource] += 1
      print('   صناعة', names[resource], 'اكتملت')
    #... غير ذلك فإن المورد لا يمكن إنشائه...
    else:
      print('   لا يمكن صناعة', names[resource])
    #تحديث مظهر المخزون
    drawInventory()

#إنشاء دالة لوضع المورد
def makeplace(resource):
  return lambda: place(resource)

#ارفق دالة 'وضع' لكل ضغطة المفتاح
def bindPlacingKeys():
  for k in placekeys:
    screen.onkey(makeplace(k), placekeys[k])

#إنشاء دالة لانشاء المورد
def makecraft(resource):
  return lambda: craft(resource)

#ارفق دالة 'صناعة' لكل ضغطة المفتاح
def bindCraftingKeys():
  for k in craftkeys:
    screen.onkey(makecraft(k), craftkeys[k])

#رسم مورد في منطقة (ص،س)
def drawResource(y, x):
  # هذا المتغير يتوقف على الأشياء الأخرى التي يتم رسمها
  global drawing
  #فقط ارسم في حال لم يتم رسم شيء آخر
  if drawing == False:
    #شيء ما يتم رسمه الآن
    drawing = True
    # رسم المورد في منطقة معينة من خريطة البلاط، باستخدام الصورة الصحيحة
    rendererT.goto( (y * TILESIZE) + 20, height - (x * TILESIZE) - 20 )
    #رسم البلاط بالبنية الصحيحة
    texture = textures[world[y][x]]
    rendererT.shape(texture)
    rendererT.stamp()
    if playerX == y and playerY == x:
      rendererT.shape(playerImg)
      rendererT.stamp()
    screen.update()
    #لا شيء يتم رسمه
    drawing = False
    
#رسم خريطة العالم
def drawWorld():
  #كرر من خلال كل صف
  for row in range(MAPHEIGHT):
    #كرر من خلال كل عمود في الصف
    for column in range(MAPWIDTH):
      #رسم البلاط في المنطقة الحالية
      drawResource(column, row)

#رسم المخزون على الشاشة
def drawInventory():
  # هذا المتغير يتوقف على الأشياء الأخرى التي يتم رسمها
  global drawing
  #فقط ارسم في حال لم يتم رسم شيء آخر
  if drawing == False:
    #شيء ما يتم رسمه الآن
    drawing = True
    #استخدم المستطيل لتغطية المخزون الحالي
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
    rendererT.color('اسود')
    #عرض نص "المكان" و"الصنعة"
    for i in range(1,num_rows+1):
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 20 - (i * 100))
      rendererT.write("المكان")
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 40 - (i * 100))
      rendererT.write("الصنعة")
    #ضبط منطقة المخزون
    xPosition = 70
    yPostition = height - (MAPHEIGHT * TILESIZE) - 80
    itemNum = 0
    for i, item in enumerate(resources):
      #اضف الصورة
      rendererT.goto(xPosition, yPostition)
      rendererT.shape(textures[item])
      rendererT.stamp()
      #اضف قيمة المخزون
      rendererT.goto(xPosition, yPostition - TILESIZE)
      rendererT.write(inventory[item])
      #اضف مفتاح للمكان
      rendererT.goto(xPosition, yPostition - TILESIZE - 20)
      rendererT.write(placekeys[item])
      #اضف مفتاح للصناعة
      if crafting.get(item) != None:
        rendererT.goto(xPosition, yPostition - TILESIZE - 40)
        rendererT.write(craftkeys[item])     
      #التحرك لوضع عنصر المخزون التالي
      xPosition += 50
      itemNum += 1
      #انتقل الى الصف التالي كل 10 عناصر
      if itemNum % INVWIDTH == 0:
        xPosition = 70
        itemNum = 0
        yPostition -= TILESIZE + 80
    drawing = False

#توفير التعليمات، بالاضافة الى قوانين الصناعه
def generateInstructions():
  instructions.append('قوانين الصناعة:')
  #لكل مورد يمكن إنشائه...
  for rule in crafting:
    #إنشاء نص قانون الصياغة
    craftrule = names[rule] + ' = '
    for resource, number in crafting[rule].items():
      craftrule += str(number) + ' ' + names[resource] + ' '
    #اضف قواعد الصناعه على التعليمات
    instructions.append(craftrule)
  #إظهار التعليمات
  yPos = height - 20
  for item in instructions:
    rendererT.goto( MAPWIDTH*TILESIZE + 40, yPos)
    rendererT.write(item)
    yPos-=20

#إدراج عالم عشوائي
def generateRandomWorld():
  #كرر من خلال كل صف
  for row in range(MAPHEIGHT):
    #كرر من خلال كل عمود في الصف
    for column in range(MAPWIDTH):
      #اختر رقم عشوائي بين 0 الى 10
      randomNumber = random.randint(0,10)
      # الماء إذا كان الرقم العشوائي 1 او 2
      if randomNumber in [1,2]:
        tile = WATER
      #عشب إذا كان الرقم العشوائي 3 او 4
      elif randomNumber in [3,4]:
        tile = GRASS
      #خشب إذا كان الرقم 5
      elif randomNumber == 5:
        tile = WOOD
      #رمل إذا كان 6
      elif randomNumber == 6:
        tile = SAND
      # غير ذلك فهو طين
      else:
        tile = DIRT
      #ضبط الموقع في خريطة البلاط للأختيار العشوائي للبلاط
      world[column][row] = tile

#---
#يبدأ تشغيل الكود من هنا
#---

#استدعي الوحدات والمتغيرات اللازمة
import turtle
import random
from variables import *
from math import ceil

TILESIZE = 20
#عدد موارد المخزون لكل صف
INVWIDTH = 8
drawing = False

# إنشاء كائن "شاشة" جديد
screen = turtle.Screen()
# حساب العرض والارتفاع
width = (TILESIZE * MAPWIDTH) + max(200,INVWIDTH * 50)
num_rows = int(ceil((len(resources) / INVWIDTH)))
inventory_height =  num_rows * 120 + 40
height = (TILESIZE * MAPHEIGHT) + inventory_height

screen.setup(width, height)
screen.setworldcoordinates(0,0,width,height)
screen.bgcolor(BACKGROUNDCOLOUR)
screen.listen()

#تسجيل صورة اللاعب  
screen.register_shape(playerImg)
#تسجيل كل صور الموارد
for texture in textures.values():
  screen.register_shape(texture)

#إنشاء سلاحف اخرى للقيام بالرسم البياني
rendererT = turtle.Turtle()
rendererT.hideturtle()
rendererT.penup()
rendererT.speed(0)
rendererT.setheading(90)

#إنشاء عالم من الموارد العشوائية.
world = [ [DIRT for w in range(MAPHEIGHT)] for h in range(MAPWIDTH) ]

#تعيين مفتاح لتحريك والتقاط المهام الصحيحة.
screen.onkey(moveUp, 'w')
screen.onkey(moveDown, 's')
screen.onkey(moveLeft, 'a')
screen.onkey(moveRight, 'd')
screen.onkey(pickUp, 'مسافة')

#ضبط مفاتيح لوضع وصياغة كل مورد
bindCraftingKeys()
bindCraftingKeys()

#هذه الدوال معرفة بالاعلى
generateRandomWorld()
drawWorld()
drawInventory()
generateInstructions()


