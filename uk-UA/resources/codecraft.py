#!/bin/python3

#############
# CodeCraft #
#############

#---
#Ігрові функції
#---

#переміщає гравця на 1 плитку ліворуч.
def moveLeft ():
  global playerX
  if(drawing == False and playerX > 0):
    oldX = playerX
    playerX - = 1
    drawResource(oldX, playerY)
    drawResource(playerX, playerY)
    
#перемістити гравця на 1 плитку праворуч.
def moveRight():
  global playerX, MAPWIDTH
  if(drawing == False and playerX < MAPWIDTH - 1):
    oldX = playerX
    playerX + = 1
    drawResource(oldX, playerY)
    drawResource(playerX, playerY)
    
#переміщає гравця на 1 плитку вверх.
def moveUp():
  global playerY
  if(drawing == False and playerY > 0):
    oldY = playerY
    playerY - = 1
    drawResource(playerX, oldY)
    drawResource(playerX, playerY)
    
#переміщає гравця на 1 плитку вниз.
def moveDown():
  global playerY, MAPHEIGHT
  if(drawing == False and playerY < MAPHEIGHT - 1):
    oldY = playerY
    playerY += 1
    drawResource(playerX, oldY)
    drawResource(playerX, playerY)
    
#підбирає ресурс з позиції гравця.
def pickUp():
  global playerX, playerY
  drawing = True
  currentTile = world[playerX][playerY]
  #якщо гравець ще не має надто багато...
  if inventory[currentTile] < MAXTILES:
    #гравець тепер має на 1 більше цього ресурсу
    inventory[currentTile] += 1
    #гравець зараз стоїть на землі
    world[playerX][playerY] = DIRT
    #намалювати нову плитку землі
    drawResource(playerX, playerY)
    #перемалювати інвентар з додатковим ресурсом.
    drawInventory()
    #drawPlayer()

#поставити ресурс на поточну позицію гравця
def place(resource):
  print('Розміщуємо: ', names[resource])
  #розміщуємо тільки якщо у гравця є ресурс...
  if inventory[resource] > 0:
    #визначаємо ресурс на поточній позиції гравця
    currentTile = world[playerX][playerY]
    #підбираємо ресурс з-під ніг гравця
    #(якщо це не земля)
    if currentTile is not DIRT:
      inventory[currentTile] += 1
    #ставимо ресурс на поточну позицію гравця
    world[playerX][playerY] = resource
    #віднімаємо ресурс з інвентарю
    inventory[resource] -= 1
    #оновлюємо дисплей (світ та інвентар)
    drawResource(playerX, playerY)
    drawInventory()
    #drawPlayer()
    print('   Ресурс', names[resource], 'розміщено')
  #...і якщо жодного не залишилось...
  else:
    print('   Ресурсу', names[resource], 'немає')

#створюємо новий ресурс
def craft(resource):
  print('Створюємо: ', names[resource])
  #якщо ресурс можна створити...
  if resource in crafting:
    #відстежуємо чи є у нас ресурси
    #щоб створити предмет
    canBeMade = True
    #для кожного предмету потрібного для створення ресурсу
    for i in crafting[resource]:
      #...якщо ми не маємо достатньо...
      if crafting[resource][i] > inventory[i]:
      #...ми не можемо створити!
        canBeMade = False
        break
    #якщо ми можемо створити (у нас є всі необхідні ресурси)
    if canBeMade == True:
      #взяти кожен елемент з інвентарю
      for i in crafting[resource]:
        inventory[i] -= crafting[resource][i]
      #додаємо створений предмет до інвентарю
      inventory[resource] += 1
      print('   Ресурс', names[resource], 'розміщено')
    #...в іншому випадку ресурс не можливо створити...
    else:
      print('   Не можливо створити ресурс', names[resource])
    #оновлюємо зображення інвентарю
    drawInventory()

#створює функцію для розміщення кожного ресурсу
def makeplace(resource):
  return lambda: place(resource)

#прикріплює функцію 'розміщення' до кожної клавіші
def bindPlacingKeys():
  for k in placekeys:
    screen.onkey(makeplace(k), placekeys[k])

#створює функцію для розміщення кожного ресурсу
def makecraft(resource):
  return lambda: craft(resource)

#прикріплює функцію 'створення' до кожної клавіші
def bindCraftingKeys():
  for k in craftkeys:
    screen.onkey(makecraft(k), craftkeys[k])

#малює ресурс на позиції (y, x)
def drawResource(y, x):
  #ця змінна зупиняє промальовування інших речей, поки попереднє не завершилось
  global drawing
  #малюємо тільки якщо нічого не малюється
  if drawing == False:
    #зараз щось малюється
    drawing = True
    #малює ресурс на позиції на карті плиток, використовуючи правильне зображення
    rendererT.goto( (y * TILESIZE) + 20, height - (x * TILESIZE) - 20 )
    #намалювати плитку з правильною текстурою
    texture = textures[world[y][x]]
    rendererT.shape(texture)
    rendererT.stamp()
    if playerX == y and playerY == x:
      rendererT.shape(playerImg)
      rendererT.stamp()
    screen.update()
    #тепер нічого не малюється
    drawing = False
    
#draws карта світу
def drawWorld():
  #цикл через кожен рядок
  for row in range(MAPHEIGHT):
    #цикл через кожен стовпець рядка
    for column in range(MAPWIDTH):
      #малює плитку на поточній позиції
      drawResource(column, row)

