#!/bin/python3

#############
# CodeCraft #
#############

#---
#Spelfuncties
#---

#beweegt speler 1 tegel naar links.
def beweegLinks():
  global spelerX
  if(drawing == False and playerX > 0):
    oldX = playerX
    spelerX -= 1
    drawResource(oldX, playerY)
    tekenBron(spelerX, spelerY)
    
#beweegt speler 1 tegel naar rechts.
def beweegRechts():
  global spelerX, KAARTBREEDTE
  if(drawing == False and playerX < MAPWIDTH - 1):
    oldX = playerX
    spelerX += 1
    drawResource(oldX, playerY)
    tekenBron(spelerX, spelerY)
    
#beweegt speler 1 tegel naar boven.
def beweegBoven():
  global spelerY
  if(drawing == False and playerY > 0):
    oldY = playerY
    spelerY -= 1
    drawResource(playerX, oldY)
    tekenBron(spelerX, spelerY)
    
#beweegt speler 1 tegel naar onder.
def beweegOnder():
  global spelerY, KAARTHOOGTE
  if(drawing == False and playerY < MAPHEIGHT - 1):
    oldY = playerY
    spelerY += 1
    drawResource(playerX, oldY)
    tekenBron(spelerX, spelerY)
    
#pakt de bron op, op de positie van de speler.
def pakOp():
  global spelerX, spelerY
  tekenen = True
  dezeTegel = wereld[spelerX][spelerY]
  #als de speler er al niet teveel heeft...
  if inventaris[dezeTegel] < MAXTEGELS:
    #speler heeft nu 1 of meer van deze bron
    inventaris[dezeTegel] += 1
    #de speler staat nu op Vuil
    wereld[spelerX][spelerY] = VUIL
    #teken de volgende VUIL tegel
    tekenBron(spelerX, spelerY)
    #herteken de inventaris met de extra bron.
    tekenInventaris()
    #tekenSpeler()

#plaats een bron op de positie van de speler
def plaats(bron):
  print('plaatsen: ', namen[bron])
  #alleen plaatsen als de speler nog wat over heeft...
  if inventaris[bron] > 0:
    #wat is de bron op de positie van de speler
    dezeTegel = wereld[spelerX][spelerY]
    #pak de bron waarop de speler staat
    #(als het niet VUIL is)
    if dezeTegel is not VUIL:
      inventaris[dezeTegel] += 1
    #plaats de bron op de positie van de speler
    wereld[spelerX][spelerY] = bron
    #voeg de nieuwe bron toe aan de inventaris
    inventaris[bron] -= 1
    #vernieuw het scherm (wereld en inventaris)
    tekenBron(spelerX, spelerY)
    tekenInventaris()
    #tekenSpeler()
    print('   Plaatsen', namen[bron], 'klaar')
  #...en als er niks over is...
  else:
    print('   Je hebt geen', namen[bron], 'over')

#maak een nieuwe bron
def maak(bron):
  print('maken: ', namen[bron])
  #als de bron kan worden gemaakt...
  if bron in maken:
    #hou bij of we de bronnen hebben
    #om dit item te kunnen maken
    kanGemaaktWorden = True
    #voor elke item dat we nodig hebben om de bron te maken
    for i in maken[bron]:
      #...als we niet genoeg hebben...
      if maken[bron][i] > inventaris[i]:
      #...kunnen we het niet maken!
        kanGemaaktWorden = False
        break
    #als we het kunnen maken (we hebben alle bronnen)
    if kanGemaaktWorden == True:
      #neem elk item van de inventaris
      for i in maken[bron]:
        inventaris[i] -= maken[bron][i]
      #voeg het gemaakte item toe aan de inventaris
      inventaris[bron] += 1
      print('   maken', namen[bron], 'klaar')
    #...anders kan de bron niet worden gemaakt...
    else:
      print('   Kan', namen[bron],'niet maken')
    #vernieuw de inventaris op het scherm
    tekenInventaris()

