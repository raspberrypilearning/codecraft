#!/bin/python3

#############
# CodeCraft #
#############

#---
#Funkcije u igri
#---

#pomiče igrača 1 pločicu u lijevo.
def moveLeft():
  global playerX
  if(drawing == False and playerX > 0):
    oldX = playerX
    playerX -= 1
    drawResource(oldX, playerY)
    drawResource(playerX, playerY)
    
#pomiče igrača 1 pločicu u desno.
def moveRight():
  global playerX, MAPWIDTH
  if(drawing == False and playerX < MAPWIDTH - 1):
    oldX = playerX
    playerX += 1
    drawResource(oldX, playerY)
    drawResource(playerX, playerY)
    
#pomiče igrača 1 pločicu prema gore.
def moveUp():
  global playerY
  if(drawing == False and playerY > 0):
    oldY = playerY
    playerY -= 1
    drawResource(playerX, oldY)
    drawResource(playerX, playerY)
    
#pomiče igrača 1 pločicu prema dolje.
def moveDown():
  global playerY, MAPHEIGHT
  if(drawing == False and playerY < MAPHEIGHT - 1):
    oldY = playerY
    playerY += 1
    drawResource(playerX, oldY)
    drawResource(playerX, playerY)
    
#skuplja resurs na mjestu na kojem se igrač trenutno nalazi.
def pickUp():
  global playerX, playerY
  drawing = True
  currentTile = world[playerX][playerY]
  #ako korisnik već nema previše...
  if inventory[currentTile] < MAXTILES:
    #igrač sada ima još jedan resurs
    inventory[currentTile] += 1
    #the player is now standing on dirt
    world[playerX][playerY] = DIRT
    #nacrtaj novu pločicu ZEMLJA
    drawResource(playerX, playerY)
    #ponovno prikaži inventar s ekstra resursom.
    drawInventory()
    #drawPlayer()

#postavi resurs na trenutni položaj igrača
def place(resource):
  print('placing: ', names[resource])
  #postavi samo ako igrač već posjeduje resurs...
  if inventory[resource] > 0:
    #otkrijte resurs na trenutnoj poziciji igrača
    currentTile = world[playerX][playerY]
    #skupi resurs na kojemu igrač stoji
    #(ako nije ZEMLJA)
    if currentTile is not DIRT:
      inventory[currentTile] += 1
    #postavi resurs na igračev trenutni položaj
    world[playerX][playerY] = resource
    #dodaj novi resurs u inventar
    inventory[resource] -= 1
    #ažuriraj prikaz (svijet i inventar)
    drawResource(playerX, playerY)
    drawInventory()
    #drawPlayer()
    print('   Placing', names[resource], 'complete')
  #...a ako nije ostao niti jedan...
  else:
    print('   You have no', names[resource], 'left')

#stvori novi resurs
def craft(resource):
  print('Crafting: ', names[resource])
  #ako resurs može biti stvoren...
  if resource in crafting:
    #prati stanje o tome imamo li resurse
    #da stvorimo ovaj predmet
    canBeMade = True
    #za svaki predmet potreban za stvaranje resursa
    for i in crafting[resource]:
      #...ako nemamo dovoljno...
      if crafting[resource][i] > inventory[i]:
      #...ne možemo ga stvoriti!
        canBeMade = False
        break
    #ako ga možemo stvoriti (imamo sve potrebne resurse)
    if canBeMade == True:
      #uzmi pojedinčni predmet iz inventara
      for i in crafting[resource]:
        inventory[i] -= crafting[resource][i]
      #dodaj stvoreni predmet u inventar
      inventory[resource] += 1
      print('   Crafting', names[resource], 'complete')
    #...inače ako resurs ne može biti stvoren...
    else:
      print('   Ne može se stvoriti resurs:', names[resource])
    #ažuriraj prikazani inventar
    drawInventory()

#funkcija za postavljanje pojedinog resursa
def makeplace(resource):
  return lambda: place(resource)

#pridružuje funkciju za postavljanje s pripadajućom tipkom
def bindPlacingKeys():
  for k in placekeys:
    screen.onkey(makeplace(k), placekeys[k])

#stvara funkciju za stvaranje pojedinog resursa
def makecraft(resource):
  return lambda: craft(resource)

#pridružuje funkciju za stvaranje s pripadajućom tipkom
def bindCraftingKeys():
  for k in craftkeys:
    screen.onkey(makecraft(k), craftkeys[k])

#prikazuje resurs na poziciji (y,x)
def drawResource(y, x):
  #ova varijabla zaustavlja prikaz drugih stvari
  global drawing
  #samo crta ako se ništa drugo ne crta
  if drawing == False:
    #nešto se trenutno prikazuje
    drawing = True
    #nacrtaj resurs na položaju u mapi koristeći ispravnu sliku
    rendererT.goto( (y * TILESIZE) + 20, height - (x * TILESIZE) - 20 )
    #prikaži pločicu s ispravnom teksturom
    texture = textures[world[y][x]]
    rendererT.shape(texture)
    rendererT.stamp()
    if playerX == y and playerY == x:
      rendererT.shape(playerImg)
      rendererT.stamp()
    screen.update()
    #ništa se sada crta
    drawing = False
    
#crta mapu svijeta
def drawWorld():
  #ponavljaj za svaki redak
  for row in range(MAPHEIGHT):
    #ponavljaj za svaki stupac u retku
    for column in range(MAPWIDTH):
      #prikaži pločicu na trenutnoj poziciji
      drawResource(column, row)

#crta inventar na zaslonu
def drawInventory():
  #ova varijabla zaustavlja crtanje drugih stvari
  global drawing
  #samo crta ako se ništa drugo ne crta
  if drawing == False:
    #nešto se trenutno crta
    drawing = True
    #koristi pravokutnik za prekrivanje trenutnog inventara
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
    #prikaži tekst 'postavi' i 'izradi'
    for i in range(1,num_rows+1):
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 20 - (i * 100))
      rendererT.write("place")
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 40 - (i * 100))
      rendererT.write("craft")
    #postavi položaj inventara
    xPosition = 70
    yPostition = height - (MAPHEIGHT * TILESIZE) - 80
    itemNum = 0
    for i, item in enumerate(resources):
      #dodaj sliku
      rendererT.goto(xPosition, yPostition)
      rendererT.shape(textures[item])
      rendererT.stamp()
      #dodaj broj u inventar
      rendererT.goto(xPosition, yPostition - TILESIZE)
      rendererT.write(inventory[item])
      #dodaj tipku za postavljanje
      rendererT.goto(xPosition, yPostition - TILESIZE - 20)
      rendererT.write(placekeys[item])
      #dodaj tipku za stvaranje
      if crafting.get(item) != None:
        rendererT.goto(xPosition, yPostition - TILESIZE - 40)
        rendererT.write(craftkeys[item])     
      #pomakni se za postavljanje sljedećeg elementa u inventaru
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
      #WOOD if it's a 5
      elif randomNumber == 5:
        tile = WOOD
      #SAND if it's a 6
      elif randomNumber == 6:
        tile = SAND
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


