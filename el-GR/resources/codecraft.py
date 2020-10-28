#!/bin/python3

#############
# CodeCraft #
#############

#---
#Λειτουργίες παιχνιδιού
#---

#μετακινεί τον παίκτη ένα τετράγωνο αριστερά.
def moveLeft():
  global playerX
  if(drawing == False and playerX > 0):
    oldX = playerX
    playerX -= 1
    drawResource(oldX, playerY)
    drawResource(playerX, playerY)
    
#μετακινεί τον παίκτη ένα τετράγωνο δεξιά.
def moveRight():
  global playerX, MAPWIDTH
  if(drawing == False and playerX < MAPWIDTH - 1):
    oldX = playerX
    playerX += 1
    drawResource(oldX, playerY)
    drawResource(playerX, playerY)
    
#μετακινεί τον παίκτη ένα τετράγωνο πάνω.
def moveUp():
  global playerY
  if(drawing == False and playerY > 0):
    oldY = playerY
    playerY -= 1
    drawResource(playerX, oldY)
    drawResource(playerX, playerY)
    
#μετακινεί τον παίκτη ένα τετράγωνο κάτω.
def moveDown():
  global playerY, MAPHEIGHT
  if(drawing == False and playerY < MAPHEIGHT - 1):
    oldY = playerY
    playerY += 1
    drawResource(playerX, oldY)
    drawResource(playerX, playerY)
    
#μαζεύει τον πόρο στη θέση που βρίσκεται ο παίκτης.
def pickUp():
  global playerX, playerY
  drawing = True
  currentTile = world[playerX][playerY]
  #αν ο χρήστης δεν έχει ήδη πολλά...
  if inventory[currentTile] < MAXTILES:
    #τώρα ο παίκτης έχει ένα ακόμη από αυτούς τους πόρους
    inventory[currentTile] += 1
    #ο παίκτης στέκεται σε λάσπη
    world[playerX][playerY] = DIRT
    #κάνε το εικονίδιο λάσπη
    drawResource(playerX, playerY)
    #ξαναζωγράφισε το απόθεμα με τον επιπλέον πόρο.
    drawInventory()
    #drawPlayer()

#τοποθετεί ένα πόρο στη θέση που είναι ο παίκτης
def place(resource):
  print('τοποθέτηση: ', names[resource])
  #τοποθετεί μόνο αν έχουν μείνει στον παίκτη...
  if inventory[resource] > 0:
    #βρίσκει τον πόρο που είναι στη θέση του παίκτη
    currentTile = world[playerX][playerY]
    #παίρνει τον πόρο στον οποίο στέκεται ο παίκτης
    #(αν δεν είναι λάσπη)
    if currentTile is not DIRT:
      inventory[currentTile] += 1
    #τοποθετεί τον πόρο στη θέση του παίκτη
    world[playerX][playerY] = resource
    #προσθέτει τον νέο πόρο στο απόθεμα
    inventory[resource] -= 1
    #ενημερώνει την οθόνη (τον κόσμο και το απόθεμα)
    drawResource(playerX, playerY)
    drawInventory()
    #drawPlayer()
    print('   Η τοποθέτηση', names[resource], 'ολοκληρώθηκε')
  #...και αν δεν έχουν μείνει...
  else:
    print('   Δεν έχει μείνει καθόλου', names[resource], '')

#Δημιουργεί έναν νέο πόρο
def craft(resource):
  print('Δημιουργία: ', names[resource])
  #αν ο πόρος μπορεί να δημιουργηθεί...
  if resource in crafting:
    #ελέγχει αν έχουμε τους πόρους
    #για να φτιάξουμε αυτό το αντικείμενο
    canBeMade = True
    #για κάθε αντικείμενο που χρειαζόμαστε για να φτιάξουμε τον πόρο
    for i in crafting[resource]:
      #...if we don't have enough...
      if crafting[resource][i] > inventory[i]:
      #...δεν μπορούμε να το φτιάξουμε!
        canBeMade = False
        break
    #αν μπορούμε να το φτιάξουμε (έχουμε όλους τους πόρους που χρειαζόμαστε)
    if canBeMade == True:
      #παίρνει τα αντικείμενα από το απόθεμα
      for i in crafting[resource]:
        inventory[i] -= crafting[resource][i]
      #προσθέτει το δημιουργημένο αντικείμενο στο απόθεμα
      inventory[resource] += 1
      print('   Δημιουργία', names[resource], 'ολοκληρώθηκε')
    #...ειδάλλως ο πόρος δεν μπορεί να δημιουργηθεί...
    else:
      print('   Δεν μπορεί να δημιουργηθεί', names[resource])
    #ενημερώνει το απόθεμα στην οθόνη
    drawInventory()