#maakt een functie om elke bron te plaatsen
def maakplaats(bron):
  return lambda: plaats(bron)

#verbind een 'plaats'functie aan elke ingedrukte toe
def verbindPlaatsToetsen():
  for k in plaatstoetsen:
    scherm.onkey(maakplaats(k), plaatstoetsen[k])

#maak een functie voor het maken van elke bron
def maakmaak(bron):
  return lambda: maak(bron)

#verbindt een 'maak'functie aan elke ingedrukte toets
def verbindMaakToetsen():
  for k in maaktoetsen:
    scherm.onkey(maakmaak(k), maaktoetsen[k])

#teken bron op positie (y,x)
def tekenBron(y, x):
  #Deze variabele stopt alle dingen die getekend worden
  global tekenen
  teken alleen als er niks anders wordt getekend
  if tekenen == False:
    #er wordt nu iets getekend
    tekenen = True
    #teken de bron op de positie op de tegelkaart, met het goede plaatje erbij
    rendererT.goto( (y * TEGELGROOTTE) + 20, hoogte - (x * TEGELGROOTTE) - 20 )
    #teken de tegel met het juiste materiaal
    materiaal = materialen[wereld[y][x]]
    rendererT.shape(materiaal)
    rendererT.stamp()
    if playerX == y and playerY == x:
      rendererT.shape(playerImg)
      rendererT.stamp()
    scherm.update()
    #er wordt niets getekend
    tekenen = False
    
#teken de wereldkaart
def tekenWereld():
  #doorloop elke rij
  for rij in range(KAARTHOOGTE):
    #doorloop elke kolom in de rij
    for kolom in range(KAARTBREEDTE):
      #teken de tegel op de huidige positie
      tekenBron(kolom, rij)

#tekent de inventaris op het scherm
def tekenInventaris():
  #Deze variabele stopt alle dingen die getekend worden
  global tekenen
  teken alleen als er niks anders wordt getekend
  if tekenen == False:
    #er wordt nu iets getekend
    tekenen = True
    #gebruik een rechthoek voor de inventaris
    rendererT.color(ACHTERGRONDKLEUR)
    rendererT.goto(0,0)
    rendererT.begin_fill()
    #rendererT.setheading(0)
    for i in range(2):
      rendererT.forward(inventaris_hoogte - 60)
      rendererT.right(90)
      rendererT.forward(breedte)
      rendererT.right(90)
    rendererT.end_fill()
    rendererT.color('black')
    #laat 'plaats' en 'maak' tekst zien
    for i in range(1,num_rijen+1):
      rendererT.goto(20, (hoogte - (KAARTHOOGTE * TEGELGROOTTE)) - 20 - (i * 100))
      rendererT.write("plaats")
      rendererT.goto(20, (hoogte - (KAARTHOOGTE * TEGELGROOTTE)) - 40 - (i * 100))
      rendererT.write("maak")
    #bepaal de positie van de inventaris
    xPositie = 70
    yPostition = height - (MAPHEIGHT * TILESIZE) - 60
    itemNum = 0
    for i, item in enumerate(bronnen):
      #voeg de afbeelding toe
      rendererT.goto(xPosition + 10, yPostition)
      rendererT.shape(materialen[item])
      rendererT.stamp()
      #voeg het nummer in de inventaris toe
      rendererT.goto(xPositie, yPositie - TEGELGROOTTE)
      rendererT.write(inventaris[item])
      #add the name
      rendererT.goto(xPositie, yPositie - TEGELGROOTTE - 20)
      rendererT.write('[' + names[item] + ']')
      #voeg 'plaats'toets toe
      rendererT.goto(xPositie, yPostitie - TEGELGROOTTE - 40)
      rendererT.write(plaatstoetsen[item])
      #voeg 'maak'toets toe
      if maken.get(item) != None:
        rendererT.goto(xPosition, yPostition - TILESIZE - 60)
        rendererT.write(maaktoetsen[item])     
      #ga door naar het volgende inventaris item
      xPositie += 50
      itemNum += 1
      #ga naar de volgende rij na elke 10 items
      if itemNum % INVbreedte == 0:
        xPositie = 70
        itemNum = 0
        yPositie -= TEGELGROOTTE + 80
    tekenen = False

