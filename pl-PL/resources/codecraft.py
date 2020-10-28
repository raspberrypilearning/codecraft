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
    # coś się obecnie rysowane
    rysowanie = True
    # narysuj zasób w zadanej pozycji na mapie używając odpowiedniego obrazka
    rendererT.goto( (y * ROZMIARKLOCKA) + 20, height - (x * ROZMIARKLOCKA) - 20 )
    # rysuj blok używając odpowiedniej tekstury
    tekstura = tekstury[swiat[y][x]]
    rendererT.shape(tekstura)
    rendererT.stamp()
    if graczX == y and graczY == x:
      rendererT.shape(obrazGracz)
      rendererT.stamp()
    screen.update()
    # obecnie nic już się nie rysuje
    rysowanie = False
    
# rysuj świat
def rysujSwiat():
      # pętla po wierszach
  for wiersz in range(WYSOKOSCMAPY):
            # pętla po kolumnach każdego wiersza
    for kolumna in range(SZEROKOSCMAPY):
                  # rysuj blok w bieżącej pozycji
      rysujZasob(kolumna, wiersz)

# rysuj ekwipunek na ekranie
def rysujEkwipunek():
      # ta zmienna wstrzymuje rysowanie innych elementów
  global rysowanie
      # rysuj tylko gdy nic innego nie jest obecnie rysowane
  if rysowanie == False:
    # coś się obecnie rysowane
    rysowanie = True
    # przykryj obecny ekwipunek prostokątem
    rendererT.color(KOLORTLA)
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
      rendererT.goto(20, (height - (WYSOKOSCMAPY * ROZMIARKLOCKA)) - 20 - (i * 100))
      rendererT.write("wstaw")
      rendererT.goto(20, (height - (WYSOKOSCMAPY * ROZMIARKLOCKA)) - 40 - (i * 100))
      rendererT.write("buduj")
            # ustaw pozycję ekwipunku
    xPosition = 70
    yPostition = height - (MAPHEIGHT * TILESIZE) - 60
    numerElementu = 0
    for i, element in enumerate(zasoby):
      # dodaj obrazek
      rendererT.goto(xPosition + 10, yPostition)
      rendererT.shape(tekstury[element])
      rendererT.stamp()
      # dodaj numer do ekwipunku
      rendererT.goto(xPosition, yPostition - ROZMIARKLOCKA)
      rendererT.write(ekwipunek[element])
      #add the name
      rendererT.goto(xPosition, yPostition - ROZMIARKLOCKA - 20)
      rendererT.write('[' + names[item] + ']')
      # dodaj klawisz wstawiania
      rendererT.goto(xPosition, yPostition - ROZMIARKLOCKA - 40)
      rendererT.write(klawiszeumieszczania[element])
      # dodaj klawisz do budowania
      if budowanie.get(element) != None:
        rendererT.goto(xPosition, yPostition - TILESIZE - 60)
        rendererT.write(klawiszetworzenia[element])     
      # przesuń się, aby wstawić następny element ekwipunku
      xPosition += 50
      numerElementu += 1
      # przesuń się do kolejnego wiersza po każdym 10 elemencie
      if NumerElementu % SZEROKOSCEKWIPUNKU == 0:
        xPosition = 70
        numerElementu = 0
        yPostition -= ROZMIARKLOCKA + 80
    rysowanie = False

# wygeneruj instrukcje, w tym zasady tworzenia
def generujInstrukcje():
  instructions.append('Zasady budowania:')
  # dla każdego zasobu, który można zbudować...
  for regula in budowanie:
    # utwórz tekst dla reguły tworzenia
    regulabudowania = nazwy[regula] + ' = '
    for zasob, liczba in budowanie[regula].elementy():
      regulabudowania += str(liczba) + ' ' + nazwy[zasob] + ' '
    # dodaj regułę tworzenia do 'instructions'
    instructions.append(regulabudowania)
  # wyświetl instrukcje
  yPos = height - 20
  for element in instrukcje:
    rendererT.goto( SZEROKOSCMAPY*ROZMIARKLOCKA + 40, yPos)
    rendererT.write(element)
    yPos-=20

# wygeneruj losowy świat
def generujLosowySwiat():
      # pętla po wierszach
  for wiersz in range(WYSOKOSCMAPY):
    # pętla po kolumnach każdego wiersza
    for kolumna in range(SZEROKOSCMAPY):
      # losuj liczbę między 0, a 10
      losowaLiczba = random.randint(0,10)
      # WATER jeśli losowa liczba to 1 lub 2
      if losowaLiczba in [1,2]:
        klocek = WODA
      # GRASS jeśli losowa liczba to 3 lub 4
      elif losowaLiczba in [3,4]:
        klocek = TRAWA
      # w pozostałych przypadkach to DIRT
      else:
        klocek = ZIEMIA
      # losuj pozycję na mapie
      swiat[kolumna][wiersz] = klocek

#---
# kod zaczyna działać tutaj
#---

# importuj wymagane moduły i zmienne
import turtle
import random
from variables import *
from math import ceil

ROZMIARKLOCKA = 20
# liczba zasobów ekwipunku w wierszu
SZEROKOSCEKWIPUNKU = 8
rysowanie = False

# utwórz nowy obiekt „screen”
ekran = turtle.Screen()
# oblicz szerokość i wysokość
szerokosc = (ROZMIARKLOCKA * SZEROKOSCMAPY) + max(200,SZEROKOSCEKWIPUNKU * 50)
num_rows = int(ceil((len(zasoby) / SZEROKOSCEKWIPUNKU)))
wysokosc_ekwipunku =  num_rows * 120 + 40
wysokosc = (ROZMIARKLOCKA * WYSOKOSCMAPY) + wysokosc_ekwipunku

screen.setup(width, height)
screen.setworldcoordinates(0,0,width,height)
screen.bgcolor(KOLORTLA)
screen.listen()

# zarejestruj obrazek gracza  
screen.register_shape(obrazGracz)
#zarejestruj każdy z obrazów zasobów
for tekstura in tekstury.values():
  screen.register_shape(tekstura)

# utwórz kolejnego żółwia do rysowania grafiki
rendererT = turtle.Turtle()
rendererT.hideturtle()
rendererT.penup()
rendererT.speed(0)
rendererT.setheading(90)

# utwórz świat z losowanych zasobów
swiat = [ [ZIEMIA for w in range(WYSOKOSCMAPY)] for h in range(SZEROKOSCMAPY) ]

# przypisz klawisze ruchów i podnoszenia do odpowiednich funkcji
screen.onkey(przesunGora, 'w')
screen.onkey(przesunDol, 's')
screen.onkey(przesunLewo, 'a')
screen.onkey(przesunPrawo, 'd')
screen.onkey(podnies, 'spacja')

# ustaw klawisze do umieszczania i tworzenia każdego zasobu
polaczKlawiszeUmieszczania()
polaczKlawiszeTworzenia()

# te funkcje są zdefiniowane powyżej
generujLosowySwiat()
rysujSwiat()
rysujEkwipunek()
generujInstrukcje()