#δημιουργεί μία συνάρτηση για να τοποθετούμε κάθε πόρο
def makeplace(resource):
  return lambda: place(resource)

#αντιστοιχεί μία συνάρτηση "τοποθέτησης" σε κάθε πλήκτρο
def bindPlacingKeys():
  for k in placekeys:
    screen.onkey(makeplace(k), placekeys[k])

#δημιουργεί μία συνάρτηση για τη δημιουργία του κάθε πόρου
def makecraft(resource):
  return lambda: craft(resource)

#αντιστοιχεί μία συνάρτηση "δημιουργίας" σε κάθε πλήκτρο
def bindCraftingKeys():
  for k in craftkeys:
    screen.onkey(makecraft(k), craftkeys[k])

#ζωγραφίζει έναν πόρο στη θέση (y,x)
def drawResource(y, x):
  #this variable stops other stuff being drawn
  global drawing
  #ζωγραφίζει μόνο αν δεν ζωγραφίζεται τίποτε άλλο
  if drawing == False:
    #τώρα κάτι ζωγραφίζεται
    drawing = True
    #ζωγραφίζει τον πόρο σε εκείνο το σημείο, χρησιμοποιώντας τη σωστή εικόνα
    rendererT.goto( (y * TILESIZE) + 20, height - (x * TILESIZE) - 20 )
    #ζωγραφίζει με τη σωστή υφή
    texture = textures[world[y][x]]
    rendererT.shape(texture)
    rendererT.stamp()
    if playerX == y and playerY == x:
      rendererT.shape(playerImg)
      rendererT.stamp()
    screen.update()
    #τίποτε δεν ζωγραφίζεται πλέον
    drawing = False
    
#ζωγραφίζει τον χάρτη
def drawWorld():
  #επαναλαμβάνοντας τη σχεδίαση για κάθε γραμμή
  for row in range(MAPHEIGHT):
    #επαναλαμβάνοντας για κάθε στήλη
    for column in range(MAPWIDTH):
      #ζωγραφίζει το τετραγωνάκι στη συγκεκριμένη θέση
      drawResource(column, row)

#ζωγραφίζει το απόθεμα στην οθόνη
def drawInventory():
  #this variable stops other stuff being drawn
  global drawing
  #ζωγραφίζει μόνο αν δεν ζωγραφίζεται τίποτε άλλο
  if drawing == False:
    #τώρα κάτι ζωγραφίζεται
    drawing = True
    #χρησιμοποιεί ένα τετράπλευρο για να καλύψει το απόθεμα αυτή τη στιγμή
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
    #εμφανίζει το κείμενο "τοποθέτηση" και "δημιουργία"
    for i in range(1,num_rows+1):
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 20 - (i * 100))
      rendererT.write("τοποθέτηση")
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 40 - (i * 100))
      rendererT.write("δημιουργία")
    #ορίζει τη θέση του αποθέματος
    xPosition = 70
    yPostition = height - (MAPHEIGHT * TILESIZE) - 60
    itemNum = 0
    for i, item in enumerate(resources):
      #προσθέτει την εικόνα
      rendererT.goto(xPosition + 10, yPostition)
      rendererT.shape(textures[item])
      rendererT.stamp()
      #προσθέτει το νούμερο στο απόθεμα
      rendererT.goto(xPosition, yPostition - TILESIZE)
      rendererT.write(inventory[item])
      #add the name
      rendererT.goto(xPosition, yPostition - TILESIZE - 20)
      rendererT.write('[' + names[item] + ']')
      #προσθέτει το πλήκτρο τοποθέτησης
      rendererT.goto(xPosition, yPostition - TILESIZE - 40)
      rendererT.write(placekeys[item])
      #προσθέτει το πλήκτρο δημιουργίας
      if crafting.get(item) != None:
        rendererT.goto(xPosition, yPostition - TILESIZE - 60)
        rendererT.write(craftkeys[item])     
      #μεταφέρεται στο επόμενο αντικείμενο του αποθέματος
      xPosition += 50
      itemNum += 1
      #κάθε δέκα αντικείμενα, πηγαίνει στην επόμενη γραμμή
      if itemNum % INVWIDTH == 0:
        xPosition = 70
        itemNum = 0
        yPostition -= TILESIZE + 80
    drawing = False