#genereer de instructies, inclusief de maakregels
def genereerInstructies():
  instructies.append('maakregels:')
  #voor elke bron die kan worden gemaakt...
  for regel in maken:
    #maak de maakregeltekst
    maakregel = namen[regel] + ' = '
    for bron, nummer in maken[regel].items():
      maakregel += str(nummer) + ' ' + namen[bron] + ' '
    #voeg maakregel toe aan de instructies
    instructies.append(maakregel)
  #laat de instructies zien
  yPos = hoogte - 20
  for item in instructies:
    rendererT.goto( KAARTBREEDTE*TEGELGROOTTE + 40, yPos)
    rendererT.write(item)
    yPos-=20

#genereer een willekeurige wereld
def genereerWillekeurigeWereld():
  #doorloop elke rij
  for rij in range(KAARTHOOGTE):
    #doorloop elke kolom in de rij
    for kolom in range(KAARTBREEDTE):
      #neem een willekeurig getal tussen 0 en 10
      willekeurigGetal = random.randint(0,10)
      #WATER als het willekeurige getal 1 of 2 is
      if willekeurigGetal in [1,2]:
        tegel = WATER
      #GRAS als het een 3 of een 4 is
      elif willekeurigGetal in [3,4]:
        tegel = GRAS
      #anders is het VUIL
      else:
        tegel = VUIL
      #maak de positie in op de tegelkaart een willekeurig gekozen tegel
      wereld[kolom][rij] = tegel

#---
#Het programma begint hier
#---

#importeer de benodigde modules en variables
import turtle
import random
from variables import *
from math import ceil

TEGELGROOTTE = 20
#het aantal inventarisbronnen per rij
INVbreedte = 8
tekenen = False

#maak een nieuw spelerobject
scherm = turtle.Screen()
#bereken breedte hoogte
breedte = (TEGELGROOTTE * KAARTBREEDTE) + max(200,INVbreedte * 50)
num_rijen = int(ceil((len(bronnen) / INVbreedte)))
inventaris_hoogte =  num_rijen * 120 + 40
hoogte = (TEGELGROOTTE * KAARTHOOGTE) + inventaris_hoogte

scherm.setup(breedte, hoogte)
scherm.setworldcoordinates(0,0,breedte,hoogte)
scherm.bgcolor(ACHTERGRONDKLEUR)
scherm.listen()

#registreer de spelersafbeelding  
scherm.register_shape(spelerImg)
#registreer alle bronafbeeldingen
for materiaal in materialen.values():
  scherm.register_shape(materiaal)

#maak een nieuwe turtle (schildpad) om te tekenen
rendererT = turtle.Turtle()
rendererT.hideturtle()
rendererT.penup()
rendererT.speed(0)
rendererT.setheading(90)

#maak een wereld met willekeurige bronnen.
wereld = [ [VUIL for w in range(KAARTHOOGTE)] for h in range(KAARTBREEDTE) ]

#laat de toetsen zien voor de voortbeweging en het oppakken.
scherm.onkey(beweegBoven, 'w')
scherm.onkey(beweegOnder, 's')
scherm.onkey(beweegLinks, 'a')
scherm.onkey(beweegRechts, 'd')
scherm.onkey(pakOp, 'space')

#installeren van de toetsen voor plaatsen en maken van elke bron
verbindPlaatsToetsen()
verbindMaakToetsen()

#deze functies worden hierboven gedefinieerd
genereerWillekeurigeWereld()
tekenWereld()
tekenInventaris()
genereerInstructies()
