#!/bin/python3

#############
# कोडक्राफ्ट #
#############

#---
#गेम फंक्शन
#---

#खिलाड़ी 1 टाइल बाएं जाता है।
def moveLeft():
  global playerX
  if(drawing == False and playerX > 0):
    oldX = playerX
    playerX -= 1
    drawResource(oldX, playerY)
    drawResource(playerX, playerY)
    
#खिलाड़ी 1 टाइल दाएं जाता है।
def moveRight():
  global playerX, MAPWIDTH
  if(drawing == False and playerX < MAPWIDTH - 1):
    oldX = playerX
    playerX += 1
    drawResource(oldX, playerY)
    drawResource(playerX, playerY)
    
#खिलाड़ी 1 टाइल ऊपर जाता है।
def moveUp():
  global playerY
  if(drawing == False and playerY > 0):
    oldY = playerY
    playerY -= 1
    drawResource(playerX, oldY)
    drawResource(playerX, playerY)
    
#खिलाड़ी 1 टाइल नीचे जाता है।
def moveDown():
  global playerY, MAPHEIGHT
  if(drawing == False and playerY < MAPHEIGHT - 1):
    oldY = playerY
    playerY += 1
    drawResource(playerX, oldY)
    drawResource(playerX, playerY)
    
#खिलाड़ी की स्थिति में संसाधन को उठाता है।
def pickUp():
  global playerX, playerY
  drawing = True
  currentTile = world[playerX][playerY]
  #यदि खिलाड़ी के पास पहले से बहुत अधिक संसाधन नहीं हैं...
  if inventory[currentTile] < MAXTILES:
    #खिलाड़ी के पास अब इस संसाधन 1 और है
    inventory[currentTile] += 1
    #खिलाड़ी अब गंदगी पर खड़ा है
    world[playerX][playerY] = DIRT
    #नई DIRT टाइल बनाइये
    drawResource(playerX, playerY)
    #अतिरिक्त संसाधन के साथ इन्वेंट्री फिरसे बनाइये।
    drawInventory()
    #drawPlayer()

#खिलाड़ी की वर्तमान स्थिति पर एक संसाधन रखिये
def place(resource):
  print('रखा जा रहा है: ', names[resource])
  #अगर खिलाड़ी के पास कुछ बचा है तो रखिये...
  if inventory[resource] > 0:
    #खिलाड़ी की वर्तमान स्थिति के संसाधन का पता लगाएं
    currentTile = world[playerX][playerY]
    #खिलाड़ी जिस संसाधन पर खड़ा है, उसे उठाएं
    #(यदि यह DIRT नहीं है)
    if currentTile is not DIRT:
      inventory[currentTile] += 1
    #खिलाड़ी की वर्तमान स्थिति में संसाधन रखें
    world[playerX][playerY] = resource
    #सूची में नए संसाधन जोड़ें
    inventory[resource] -= 1
    #प्रदर्शन अपडेट करें (दुनिया और सूची)
    drawResource(playerX, playerY)
    drawInventory()
    #drawPlayer()
    print('   रखना', names[resource], 'पूर्ण')
  #...और अगर उनके पास कुछ नहीं बचा...
  else:
    print('   आपके पास', names[resource], 'नहीं बचे हैं')

#नया संसाधन तैयार करें
def craft(resource):
  print('बन रहा है: ', names[resource])
  #अगर संसाधन तैयार किया जा सकता है...
  if resource in crafting:
    #हमारे पास संसाधन हैं या नहीं, इसका ध्यान रखता है
    #इस वस्तु को शिल्प करने के लिए
    canBeMade = True
    #संसाधन को शिल्प करने के लिए आवश्यक प्रत्येक वस्तु
    for i in crafting[resource]:
      #...अगर हमारे पास पर्याप्त नहीं है...
      if crafting[resource][i] > inventory[i]:
      #...हम इसे शिल्प नहीं कर सकते!
        canBeMade = False
        break
    #यदि हम इसे तैयार कर सकते हैं (हमारे पास सभी आवश्यक संसाधन हैं)
    if canBeMade == True:
      #इन्वेंट्री से प्रत्येक वस्तु ले
      for i in crafting[resource]:
        inventory[i] -= crafting[resource][i]
      #सूची में बनायीं गई वस्तु को जोड़ें
      inventory[resource] += 1
      print('   बनाना', names[resource], 'पूर्ण')
    #...अन्यथा संसाधन को तैयार नहीं किया जा सकता है...
    else:
      print('   शिल्प नहीं किया जा सकता', names[resource])
    #प्रदर्शित सूची को अद्यतन करें
    drawInventory()

