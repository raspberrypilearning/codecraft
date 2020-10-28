#!/bin/python3

#############
# CodeCraft #
#############

#---
#Funktionen des Spiels
#---

#bewege den Spieler um ein Feld nach links.
def nachLinksBewegen():
  global spielerX
  if(drawing == False and playerX > 0):
    oldX = playerX
    spielerX -=1
    drawResource(oldX, playerY)
    zeichneRessource(spielerX, spielerY)
    
#bewege den Spieler um ein Feld nach rechts.
def nachRechtsBewegen():
  global spielerX, WELTBREITE
  if(drawing == False and playerX < MAPWIDTH - 1):
    oldX = playerX
    spielerX += 1
    drawResource(oldX, playerY)
    zeichneRessource(spielerX, spielerY)
    
#bewege den Spieler um ein Feld nach oben.
def nachObenBewegen():
  global spielerY
  if(drawing == False and playerY > 0):
    oldY = playerY
    spielerY -= 1
    drawResource(playerX, oldY)
    zeichneRessource(spielerX, spielerY)
    
#bewege den Spieler um ein Feld nach unten.
def nachUntenBewegen():
  global spielerY, WELTHOEHE
  if(drawing == False and playerY < MAPHEIGHT - 1):
    oldY = playerY
    spielerY += 1
    drawResource(playerX, oldY)
    zeichneRessource(spielerX, spielerY)
    
#nimm die Ressource an der Spieler-Position auf.
def nehmen():
  global spielerX, spielerY
  binAmZeichnen = True
  aktuellesFeld = welt[spielerX][spielerY]
  #sofern der Nutzer nicht bereits zu viele davon hat...
  if inventar[aktuellesFeld] < MAXELEMENTE:
    #der Spieler besitzt von dieser Ressource nun ein Element mehr
    inventar[aktuellesFeld] += 1
    #der Spieler steht nun auf Erde
    welt[spielerX][spielerY] = ERDE
    #neues ERDE Feld zeichnen
    zeichneRessource(spielerX, spielerY)
    #Inventar mit zusätzlicher Ressource neu zeichnen.
    zeichneInventar()
    #zeichneSpieler()

# Platziere eine Ressource an der aktuellen Position des Spielers
def platzieren(ressource):
  print('Platziere: ', namen[ressource])
  #aber nur wenn der Spieler ein paar übrig hat ...
  if inventar[ressource] > 0:
    # Prüfe welche Ressource sich aktuell an der Spielerposition befindet
    aktuellesFeld = welt[spielerX][spielerY]
    #hebt die Ressource an der Spieler-Position auf
    #(sofern ist keine ERDE ist)
    if aktuellesFeld is not ERDE:
      inventar[aktuellesFeld] += 1
    # Platziere die Ressource an der aktuellen Position des Spielers
    welt[spielerX][spielerY] = ressource
    # Aktualisiere das Inventar
    inventar[ressource] -= 1
    # aktualisiere die Anzeigen (Welt und Inventar)
    zeichneRessource(spielerX, spielerY)
    zeichneInventar()
    #zeichneSpieler()
    print('   Platzieren von ', namen[ressource], ' abgeschlossen')
  # ... und falls keine Ressource vorhanden ist ...
  else:
    print('   Du hast kein/keinen ', namen[ressource], ' übrig')

# Eine neue Ressource herstellen
def herstellen(ressource):
  print('Bin beim Herstellen von ', namen[ressource])
  #sofern die Ressource hergestellt werden kann...
  if ressource in herstellenMit:
    #prüft ob die notwendigen Ressourcen vorhanden sind
    #um die neue Ressource herzustellen
    kannHergestelltWerden = True
    #für jedes Element, das benötigt wird um die Ressource herzustellen
    for i in herstellenMit[ressource]:
      #...falls wir nicht genügend davon haben...
      if herstellenMit[ressource][i] > inventar[i]:
      #...dann können wir die neue Ressource nicht herstellen!
        kannHergestelltWerden = False
        break
    #aber wenn wir sie herstellen können (wir haben alle dafür nötigen Ressourcen)
    if kannHergestelltWerden == True:
      #entferne die betreffenden Elemente aus dem Inventar
      for i in herstellenMit[ressource]:
        inventar[i] -= herstellenMit[ressource][i]
      #und füge die neu hergestellte Ressource dem Inventar hinzu
      inventar[ressource] += 1
      print('   Herstellen von ', namen[ressource], ' abgeschlossen')
    #...wenn die neue Ressource aber nicht hergestellt werden kann...
    else:
      print('   Die Ressource ', namen[ressource], ' kann nicht hergestellt werden.')
    #aktualisiere das angezeigte Inventar
    zeichneInventar()

