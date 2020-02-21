#!/bin/python3

# zmienne gry, które można modyfikować!

# kolor tła gry
KOLORTLA = 'jasnoniebieski'

# zmienne mapy
LIMITZASOBOW  = 40
SZEROKOSCMAPY  = 20
WYSOKOSCMAPY = 15

# zmienne reprezentujące różne zasoby
ZIEMIA    = 0
TRAWA   = 1
WODA   = 2
CEGLA   = 3
DREWNO = 4
PIASEK    = 5
DESKA   = 6
SZKLO   = 7

# lista wszystkich zasobów gry
zasoby = [ZIEMIA,TRAWA,WODA,CEGLA,DREWNO,PIASEK,DESKA,SZKLO]

# nazwy zasobów
nazwy = {
  ZIEMIA    : 'ziemia',
  TRAWA   : 'trawa',
  WODA   : 'woda',
  CEGLA   : 'cegla',
  DREWNO: 'drewno',
  PIASEK    : 'piasek',
  DESKA   : 'deska',
  SZKLO   : 'szklo'
}

# słownik łączący zasoby z obrazami
tekstury = {
  ZIEMIA    : 'dirt.gif',
  TRAWA   : 'grass.gif',
  WODA   : 'water.gif',
  CEGLA   : 'brick.gif',
  DREWNO    : 'wood.gif',
  PIASEK    : 'sand.gif',
  DESKA   : 'plank.gif',
  SZKLO   : 'glass.gif'
}

# ilość zasobów posiadanych przez gracza
ekwipunek = {
  ZIEMIA    : 10,
  TRAWA   : 10,
  WODA   : 10,
  CEGLA   : 0,
  DREWNO    : 5,
  PIASEK    : 5,
  DESKA   : 0,
  SZKLO   : 0
}

# obrazek gracza
graczObraz = 'player.gif'

#pozycja gracza.
graczX = 0
graczY = 0

# klawisze do umieszczania zasobów
klawiszeumieszczania = {
  ZIEMIA  : '1',
  TRAWA : '2',
  WODA : '3',
  CEGLA : '4',
  DREWNO  : '5',
  PIASEK  : '6',
  DESKA : '7',
  SZKLO : '8'
}

# zasady  tworzenia nowych zasobów
budowanie = {
  CEGLA    : { WODA : 1, ZIEMIA : 2 },
  DESKA    : { DREWNO : 3 },
  SZKLO    : { PIASEK : 3 }
}

# klawisze do tworzenia zasobów
klawiszebudowania = {
  CEGLA : 'r',
  DESKA : 'u',
  SZKLO : 'i'
}

# wyświetlane instrukcje gry
instrukcje =  [
  'Instrukcje:',
  'Ruchy - WSAD'
]