#प्रत्येक संसाधन रखने के लिए एक फंक्शन बनाता है
def makeplace(resource):
  return lambda: place(resource)

#प्रत्येक कुंजी प्रेस के लिए एक 'placing' फ़ंक्शन देता है
def bindPlacingKeys():
  for k in placekeys:
    screen.onkey(makeplace(k), placekeys[k])

#प्रत्येक संसाधन बनाने के लिए एक फंक्शन बनाता है
def makecraft(resource):
  return lambda: craft(resource)

#प्रत्येक कुंजी प्रेस के लिए एक 'crafting' फ़ंक्शन देता है
def bindCraftingKeys():
  for k in craftkeys:
    screen.onkey(makecraft(k), craftkeys[k])

#(y, x) स्थिति में एक संसाधन बनाता है
def drawResource(y, x):
  #यह वेरियबल अन्य सामान को बनाना बंद कर देता है
  global drawing
  #केवल तभी बनाएं जब कुछ और नहीं बनाया जा रहा है
  if drawing == False:
    #अब कुछ बनाया जा रहा है
    drawing = True
    #सही छवि का उपयोग करके, टिलेमैप में उस स्थिति में संसाधन निकालें
    rendererT.goto( (y * TILESIZE) + 20, height - (x * TILESIZE) - 20 )
    #सही बनावट के साथ टाइल बनाएं
    texture = textures[world[y][x]]
    rendererT.shape(texture)
    rendererT.stamp()
    if playerX == y and playerY == x:
      rendererT.shape(playerImg)
      rendererT.stamp()
    screen.update()
    #अब कुछ नहीं बनाया जा रहा है
    drawing = False
    
#दुनिया का नक्शा बनाता है
def drawWorld():
  #लूप करें प्रत्येक पंक्ति के माध्यम से
  for row in range(MAPHEIGHT):
    #लूप करें पंक्ति में प्रत्येक स्तंभ को
    for column in range(MAPWIDTH):
      #वर्तमान स्थिति पर टाइल बनाएं
      drawResource(column, row)

#स्क्रीन पर इन्वेंट्री को बनाएं
def drawInventory():
  #यह वेरियबल अन्य सामान को बनाना बंद कर देता है
  global drawing
  #केवल तभी बनाएं जब कुछ और नहीं बनाया जा रहा है
  if drawing == False:
    #अब कुछ बनाया जा रहा है
    drawing = True
    #वर्तमान सूची को ढकने के लिए एक आयत का इस्तेमाल करें
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
    #'जगह' और 'शिल्प' पाठ प्रदर्शित करें
    for i in range(1,num_rows+1):
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 20 - (i * 100))
      rendererT.write("place")
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 40 - (i * 100))
      rendererT.write("craft")
    #सूची की स्थिति निर्धारित करें
    xPosition = 70
    yPostition = height - (MAPHEIGHT * TILESIZE) - 60
    itemNum = 0
    for i, item in enumerate(resources):
      #छवि जोड़ें
      rendererT.goto(xPosition + 10, yPostition)
      rendererT.shape(textures[item])
      rendererT.stamp()
      #इन्वेंट्री में संख्या जोड़ें
      rendererT.goto(xPosition, yPostition - TILESIZE)
      rendererT.write(inventory[item])
      #नाम जोड़ें
      rendererT.goto(xPosition, yPostition - TILESIZE - 20)
      rendererT.write('[' + names[item] + ']')
      #जगह की कुंजी जोड़ें
      rendererT.goto(xPosition, yPostition - TILESIZE - 40)
      rendererT.write(placekeys[item])
      #शिल्प की कुंजी जोड़ें
      if crafting.get(item) != None:
        rendererT.goto(xPosition, yPostition - TILESIZE - 60)
        rendererT.write(craftkeys[item])     
      #अगली इन्वेंट्री आइटम रखने के लिए आगे बढे
      xPosition += 50
      itemNum += 1
      #हर 10 आइटम पर अगली पंक्ति पर जाएं
      if itemNum % INVWIDTH == 0:
        xPosition = 70
        itemNum = 0
        yPostition -= TILESIZE + 80
    drawing = False

