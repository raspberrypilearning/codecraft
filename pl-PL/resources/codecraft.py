#!/bin/python3

#############
# CodeCraft #
#############

#---
# funkcje gry
#---

# przesuń gracza o 1 pole w lewo.
def przesunLewo():
  global graczX
  if(rysowanie == False and graczX > 0):
    staryX = graczX
    graczX -= 1
    rysujZasob(staryX, graczY)
    rysujZasob(graczX, graczY)
    
# przesuń gracza o 1 pole w prawo.
def przesunPrawo():
  global graczX, SZEROKOSCMAPY
  if(rysowanie == False and graczX < SZEROKOSCMAPY - 1):
    staryX = graczX
    graczX += 1
    rysujZasob(staryX, graczY)
    rysujZasob(graczX, graczY)
    
# przesuń gracza o 1 pole do góry.
def przesunGora():
  global graczY
  if(rysowanie == False and graczY > 0):
    staryY = graczY
    graczY -= 1
    rysujZasob(graczX, staryY)
    rysujZasob(graczX, graczY)
    
# przesuń gracza o 1 pole w dół.
def przesunDol():
  global graczY, WYSOKOSCMAPY
  if(rysowanie == False and graczY < WYSOKOSCMAPY - 1):
    staryY = graczY
    graczY += 1
    rysujZasob(graczX, staryY)
    rysujZasob(graczX, graczY)
    
# podnieś zasób z miejsca, w którym znajduje się gracz.
def podnies():
  global graczX, graczY
  rysowanie = True
  aktualnyKlocek = swiat[graczX][graczY]
  # o ile gracz nie ma już zbyt wielu...
  if ekwipunek[aktualnyKlocek] < LIMITZASOBOW:
    # gracz ma o 1 sztukę zasobu więcej
    ekwipunek[aktualnyKlocek] += 1
    # gracz stoi na ziemi
    swiat[graczX][graczY] = ZIEMIA
    # rysuj nowy blok ZIEMIA
    rysujZasob(graczX, graczY)
    # przerysuj ekwipunek dodając nowy zasób
    rysujEkwipunek()
    #rysujGracz()

# umieść zasób w obecnej pozycji gracza
def miejsce(zasob):
  print('umieszczanie: ', nazwy[zasob])
  # umieść TYLKO jeśli gracz ma zasób w ekwipunku
  if ekwipunek[zasob] > 0:
    # sprawdź na jakim zasobie znajduje się gracz
    aktualnyKlocek = swiat[graczX][graczY]
    # podnieś zasób, na którym stoi gracz
    # (jeśli to nie jest ZIEMIA)
    if aktualnyKlocek nie jest ZIEMIA:
      ekwipunek[aktualnyKlocek] += 1
    # umieść wybrany zasób w bieżącej pozycji gracza
    swiat[graczX][graczY] = zasob
    # usuń zasób z ekwipunku
    ekwipunek[zasob] -= 1
    # zaktualizuj planszę (świat i ekwipunek)
    rysujZasob(graczX, graczY)
    rysujEkwipunek()
    #rysujGracz()
    print('     Umieszczanie', nazwy[zasob], 'zakończone')
  # ...a gdy już nic nie zostało...
  else:
    print('     Nie masz już więcej', nazwy[zasob])

# budowanie nowego zasobu
def budowanie(zasob):
  print('Budowanie:', nazwy[zasob])
      # o ile zasób może być zbudowany...
  if zasob in budowanie:
    # sprawdza czy mamy odpowiednie zasoby
            # żeby zbudować nowy zasób
    mozeBycUtworzony = True
            # dla każdego z wymaganych zasobów
    for i in budowanie[zasob]:
                  # ...jeśli mamy ich za mało...
      if budowanie[zasob][i] > ekwipunek[i]:
                      # ...nie możemy budować!
        mozeBycUtworzony = False
        break
            # jeśli możemy zbudować (czyli mamy wszystkie potrzebne zasoby)
    if mozeBycUtworzony == True:
                  # weź odpowiednią ilość każdego z potrzebnych zasobów z ekwipunku
      for i in budowanie[zasob]:
        ekwipunek[i] -= budowanie[zasob][i]
                  # dodaj zbudowany zasób do ekwipunku
      ekwipunek[zasob] += 1
      print('   Budowanie', nazwy[zasob], 'ukończone')
            # ...w przeciwnym razie nie da się zbudować nowego zasobu...
    else:
      print('   Nie można zbudować', nazwy[zasob])
            # zaktualizuje wyświetlany ekwipunek
    rysujEkwipunek()

# tworzy funkcję do umieszczania zasobu
def miejscetworzenia(zasob):
  return lambda: miejsce(zasob)

# łączy wciśnięcie klawisza z funkcją „umieszczającą”
def polaczKlawiszeUmieszczania():
  for k in klawiszeumieszczania:
    screen.onkey(miejscetworzenia(k), klawiszeumieszczania[k])

# tworzy funkcję do budowania zasobu
def tworzenie(zasob):
  return lambda: utworz(zasob)

# łączy wciśnięcie klawisza z funkcją „budującą”
def polaczKlawiszeTworzenia():
  for k in klawiszetworzenia:
    screen.onkey(tworzenie(k), klawiszetworzenia[k])

# rysuje zasób w pozycji (y, x)
def rysujZasob(y, x):
      # ta zmienna wstrzymuje rysowanie innych elementów
  global rysowanie
      # rysuj tylko gdy nic innego nie jest obecnie rysowane
  if rysowanie == False:
    #something is now being drawn
    rysowanie = True
    #draw the resource at that position in the tilemap, using the correct image
    rendererT.goto( (y * ROZMIARKLOCKA) + 20, height - (x * ROZMIARKLOCKA) - 20 )
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