#παράγει τις οδηγίες, όπως και τους κανόνες δημιουργίας
def generateInstructions():
  instructions.append('Κανόνες δημιουργίας:')
  #για κάθε πόρο που μπορεί να δημιουργηθεί...
  for rule in crafting:
    #δημιουργεί το κείμενο του κανόνα δημιουργίας
    craftrule = names[rule] + ' = '
    for resource, number in crafting[rule].items():
      craftrule += str(number) + ' ' + names[resource] + ' '
    #προσθέτει τον κανόνα δημιουργίας στις οδηγίες
    instructions.append(craftrule)
  #εμφανίζει τις οδηγίες
  yPos = height - 20
  for item in instructions:
    rendererT.goto( MAPWIDTH*TILESIZE + 40, yPos)
    rendererT.write(item)
    yPos-=20

#δημιουργεί ένα τυχαίο κόσμο
def generateRandomWorld():
  #επαναλαμβάνοντας τη σχεδίαση για κάθε γραμμή
  for row in range(MAPHEIGHT):
    #επαναλαμβάνοντας για κάθε στήλη
    for column in range(MAPWIDTH):
      #επιλέγει έναν τυχαίο αριθμό μεταξύ 0 και 10
      randomNumber = random.randint(0,10)
      #WATER (νερό) αν ο τυχαίος αριθμός είναι 1 ή 2
      if randomNumber in [1,2]:
        tile = WATER
      #GRASS (γρασίδι) αν ο τυχαίος αριθμός είναι 3 ή 4
      elif randomNumber in [3,4]:
        tile = GRASS
      #ειδάλλως είναι DIRT (λάσπη)
      else:
        tile = DIRT
      #τοποθετεί στη θέση του χάρτη το τυχαίο εικονίδιο
      world[column][row] = tile

#---
#Ο κώδικας αρχίζει να τρέχει εδώ
#---

#εισάγει τα modules και τις μεταβλητές που χρειάζονται
import turtle
import random
from variables import *
from math import ceil

TILESIZE = 20
# ο αριθμός των πόρων αποθέματος ανά σειρά
INVWIDTH = 8
drawing = False

#δημιουργεί ένα νέο αντικείμενο "οθόνης"
screen = turtle.Screen()
#υπολογίζει το πλάτος και το ύψος
width = (TILESIZE * MAPWIDTH) + max(200,INVWIDTH * 50)
num_rows = int(ceil((len(resources) / INVWIDTH)))
inventory_height =  num_rows * 120 + 40
height = (TILESIZE * MAPHEIGHT) + inventory_height

screen.setup(width, height)
screen.setworldcoordinates(0,0,width,height)
screen.bgcolor(BACKGROUNDCOLOUR)
screen.listen()

#καταγράφει την εικόνα του παίκτη  
screen.register_shape(playerImg)
#καταγράφει τις εικόνες των πόρων
for texture in textures.values():
  screen.register_shape(texture)

#δημιουργεί άλλο αντικείμενο της κλάσης turtle για να σχεδιάσει τα γραφικά
rendererT = turtle.Turtle()
rendererT.hideturtle()
rendererT.penup()
rendererT.speed(0)
rendererT.setheading(90)

#δημιουργεί έναν κόσμο τυχαίων πόρων.
world = [ [DIRT for w in range(MAPHEIGHT)] for h in range(MAPWIDTH) ]

#αντιστοιχεί τα πλήκτρα για μετακίνηση και λήψη πόρου με τις σωστές συναρτήσεις.
screen.onkey(moveUp, 'w')
screen.onkey(moveDown, 's')
screen.onkey(moveLeft, 'a')
screen.onkey(moveRight, 'd')
screen.onkey(pickUp, 'space')

#ρυθμίζει τα πλήκτρα για την τοποθέτηση και την δημιουργία κάθε πόρου
bindPlacingKeys()
bindCraftingKeys()

#αυτές οι συναρτήσεις ορίζονται παραπάνω
generateRandomWorld()
drawWorld()
drawInventory()
generateInstructions()
