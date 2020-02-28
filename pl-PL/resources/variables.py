#!/bin/python3

# zmienne gry, które można modyfikować!

# kolor tła gry
KOLORTLA = 'bialy'

# zmienne mapy
LIMITZASOBOW  = 20
SZEROKOSCMAPY  = 10
WYSOKOSCMAPY = 10

# zmienne reprezentujące różne zasoby
ZIEMIA    = 0
TRAWA   = 1
WODA   = 2
CEGLA   = 3

#lista wszystkich zasobów gry.
zasoby = [ZIEMIA,TRAWA,WODA,CEGLA]

#nazwy zasobów.
nazwy = {
  ZIEMIA    : 'ziemia',
  TRAWA   : 'trawa',
  WODA   : 'woda',
  CEGLA   : 'cegla'
}

#słownik łączący zasoby z obrazami.
tekstury = {
  ZIEMIA    : 'dirt.gif',
  TRAWA   : 'grass.gif',
  WODA   : 'water.gif',
  CEGLA   : 'brick.gif'
}

#ilość zasobów posiadanych przez gracza.
ekwipunek = {
  ZIEMIA    : 10,
  TRAWA   : 10,
  WODA   : 10,
  CEGLA   : 0
}

#obrazek gracza.
graczObraz = 'player.gif'

#pozycja gracza.
graczX = 0
graczY = 0

#zasady tworzenia nowych zasobów.
budowanie = {
  CEGLA    : { WODA : 1, ZIEMIA : 2 }
}

#klawisze do umieszczania zasobów.
klawiszeumieszczania = {
  ZIEMIA  : '1',
  TRAWA : '2',
  WODA : '3',
  CEGLA : '4'
}

#klawisze do tworzenia zasobów.
klawiszebudowania = {
  CEGLA : 'r'
}

#wyświetlane instrukcje gry.
instrukcje =  [
  'Instrukcje:',
  'Ruchy - WSAD'
]
