#!/bin/python3

#############
# CodeCraft #
#############

#---
#Funzioni del gioco
#---

#sposta il giocatore a sinistra di una casella.
def spostaSinistra():
  global giocatoreX
  if(disegno == False and giocatoreX > 0):
    vecchioX = giocatoreX
    giocatoreX -= 1
    disegnaRisorsa(vecchioX, giocatoreY)
    disegnaRisorsa(giocatoreX, giocatoreY)
    
#sposta il giocatore a destra di 1 casella.
def spostaDestra():
  global giocatoreX, LARGHEZZAMAPPA
  if(disegno == False and giocatoreX < LARGHEZZAMAPPA - 1):
    vecchioX = giocatoreX
    giocatoreX += 1
    disegnaRisorsa(vecchioX, giocatoreY)
    disegnaRisorsa(giocatoreX, giocatoreY)
    
#sposta il giocatore verso l'alto di 1 casella.
def spostaSu():
  global giocatoreY
  if (disegno == False and giocatoreY> 0):
    vecchioY = giocatoreY
    giocatoreY -= 1
    disegnaRisorsa(giocatoreX, vecchioY)
    disegnaRisorsa(giocatoreX, giocatoreY)
    
#sposta il giocatore verso il basso di 1 casella.
def spostaGiu():
  global giocatoreY, ALTEZZAMAPPA
  if(disegno == False and giocatoreY < ALTEZZAMAPPA - 1):
    vecchioY = giocatoreY
    giocatoreY += 1
    disegnaRisorsa(giocatoreX, vecchioY)
    disegnaRisorsa(giocatoreX, giocatoreY)
    
#prendi la risorsa che si trova nella casella in cui c'è il giocatore.
def prendi():
  global giocatoreX, giocatoreY
  disegna = True
  casellaAttuale = mondo[giocatoreX][giocatoreY]
  #se il giocatore non ne ha già troppe...
  if inventario[casellaAttuale] < MAXCASELLE:
    #il giocatore ora ha un'unità in più di questa risorsa
    inventario[casellaAttuale] += 1
    #il giocatore è ora sul terreno
    mondo[giocatoreX][giocatoreY] = TERRENO
    #disegna la nuova casella TERRENO
    disegnaRisorsa(giocatoreX, giocatoreY)
    #disegna nuovamente l'inventario aggiungendo la nuova risorsa.
    disegnaInventario()
    #disegnaGiocatore()

#colloca una risorsa sull'attuale posizione del giocatore
def posiziona(risorsa):
  print('posiziona: ', nomi[risorsa])
  #posiziona solo nel caso in cui il giocatore ne abbia altre a disposizione...
  if inventario[risorsa] > 0:
    #identifica la risorsa nell'attuale posizione del giocatore
    casellaAttuale = mondo[giocatoreX][giocatoreY]
    #prendi la risorsa che si trova nella casella in cui c'è il giocatore
    #(se non è (ovvero "is not") TERRENO)
    if casellaAttuale is not TERRENO:
      inventario[casellaAttuale] += 1
    #colloca la risorsa sull'attuale posizione del giocatore
    mondo[giocatoreX][giocatoreY] = risorsa
    #aggiungi la nuova risorsa all'inventario
    inventario[risorsa] -= 1
    #aggiorna quello che viene visualizzato (il mondo e l'inventario)
    disegnaRisorsa(giocatoreX, giocatoreY)
    disegnaInventario()
    #disegnaGiocatore()
    print('   Posizionamento', nomi[risorsa], 'completato')
  #...e se non ne hanno più...
  else:
    print('   Non hai più risorse', nomi[risorsa], 'a disposizione')

#crea una nuova risorsa
def crea(risorsa):
  print('Crea: ', nomi[risorsa])
  #se la risorsa può essere creata...
  if risorsa in creazione:
    #controlla se hai a disposizione le risorse
    #per realizzare questo oggetto
    puoEssereCreata = True
    #per ogni oggetto dell'inventario necessario per creare la risorsa
    for i in creazione[risorsa]:
      #...se non ne abbiamo a sufficienza...
      if creazione[risorsa][i] > inventario[i]:
      #...non possiamo crearlo!
        puoEssereCreata = False
        break
    #se possiamo creare l'oggetto (abbiamo a disposizione tutte le risorse necessarie)
    if puoEssereCreata == True:
      #prendi ogni oggetto dall'inventario
      for i in creazione[risorsa]:
        inventario[i] -= creazione[risorsa][i]
      #aggiungi l'oggetto creato all'inventario
      inventario[risorsa] += 1
      print('   Creazione', nomi[risorsa], 'completata')
    #...in caso contrario la risorsa non può essere creata...
    else:
      print('   La risorsa', nomi[risorsa],'non può essere creata')
    #aggiorna l'inventario visualizzato
    disegnaInventario()

