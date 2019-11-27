#!/bin/python3

#############
# CodeCraft #
#############

#---
# funkcje gry
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
    
# przesuń gracza o 1 pole w dół.
def moveDown():
  global playerY, MAPHEIGHT
  if(drawing == False and playerY < MAPHEIGHT - 1):
    oldY = playerY
    playerY += 1
    drawResource(playerX, oldY)
    drawResource(playerX, playerY)
    
# podnieś zasób z miejsca, w którym znajduje się gracz.
def pickUp():
  global playerX, playerY
  drawing = True
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
    drawInventory()
    #drawPlayer()

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
    # usuń zasób z ekwipunku
    inventory[resource] -= 1
    # zaktualizuj planszę (świat i ekwipunek)
    drawResource(playerX, playerY)
    drawInventory()
    #drawPlayer()
    print('     Umieszczanie', names[resource], 'zakończone')
  # ...a gdy już nic nie zostało...
  else:
            print('     Nie masz już więcej', names[resource])

# budowanie nowego zasobu
def craft(resource):
  print('Budowanie:', names[resource])
      # o ile zasób może być zbudowany...
  if resource in crafting:
    # sprawdza czy mamy odpowiednie zasoby
            # żeby zbudować nowy zasób
    canBeMade = True
            # dla każdego z wymaganych zasobów
    for i in crafting[resource]:
                  # ...jeśli mamy ich za mało...
      if crafting[resource][i] > inventory[i]:
                      # ...nie możemy budować!
        canBeMade = False
        break
            # jeśli możemy zbudować (czyli mamy wszystkie potrzebne zasoby)
    if canBeMade == True:
                  # weź odpowiednią ilość każdego z potrzebnych zasobów z ekwipunku
      for i in crafting[resource]:
        inventory[i] -= crafting[resource][i]
                  # dodaj zbudowany zasób do ekwipunku
      inventory[resource] += 1
      print('   Budowanie', names[resource], 'ukończone')
            # ...w przeciwnym razie nie da się zbudować nowego zasobu...
    else:
      print('   Nie można zbudować', names[resource])
            # zaktualizuje wyświetlany ekwipunek
    drawInventory()

# tworzy funkcję do umieszczania zasobu
def makeplace(resource):
  return lambda: place(resource)

# łączy wciśnięcie klawisza z funkcją „umieszczającą”
def bindPlacingKeys():
  for k in placekeys:
    screen.onkey(makeplace(k), placekeys[k])

# tworzy funkcję do budowania zasobu
def makecraft(resource):
  return lambda: craft(resource)

# łączy wciśnięcie klawisza z funkcją „budującą”
def bindCraftingKeys():
  for k in craftkeys:
    screen.onkey(makecraft(k), craftkeys[k])

# rysuje zasób w pozycji (y, x)
def drawResource(y, x):
      # ta zmienna wstrzymuje rysowanie innych elementów
  global drawing
      # rysuj tylko gdy nic innego nie jest obecnie rysowane
  if drawing == False:
    # coś się obecnie rysowane
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
      # pętla po wierszach
  for row in range(MAPHEIGHT):
            # pętla po kolumnach każdego wiersza
    for column in range(MAPWIDTH):
                  # rysuj blok w bieżącej pozycji
      drawResource(column, row)

# rysuj ekwipunek na ekranie
def drawInventory():
      # ta zmienna wstrzymuje rysowanie innych elementów
  global drawing
      # rysuj tylko gdy nic innego nie jest obecnie rysowane
  if drawing == False:
    # coś się obecnie rysowane
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
    rendererT.color('black')
    # wyświetl tekst „wstaw” i „buduj”
    for i in range(1,num_rows+1):
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 20 - (i * 100))
      rendererT.write("wstaw")
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 40 - (i * 100))
      rendererT.write("buduj")
            # ustaw pozycję ekwipunku
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
      # pętla po wierszach
  for row in range(MAPHEIGHT):
    # pętla po kolumnach każdego wiersza
    for column in range(MAPWIDTH):
      # losuj liczbę między 0, a 10
      randomNumber = random.randint(0,10)
      # WATER jeśli losowa liczba to 1 lub 2
      if randomNumber in [1,2]:
        tile = WATER
      # GRASS jeśli losowa liczba to 3 lub 4
      elif randomNumber in [3,4]:
        tile = GRASS
      # w pozostałych przypadkach to DIRT
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

# utwórz nowy obiekt „screen”
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


