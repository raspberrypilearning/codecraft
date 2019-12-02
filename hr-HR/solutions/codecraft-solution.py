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
      #spusti se u sljedeći red svakih 10 stavki
      if itemNum % INVWIDTH == 0:
        xPosition = 70
        itemNum = 0
        yPostition -= TILESIZE + 80
    drawing = False

#generira upute, uključujući i pravila za stvaranje resursa
def generateInstructions():
  instructions.append('Pravila stvaranja:')
  #za svaki resurs koji se može stvoriti...
  for rule in crafting:
    #stvori tekst pravila za stvaranje
    craftrule = names[rule] + ' = '
    for resource, number in crafting[rule].items():
      craftrule += str(number) + ' ' + names[resource] + ' '
    #dodajte pravilo za stvaranje uputama
    instructions.append(craftrule)
  #prikaži upute
  yPos = height - 20
  for item in instructions:
    rendererT.goto( MAPWIDTH*TILESIZE + 40, yPos)
    rendererT.write(item)
    yPos-=20

#generira nasumični svijet
def generateRandomWorld():
  #ponavljaj za svaki redak
  for row in range(MAPHEIGHT):
    #ponavljaj za svaki stupac u retku
    for column in range(MAPWIDTH):
      #odaberi nasumičan broj između 0 i 10
      randomNumber = random.randint(0,10)
      #VODA ako je nasumičan broj 1 ili 2
      if randomNumber in [1,2]:
        tile = WATER
      #TRAVA ako je nasumičan broj 3 ili 4
      elif randomNumber in [3,4]:
        tile = GRASS
      #DRVO ako je 5
      elif randomNumber == 5:
        tile = WOOD
      #PIJESAK ako je 6
      elif randomNumber == 6:
        tile = SAND
      #inače je ZEMLJA
      else:
        tile = DIRT
      #dodaj položaj nasumično odabrane pločice na mapu
      world[column][row] = tile

#---
#Kod se počinje izvršavati ovdje
#---

#uvezi potrebne module i varijable
import turtle
import random
from variables import *
from math import ceil

TILESIZE = 20
#broj resursa u inventaru po retku
INVWIDTH = 8
drawing = False

#stvori novi objekt 'zaslon'
screen = turtle.Screen()
#izračunaj širinu i visinu
width = (TILESIZE * MAPWIDTH) + max(200,INVWIDTH * 50)
num_rows = int(ceil((len(resources) / INVWIDTH)))
inventory_height =  num_rows * 120 + 40
height = (TILESIZE * MAPHEIGHT) + inventory_height

screen.setup(width, height)
screen.setworldcoordinates(0,0,width,height)
screen.bgcolor(BACKGROUNDCOLOUR)
screen.listen()

#registriraj sliku igrača  
screen.register_shape(playerImg)
#registriraj sliku pojedinog resursa
for texture in textures.values():
  screen.register_shape(texture)

#stvori još jednu kornjaču za prikaz crteža
rendererT = turtle.Turtle()
rendererT.hideturtle()
rendererT.penup()
rendererT.speed(0)
rendererT.setheading(90)

#stvori svijet od nasumično odabranih resursa.
world = [ [DIRT for w in range(MAPHEIGHT)] for h in range(MAPWIDTH) ]

#poveži tipke za kretanje i skupljanje s ispravnim funkcijama.
screen.onkey(moveUp, 'w')
screen.onkey(moveDown, 's')
screen.onkey(moveLeft, 'a')
screen.onkey(moveRight, 'd')
screen.onkey(pickUp, 'space')

#postavi tipke za postavljanje i izradu svakog resursa
bindPlacingKeys()
bindCraftingKeys()

#ovo su funkcije koje su definirane iznad
generateRandomWorld()
drawWorld()
drawInventory()
generateInstructions()