#crea una funzione per posizionare ogni risorsa
def definisciPosizione(risorsa):
  return lambda: posiziona(risorsa)

#questo permette di assegnare la funzione 'posiziona' ad ogni tasto
def definisciTastiPosizione():
  for t in tastiPosizione:
    schermo.onkey(definisciPosizione(t), tastiPosizione[t])

#crea una funzione per realizzare ogni risorsa
def definisciCreazione(risorsa):
  return lambda: crea(risorsa)

#questo permette di assegnare la funzione 'crea' ad ogni tasto
def definisciTastiCreazione():
  for t in tastiCreazione:
    schermo.onkey(definisciCreazione(t), tastiCreazione[t])

#disegna una risorsa nella posizione (y,x)
def disegnaRisorsa(y, x):
  #questa variabile arresta altri elementi in corso di elaborazione
  global disegno
  #disegna solo se non c'è nient'altro in fase di elaborazione
  if disegno == False:
    #c'è altro in fase di elaborazione
    disegna = True
    #disegna la risorsa nella posizione selezionata nella mappa usando l'immagine corretta
    visualizzatoreT.goto( (y * DIMENSIONECASELLA) + 20, altezza - (x * DIMENSIONECASELLA) - 20 )
    #riempie la casella con l'immagine corretta
    immagine = immagini[mondo[y][x]]
    visualizzatoreT.shape(immagine)
    visualizzatoreT.stamp()
    if giocatoreX == y and giocatoreY == x:
      visualizzatoreT.shape(immagineGiocatore)
      visualizzatoreT.stamp()
    schermo.update()
    #non c'è nulla in fase di elaborazione
    disegno = False
    
#disegna la mappa del mondo
def disegnaMondo():
  #esegui un ciclo per ogni riga
  for riga in range(ALTEZZAMAPPA):
    #esegui un ciclo per ogni colonna nella riga in questione
    for colonna in range(LARGHEZZAMAPPA):
      #disegna la casella nella posizione corrente
      disegnaRisorsa(colonna, riga)

#disegna l'inventario sullo schermo
def disegnaInventario():
  #questa variabile arresta altri elementi in corso di elaborazione
  global disegno
  #disegna solo se non c'è nient'altro in fase di elaborazione
  if disegno == False:
    #c'è altro in fase di elaborazione
    disegna = True
    #utilizza un rettangolo per coprire l'inventario
    visualizzatoreT.color(COLORESFONDO)
    visualizzatoreT.goto(0,0)
    visualizzatoreT.begin_fill()
    #visualizzatoreT.setheading(0)
    for i in range(2):
      visualizzatoreT.forward(altezza_inventario - 60)
      visualizzatoreT.right(90)
      visualizzatoreT.forward(larghezza)
      visualizzatoreT.right(90)
    visualizzatoreT.end_fill()
    visualizzatoreT.color('black')
    #visualizza il testo 'posiziona' e 'crea'
    for i in range(1,num_righe+1):
      visualizzatoreT.goto(20, (altezza - (ALTEZZAMAPPA * DIMENSIONECASELLA)) - 20 - (i * 100))
      visualizzatoreT.write("posiziona")
      visualizzatoreT.goto(20, (altezza - (ALTEZZAMAPPA * DIMENSIONECASELLA)) - 40 - (i * 100))
      visualizzatoreT.write("crea")
    #determina la posizione dell'inventario
    PosizioneX = 70
    PosizioneY = altezza - (ALTEZZAMAPPA * DIMENSIONECASELLA) - 80
    oggettoNum = 0
    for i, oggetto in enumerate(risorse):
      #aggiungi l'immagine
      visualizzatoreT.goto(PosizioneX, PosizioneY)
      visualizzatoreT.shape(immagini[oggetto])
      visualizzatoreT.stamp()
      #aggiungi il numero nell'inventario
      visualizzatoreT.goto(PosizioneX, PosizioneY - DIMENSIONECASELLA)
      visualizzatoreT.write(inventario[oggetto])
      #aggiungi il tasto alla posizione
      visualizzatoreT.goto(PosizioneX, PosizioneY - DIMENSIONECASELLA - 20)
      visualizzatoreT.write(tastiPosizione[oggetto])
      #aggiungi il tasto alla creazione
      if creazione.get(oggetto) != None:
        visualizzatoreT.goto(PosizioneX, PosizioneY - DIMENSIONECASELLA - 40)
        visualizzatoreT.write(tastiCreazione[oggetto])     
      #avanza per posizionare l'oggetto successivo nell'inventario
      PosizioneX += 50
      oggettoNum =+ 1
      #ogni 10 oggetti passa alla riga successiva
      if oggettoNum % LARGHEZZAINVENTARIO == 0:
        PosizioneX = 70
        oggettoNum = 0
        PosizioneY -= DIMENSIONECASELLA + 80
    disegno = False