#малює інвентар на екрані
def drawInventory():
  #ця змінна зупиняє промальовування інших речей, поки попереднє не завершилось
  global drawing
  #малюємо тільки якщо нічого не малюється
  if drawing == False:
    #зараз щось малюється
    drawing = True
    #використовуємо прямокутник, щоб приховати поточний інвентар
    rendererT.color(BACKGROUNDCOLOUR)
    rendererT.goto(0,0)
    rendererT.begin_fill()
    #rendererT.setheading (0)
    for i in range(2):
      rendererT.forward(inventory_height - 60)
      rendererT.right(90)
      rendererT.forward(width)
      rendererT.right(90)
    rendererT.end_fill()
    rendererT.color('black')
    #відобразити текст 'розмістити' і 'створити'
    for i in range(1,num_rows+1):
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 20 - (i * 100))
      rendererT.write("розмістити")
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 40 - (i * 100))
      rendererT.write("створити")
    #встановлюємо позицію інвентарю
    xPosition = 70
    yPostition = height - (MAPHEIGHT * TILESIZE) - 80
    itemNum = 0
    for i, item in enumerate(resources):
      #додаємо зображення
      rendererT.goto(xPosition, yPostition)
      rendererT.shape(textures[item])
      rendererT.stamp()
      #додаємо кількість ресурсу в інвентарі
      rendererT.goto(xPosition, yPostition - TILESIZE)
      rendererT.write(inventory[item])
      #додаємо кнопку для розміщення
      rendererT.goto(xPosition, yPostition - TILESIZE - 20)
      rendererT.write(placekeys[item])
      #додаємо кнопку для створення
      if crafting.get(item) != None:
        rendererT.goto(xPosition, yPostition - TILESIZE - 40)
        rendererT.write(craftkeys[item])     
      #зміщуємося для розміщення наступного елемента інвентарю
      xPosition += 50
      itemNum += 1
      #зміщуємося на наступний рядок через кожних 10 елементів
      if itemNum % INVWIDTH == 0:
        xPosition = 70
        itemNum = 0
        yPostition -= TILESIZE + 80
    drawing = False

#генеруємо інструкції, разом з правилами створення
def generateInstructions():
  instructions.append('Правила створення:')
  #для кожного ресурсу який можна створити...
  for rule in crafting:
    #утворюємо текст з правилом створення
    craftrule = names[rule] + ' = '
    for resource, number in crafting[rule].items():
      craftrule += str(number) + ' ' + names[resource] + ' '
    #додаємо правило створення до інструкцій
    instructions.append(craftrule)
  #відображаємо інструкції
  yPos = height - 20
  for item in instructions:
    rendererT.goto( MAPWIDTH*TILESIZE + 40, yPos)
    rendererT.write(item)
    yPos-=20

#Генеруємо випадковий світ
def generateRandomWorld():
  #цикл через кожен рядок
  for row in range(MAPHEIGHT):
    #цикл через кожен стовпець рядка
    for column in range(MAPWIDTH):
      #беремо випадкове число між 0 і 10
      randomNumber = random.randint(0,10)
      #Вода, якщо випадкове число - 1 або 2
      if randomNumber in [1,2]:
        tile = WATER
      #Трава, якщо випадкове число - 3 або 4
      elif randomNumber in [3,4]:
        tile = GRASS
      #в іншому випадку земля
      else:
        tile = DIRT
      #встановлюємо випадково вибраний ресурс на позицію у карті плиток
      world[column][row] = tile

#---
#Код запускається тут
#---

#імпортуємо необхідні модулі та змінні
import turtle
import random
from variables import *
from math import ceil

TILESIZE = 20
#кількість ресурсів у рядку інвентаря
INVWIDTH = 8
drawing = False

#створюємо новий об'єкт "екрану"
screen = turtle.Screen()
#вираховуємо ширину і висоту
width = (TILESIZE * MAPWIDTH) + max(200,INVWIDTH * 50)
num_rows = int(ceil((len(resources) / INVWIDTH)))
inventory_height =  num_rows * 120 + 40
height = (TILESIZE * MAPHEIGHT) + inventory_height

screen.setup(width, height)
screen.setworldcoordinates(0,0,width,height)
screen.bgcolor(BACKGROUNDCOLOUR)
screen.listen()

#реєструємо зображення гравця  
screen.register_shape(playerImg)
#реєструємо зображення усіх ресурсів
for texture in textures.values():
  screen.register_shape(texture)

#створюємо іншу turtle (черепашку) для зображення картинок
rendererT = turtle.Turtle()
rendererT.hideturtle()
rendererT.penup()
rendererT.speed(0)
rendererT.setheading (90)

#створюмо світ з випадковими ресурсами.
world = [ [DIRT for w in range(MAPHEIGHT)] for h in range(MAPWIDTH) ]

#встановлюємо клавіші для переміщення та підбору предметів.
screen.onkey(moveUp, 'w')
screen.onkey(moveDown, 's')
screen.onkey(moveLeft, 'a')
screen.onkey(moveRight, 'd')
screen.onkey(pickUp, 'space')

#встановлюємо клавіші для встановлення та створення ресурсів
bindPlacingKeys()
bindCraftingKeys()

#ці функції визначені вище
generateRandomWorld()
drawWorld()
drawInventory()
generateInstructions()