#definiere eine Funktion um die Ressource abzulegen
def machPlatzieren(ressource):
  return lambda: platzieren(ressource)

#weist einem Tastendruck eine 'platziere'-Funktion zu
def verknuepfeTastenZumAblegen():
  for k in tastenZumAblegen:
    fenster.onkey(machPlatzieren(k), tastenZumAblegen[k])

#definiert eine Funktion um eine Ressource herzustellen
def stelleHer(ressource):
  return lambda: herstellen(ressource)

#weist einem Tastendruck eine 'stelle her'-Funktion zu
def verknuepfeTastenZumHerstellen():
  for k in tastenZumHerstellen:
    fenster.onkey(stelleHer(k), tastenZumHerstellen[k])

# Zeichne eine Ressource an der Position (y, x)
def zeichneRessource(y, x):
  #diese Variable verhindert, dass mehrere Objekte gleichzeitig gezeichnet werden
  global binAmZeichnen
  #nur dann zeichnen, wenn nichts anderes gezeichnet wird
  if binAmZeichnen == False:
    #dann zeichne ich jetzt
    binAmZeichnen = True
    #zeichne die Ressource an dieser Position auf dem Spielfeld und verwende dazu das richtige Bild
    grafikT.goto( (y * FELDGROESSE) + 20, hoehe - (x * FELDGROESSE) - 20 )
    #Zeichne das Feld mit der richtigen Textur
    textur = texturen[welt[y][x]]
    grafikT.shape(textur)
    grafikT.stamp()
    if playerX == y and playerY == x:
      rendererT.shape(playerImg)
      grafikT.stamp()
    fenster.update()
    #ich bin jetzt mit dem Zeichnen fertig
    binAmZeichnen = False
    
#zeichne das Spielfeld
def zeichneWelt():
  #bearbeite jede Zeile
  for zeile in range(WELTHOEHE):
    #bearbeite jede Spalte in der Zeile
    for spalte in range(WELTBREITE):
      #zeichne das Feld an der aktuellen Position
      zeichneRessource(spalte, zeile)

#Zeige das Inventar auf dem Bildschirm an
def zeichneInventar():
  #diese Variable verhindert, dass mehrere Objekte gleichzeitig gezeichnet werden
  global binAmZeichnen
  #nur dann zeichnen, wenn nichts anderes gezeichnet wird
  if binAmZeichnen == False:
    #dann zeichne ich jetzt
    binAmZeichnen = True
    #verwende ein Rechteck, um das aktuelle Inventar zu verdecken
    grafikT.color(HINTERGRUNDFARBE)
    grafikT.goto(0,0)
    grafikT.begin_fill()
    #grafikT.setheading(0)
    for i in range(2):
      grafikT.forward(inventar_hoehe - 60)
      grafikT.right(90)
      grafikT.forward(breite)
      grafikT.right(90)
    grafikT.end_fill()
    rendererT.color('black')
    #zeige den Text 'ablegen' und 'herstellen' an
    for i in range(1,anzahl_zeilen+1):
      grafikT.goto(20, (hoehe - (WELTHOEHE * FELDGROESSE)) - 20 - (i * 100))
      grafikT.write("Ablegen")
      grafikT.goto(20, (hoehe - (WELTHOEHE * FELDGROESSE)) - 40 - (i * 100))
      grafikT.write("Herstellen")
    #Position für das Inventar berechnen
    xPosition = 70
    yPostition = height - (MAPHEIGHT * TILESIZE) - 60
    elementNummer = 0
    for i, element in enumerate(ressourcen):
      #füge das Bild hinzu
      rendererT.goto(xPosition + 10, yPostition)
      grafikT.shape(texturen[element])
      grafikT.stamp()
      # Füge die Anzahl im Inventar hinzu
      grafikT.goto(xPosition, yPosition - FELDGROESSE)
      grafikT.write(inventar[element])
      #add the name
      grafikT.goto(xPosition, yPosition - FELDGROESSE - 20)
      rendererT.write('[' + names[item] + ']')
      #füge die Taste zum Ablegen hinzu
      grafikT.goto(xPosition, yPosition - FELDGROESSE - 40)
      grafikT.write(tastenZumAblegen[element])
      #füge die Taste zum Herstellen hinzu
      if herstellenMit.get(element) != None:
        rendererT.goto(xPosition, yPostition - TILESIZE - 60)
        grafikT.write(tastenZumHerstellen[element])     
      #gehe weiter um das nächste Element vom Inventar abzulegen
      xPosition += 50
      elementNummer += 1
      #gehe nach jeweils 10 Elementen eine Zeile nach unten
      if elementNummer % INVENTARBREITE == 0:
        xPosition = 70
        elementNummer = 0
        yPosition -= FELDGROESSE + 80
    binAmZeichnen = False