#genera le istruzioni e le regole per la creazione
def generaIstruzioni():
  istruzioni.append('Regole per la creazione delle risorse:')
  #per ogni risorsa che può essere creata...
  for regola in creazione:
    #genera il testo con le istruzioni per la creazione di nuove risorse
    regolacreazione = nomi[regola] + ' = '
    for risorsa, numero in creazione[regola].items():
      regolacreazione += str(numero) + ' ' + nomi[risorsa] + ' '
    #aggiungi la regola per la creazione alle istruzioni
    istruzioni.append(regolacreazione)
  #visualizza le istruzioni
  posY = altezza - 20
  for oggetto in istruzioni:
    visualizzatoreT.goto( LARGHEZZAMAPPA*DIMENSIONECASELLA + 40, posY)
    visualizzatoreT.write(oggetto)
    posY-=20

#genera un mondo aleatorio
def generaMondoAleatorio():
  #esegui un ciclo per ogni riga
  for riga in range(ALTEZZAMAPPA):
    #esegui un ciclo per ogni colonna nella riga in questione
    for colonna in range(LARGHEZZAMAPPA):
      #scegli un numero a caso fra 0 e 10
      numeroACaso = random.randint(0,10)
      #ACQUA se il numero a caso è 1 oppure 2
      if numeroACaso in [1,2]:
        casella = ACQUA
      #ERBA se il numero a caso è 3 oppure 4
      elif numeroACaso in [3,4]:
        casella = ERBA
      #LEGNO se è 5
      elif numeroACaso == 5:
        casella = LEGNO
      #SABBIA se è 6
      elif numeroACaso == 6:
        casella = SABBIA
      #altrimenti è TERRENO
      else:
        casella = TERRENO
      #assegna una posizione nella mappa alla casella scelta in maniera casuale
      mondo[colonna][riga] = casella

#---
#Il codice inizia l'esecuzione da qui
#---

#importa i moduli e le variabili necessarie
import turtle
import random
from variables import *
from math import ceil

DIMENSIONECASELLA = 20
#il numero di risorse dell'inventario per riga
LARGHEZZAINVENTARIO = 8
disegno = False

#crea un nuovo oggetto 'schermo'
schermo = turtle.Screen()
#calcola la larghezza e l'altezza
larghezza = (DIMENSIONECASELLA * LARGHEZZAMAPPA) + max(200, LARGHEZZAINVENTARIO *50)
num_righe = int(ceil((len(risorse) / LARGHEZZAINVENTARIO)))
altezza_inventario =  num_righe * 120 + 40
altezza = (DIMENSIONECASELLA * ALTEZZAMAPPA) + altezza_inventario

schermo.setup(larghezza, altezza)
schermo.setworldcoordinates(0,0,larghezza,altezza)
schermo.bgcolor(COLORESFONDO)
schermo.listen()

#registra l'immagine del giocatore  
schermo.register_shape(immagineGiocatore)
#registra ognuna delle immagini delle risorse
for immagine in immagini.values():
  schermo.register_shape(immagine)

#crea un altro oggetto con il modulo turtle che permetta di gestire le immagini
visualizzatoreT = turtle.Turtle()
visualizzatoreT.hideturtle()
visualizzatoreT.penup()
visualizzatoreT.speed(0)
visualizzatoreT.setheading(90)

#crea un mondo di risorse aleatorie.
mondo = [ [TERRENO for l in range(ALTEZZAMAPPA)] for a in range(LARGHEZZAMAPPA) ]

#associa alle funzioni corrette i tasti da conoscere per spostare/spostarsi e raccogliere le risorse.
schermo.onkey(spostaSu, 'w')
schermo.onkey(spostaGiu, 's')
schermo.onkey(spostaSinistra, 'a')
schermo.onkey(spostaDestra, 'd')
#per prendere un oggetto premi la barra spaziatrice
schermo.onkey(prendi, ' ')


#imposta i tasti per posizionare e creare ogni risorsa
definisciTastiPosizione()
definisciTastiCreazione()

#queste funzioni sono definite in alto
generaMondoAleatorio()
disegnaMondo()
disegnaInventario()
generaIstruzioni()