#निर्देशों को तैयार करें, जिसमें क्राफ्टिंग नियम भी शामिल हैं
def generateInstructions():
  instructions.append('बनाने के निर्देश:')
  #प्रत्येक संसाधन के लिए जिसे तैयार किया जा सकता है
  for rule in crafting:
    #क्राफ्टिंग नियम पाठ को बनाएँ
    craftrule = names[rule] + ' = '
    for resource, number in crafting[rule].items():
      craftrule += str(number) + ' ' + names[resource] + ' '
    #क्राफ्टिंग नियम को निर्देशों में शामिल करें
    instructions.append(craftrule)
  #निर्देशों को प्रदर्शित करें
  yPos = height - 20
  for item in instructions:
    rendererT.goto( MAPWIDTH*TILESIZE + 40, yPos)
    rendererT.write(item)
    yPos-=20

#एक यादृच्छिक दुनिया का उत्पन्न करें
def generateRandomWorld():
  #लूप करें प्रत्येक पंक्ति के माध्यम से
  for row in range(MAPHEIGHT):
    #लूप करें पंक्ति में प्रत्येक स्तंभ को
    for column in range(MAPWIDTH):
      #0 और 10 के बीच एक यादृच्छिक संख्या चुनें
      randomNumber = random.randint(0,10)
      #WATER यदि यादृच्छिक संख्या 1 या 2 है
      if randomNumber in [1,2]:
        tile = WATER
      #GRASS यदि यादृच्छिक संख्या 3 या 4 है
      elif randomNumber in [3,4]:
        tile = GRASS
      #WOOD अगर यह एक 5 है
      elif randomNumber == 5:
        tile = WOOD
      #SAND अगर यह एक 6 है
      elif randomNumber == 6:
        tile = SAND
      #अन्यथा यह है DIRT
      else:
        tile = DIRT
      #बेतरतीब ढंग से चुनी गई टाइल के लिए टीलमैप में स्थिति सेट करें
      world[column][row] = tile

#---
#कोड यहां चलने लगता है
#---

#आयात कीजिये जरूरी मॉड्यूल और वेरिएबल को
import turtle
import random
from variables import *
from math import ceil

TILESIZE = 20
#प्रति पंक्ति इन्वेंट्री संसाधनों की संख्या
INVWIDTH = 8
drawing = False

#नया 'screen' ऑब्जेक्ट बनाएँ
screen = turtle.Screen()
#चौड़ाई और ऊंचाई की गणना करें
width = (TILESIZE * MAPWIDTH) + max(200,INVWIDTH * 50)
num_rows = int(ceil((len(resources) / INVWIDTH)))
inventory_height =  num_rows * 120 + 40
height = (TILESIZE * MAPHEIGHT) + inventory_height

screen.setup(width, height)
screen.setworldcoordinates(0,0,width,height)
screen.bgcolor(BACKGROUNDCOLOUR)
screen.listen()

#खिलाड़ी की छवि को रजिस्टर करें  
screen.register_shape(playerImg)
#हर संसाधन छवि को रजिस्टर करें
for texture in textures.values():
  screen.register_shape(texture)

#ड्राइंग बनाने के लिए एक और turtle बनाएँ
rendererT = turtle.Turtle()
rendererT.hideturtle()
rendererT.penup()
rendererT.speed(0)
rendererT.setheading(90)

#यादृच्छिक संसाधनों की एक दुनिया बनाएँ।
world = [ [DIRT for w in range(MAPHEIGHT)] for h in range(MAPWIDTH) ]

#आगे बढ़ने और लेने के लिए सही फंक्शन के लिए कुंजियाँ चुनें।
screen.onkey(moveUp, 'w')
screen.onkey(moveDown, 's')
screen.onkey(moveLeft, 'a')
screen.onkey(moveRight, 'd')
screen.onkey(pickUp, 'space')

#प्रत्येक संसाधन को रखने और तैयार करने के लिए कुंजियों को चुनें
bindPlacingKeys()
bindCraftingKeys()

#ये फंक्शन ऊपर परिभाषित किया गए हैं
generateRandomWorld()
drawWorld()
drawInventory()
generateInstructions()