#generiere die Anleitungen, einschließlich der Herstellungsregeln
def generiereAnleitungen():
  anleitungen.append('Regeln für die Herstellung:')
  #für jede Ressource, die hergestellt werden kann ...
  for regel in herstellenMit:
    #definiere den Text für die Herstellungsregel
    herstellungsRegel = namen[regel] + ' = '
    for ressource, nummer in herstellenMit[regel].items():
      herstellungsRegel += str(nummer) + ' ' + namen[ressource] + ' '
    #füge die Herstellungsregel den Anweisungen hinzu
    anleitungen.append(herstellungsRegel)
  #Anzeigen der Anleitungen
  yPos = hoehe - 20
  for element in anleitungen:
    grafikT.goto( WELTBREITE*FELDGROESSE + 40, yPos)
    grafikT.write(element)
    yPos-=20

#generiere eine zufällige Welt
def generiereZufallsWelt():
  #bearbeite jede Zeile
  for zeile in range(WELTHOEHE):
    #bearbeite jede Spalte in der Zeile
    for spalte in range(WELTBREITE):
      #wähle eine Zufallszahl zwischen 0 und 10
      zufallsZahl = random.randint(0,10)
      #WASSER, wenn die Zufallszahl eine 1 oder 2 ist
      if zufallsZahl in [1,2]:
        feld = WASSER
      #GRAS, wenn die Zufallszahl eine 3 oder 4 ist
      elif zufallsZahl in [3,4]:
        feld = GRAS
      #ansonsten ist es ERDE
      else:
        feld = ERDE
      #aktualisiere die Position in der Welt mit der zufällig ausgewählten Ressource
      welt[spalte][zeile] = feld

#---
# ab hier wird das eigentliche Programm ausgeführt
#---

#importiere die benötigten Module und Variablen
import turtle
import random
from variables import *
from math import ceil

FELDGROESSE = 20
#die Anzahl der Inventarressourcen pro Zeile
INVENTARBREITE = 8
binAmZeichnen = False

#schaffe ein neues 'fenster'-Objekt
fenster = turtle.Screen()
#berechne die Breite und Höhe
breite = (FELDGROESSE * WELTBREITE) + max (200, INVENTARBREITE * 50)
anzahl_zeilen = int(ceil((len(ressourcen) / INVENTARBREITE)))
inventar_hoehe =  anzahl_zeilen * 120 + 40
hoehe = (FELDGROESSE * WELTHOEHE) + inventar_hoehe

fenster.setup(breite, hoehe)
fenster.setworldcoordinates(0,0,breite,hoehe)
fenster.bgcolor(HINTERGRUNDFARBE)
fenster.listen()

#registriere das Bild des Spielers  
fenster.register_shape(spielerBild)
#registriere jedes Bild der Ressourcen
for textur in texturen.values():
  fenster.register_shape(textur)

#definiere eine weitere Schildkröte, um die Grafik zu zeichnen
grafikT = turtle.Turtle()
grafikT.hideturtle()
grafikT.penup()
grafikT.speed(0)
grafikT.setheading(90)

#erschaffe eine Welt mit zufälligen Ressourcen.
welt = [ [ERDE for w in range(WELTHOEHE)] for h in range(WELTBREITE) ]

#weise den Tasten zum Bewegen und zum Nehmen die richtigen Funktionen zu.
fenster.onkey(nachObenBewegen, 'w')
fenster.onkey(nachUntenBewegen, 's')
fenster.onkey(nachLinksBewegen, 'a')
fenster.onkey(nachRechtsBewegen, 'd')
fenster.onkey(nehmen, 'space')

#definiere die Tasten zum Ablegen und Herstellen der Ressourcen
verknuepfeTastenZumAblegen()
verknuepfeTastenZumHerstellen()

#diese Funktionen sind weiter oben definiert
generiereZufallsWelt()
zeichneWelt()
zeichneInventar()
generiereAnleitungen()
