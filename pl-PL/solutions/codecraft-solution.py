#!/bin/python3

#############
# CodeCraft #
#############

#---
#Game functions
#---

# przesuń gracza o 1 pole w lewo.
def moveLeft():
  global playerX
  if(drawing == False and playerX > 0):
    oldX = playerX
    playerX -= 1
    drawResource(oldX, playerY)
    drawResource(playerX, playerY)
    
# przesuń gracza o 1 pole w prawo.
def moveRight():
  global playerX, MAPWIDTH
  if(drawing == False and playerX < MAPWIDTH - 1):
    oldX = playerX
    playerX += 1
    drawResource(oldX, playerY)
    drawResource(playerX, playerY)
    
# przesuń gracza o 1 pole do góry.
def moveUp():
  global playerY
  if(drawing == False and playerY > 0):
    oldY = playerY
    playerY -= 1
    drawResource(playerX, oldY)
    drawResource(playerX, playerY)
    
#moves the player down 1 tile.
def moveDown():
  global playerY, MAPHEIGHT
  if(drawing == False and playerY < MAPHEIGHT - 1):
    oldY = playerY
    playerY += 1
    drawResource(playerX, oldY)
    drawResource(playerX, playerY)
    
#picks up the resource at the player's position.
def pickUp():
  global playerX, playerY
  rysowanie = True
  currentTile = world[playerX][playerY]
  # o ile gracz nie ma już zbyt wielu...
  if inventory[currentTile] < MAXTILES:
    # gracz ma o 1 sztukę zasobu więcej
    inventory[currentTile] += 1
    # gracz stoi na ziemi
    world[playerX][playerY] = DIRT
    # rysuj nowy blok ZIEMIA
    drawResource(playerX, playerY)
    # przerysuj ekwipunek dodając nowy zasób
    rysujEkwipunek()
    #rysujGracz()

# umieść zasób w obecnej pozycji gracza
def place(resource):
  print('placing: ', names[resource])
  # umieść TYLKO jeśli gracz ma zasób w ekwipunku
  if inventory[resource] > 0:
    # sprawdź na jakim zasobie znajduje się gracz
    currentTile = world[playerX][playerY]
    # podnieś zasób, na którym stoi gracz
    #(if it's not DIRT)
    if currentTile is not DIRT:
      inventory[currentTile] += 1
    # umieść wybrany zasób w bieżącej pozycji gracza
    world[playerX][playerY] = resource
    #add the new resource to the inventory
    inventory[resource] -= 1
    # zaktualizuj planszę (świat i ekwipunek)
    drawResource(playerX, playerY)
    rysujEkwipunek()
    #rysujGracz()
    print('   Placing', names[resource], 'complete')
  # ...a gdy już nic nie zostało...
  else:
    print('   You have no', names[resource], 'left')

# budowanie nowego zasobu
def craft(resource):
  print('Crafting: ', names[resource])
      # o ile zasób może być zbudowany...
  if resource in crafting:
    # sprawdza czy mamy odpowiednie zasoby
    #to craft this item
    canBeMade = True
    # dla każdego z wymaganych zasobów
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

# łączy wciśnięcie klawisza z funkcją „umieszczającą”
def bindPlacingKeys():
  for k in placekeys:
    screen.onkey(makeplace(k), placekeys[k])

#creates a function for crafting each resource
def makecraft(resource):
  return lambda: craft(resource)

# łączy wciśnięcie klawisza z funkcją „budującą”
def bindCraftingKeys():
  for k in craftkeys:
    screen.onkey(makecraft(k), craftkeys[k])

# rysuje zasób w pozycji (y, x)
def drawResource(y, x):
  #this variable stops other stuff being drawn
  global drawing
  #only draw if nothing else is being drawn
  if drawing == False:
    #something is now being drawn
    drawing = True
    # narysuj zasób w zadanej pozycji na mapie używając odpowiedniego obrazka
    rendererT.goto( (y * TILESIZE) + 20, height - (x * TILESIZE) - 20 )
    # rysuj blok używając odpowiedniej tekstury
    texture = textures[world[y][x]]
    rendererT.shape(texture)
    rendererT.stamp()
    if playerX == y and playerY == x:
      rendererT.shape(playerImg)
      rendererT.stamp()
    screen.update()
    # obecnie nic już się nie rysuje
    drawing = False
    
# rysuj świat
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
    # przykryj obecny ekwipunek prostokątem
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
    rendererT.color('czarny')
    # wyświetl tekst „wstaw” i „buduj”
    for i in range(1,num_rows+1):
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 20 - (i * 100))
      rendererT.write("wstaw")
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 40 - (i * 100))
      rendererT.write("buduj")
    #set the inventory position
    xPosition = 70
    yPostition = height - (MAPHEIGHT * TILESIZE) - 80
    itemNum = 0
    for i, item in enumerate(resources):
      # dodaj obrazek
      rendererT.goto(xPosition, yPostition)
      rendererT.shape(textures[item])
      rendererT.stamp()
      # dodaj numer do ekwipunku
      rendererT.goto(xPosition, yPostition - TILESIZE)
      rendererT.write(inventory[item])
      # dodaj klawisz wstawiania
      rendererT.goto(xPosition, yPostition - TILESIZE - 20)
      rendererT.write(placekeys[item])
      # dodaj klawisz do budowania
      if crafting.get(item) != None:
        rendererT.goto(xPosition, yPostition - TILESIZE - 40)
        rendererT.write(craftkeys[item])     
      # przesuń się, aby wstawić następny element ekwipunku
      xPosition += 50
      itemNum += 1
      # przesuń się do kolejnego wiersza po każdym 10 elemencie
      if itemNum % INVWIDTH == 0:
        xPosition = 70
        itemNum = 0
        yPostition -= TILESIZE + 80
    drawing = False

# wygeneruj instrukcje, w tym zasady tworzenia
def generateInstructions():
  instructions.append('Crafting rules:')
  # dla każdego zasobu, który można zbudować...
  for rule in crafting:
    # utwórz tekst dla reguły tworzenia
    craftrule = names[rule] + ' = '
    for resource, number in crafting[rule].items():
      craftrule += str(number) + ' ' + names[resource] + ' '
    # dodaj regułę tworzenia do 'instructions'
    instructions.append(craftrule)
  # wyświetl instrukcje
  yPos = height - 20
  for item in instructions:
    rendererT.goto( MAPWIDTH*TILESIZE + 40, yPos)
    rendererT.write(item)
    yPos-=20

# wygeneruj losowy świat
def generateRandomWorld():
  #loop through each row
  for row in range(MAPHEIGHT):
    # pętla po kolumnach każdego wiersza
    for column in range(MAPWIDTH):
      # losuj liczbę między 0, a 10
      randomNumber = random.randint(0,10)
      #WATER if the random number is a 1 or a 2
      if randomNumber in [1,2]:
        tile = WATER
      #GRASS if the random number is a 3 or a 4
      elif randomNumber in [3,4]:
        tile = GRASS
      #WOOD if it's a 5
      elif randomNumber == 5:
        tile = WOOD
      #SAND if it's a 6
      elif randomNumber == 6:
        tile = SAND
      #otherwise it's DIRT
      else:
        tile = DIRT
      # losuj pozycję na mapie
      world[column][row] = tile

#---
# kod zaczyna działać tutaj
#---

# importuj wymagane moduły i zmienne
import turtle
import random
from variables import *
from math import ceil

TILESIZE = 20
# liczba zasobów ekwipunku w wierszu
INVWIDTH = 8
drawing = False

#create a new 'screen' object
screen = turtle.Screen()
# oblicz szerokość i wysokość
width = (TILESIZE * MAPWIDTH) + max(200,INVWIDTH * 50)
num_rows = int(ceil((len(resources) / INVWIDTH)))
inventory_height =  num_rows * 120 + 40
height = (TILESIZE * MAPHEIGHT) + inventory_height

screen.setup(width, height)
screen.setworldcoordinates(0,0,width,height)
screen.bgcolor(BACKGROUNDCOLOUR)
screen.listen()

# zarejestruj obrazek gracza  
screen.register_shape(playerImg)
#register each of the resource images
for texture in textures.values():
  screen.register_shape(texture)

# utwórz kolejnego żółwia do rysowania grafiki
rendererT = turtle.Turtle()
rendererT.hideturtle()
rendererT.penup()
rendererT.speed(0)
rendererT.setheading(90)

# utwórz świat z losowanych zasobów
world = [ [DIRT for w in range(MAPHEIGHT)] for h in range(MAPWIDTH) ]

# przypisz klawisze ruchów i podnoszenia do odpowiednich funkcji
screen.onkey(moveUp, 'w')
screen.onkey(moveDown, 's')
screen.onkey(moveLeft, 'a')
screen.onkey(moveRight, 'd')
screen.onkey(pickUp, 'space')

# ustaw klawisze do umieszczania i tworzenia każdego zasobu
bindPlacingKeys()
bindCraftingKeys()

# te funkcje są zdefiniowane powyżej
generateRandomWorld()
drawWorld()
drawInventory()
generateInstructions()


