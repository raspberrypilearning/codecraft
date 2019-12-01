#!/bin/python3

#Varijable u igri koje se mogu mijenjati!

#boja pozadine u igri.
BACKGROUNDCOLOUR = 'lightblue'

#varijable mape.
PLOCICEMAX  = 40
SIRINAMAPE  = 20
VISINAMAPE = 15

#varijable koje predstavljaju različite resurse.
ZEMLJA   = 0
TRAVA  = 1
VODA   = 2
CIGLA   = 3
DRVO    = 4
PIJESAK    = 5
DASKA   = 6
STAKLO   = 7

#popis svih resursa u igri.
resources = [ZEMLJA,TRAVA,VODA,CIGLA,DRVO,PIJESAK,DASKA,STAKLO]

#nazivi resursa.
names = {
  ZEMLJA    : 'zemlja',
  TRAVA   : 'trava',
  VODA  : 'voda',
  CIGLA   : 'cigla',
  DRVO    : 'drvo',
  PIJESAK    : 'pijesak',
  DASKA   : 'daska',
  STAKLO   : 'staklo'
}

#rječnik koji povezuje resurse sa slikama.
textures = {
  ZEMLJA    : 'dirt.gif',
  TRAVA   : 'grass.gif',
  VODA   : 'water.gif',
  CIGLA   : 'brick.gif',
  DRVO    : 'wood.gif',
  PIJESAK    : 'sand.gif',
  DASKA   : 'plank.gif',
  STAKLO   : 'glass.gif'
}

#broj svih resursa kojeg igrač posjeduje.
inventory = {
  ZEMLJA   : 10,
  TRAVA   : 10,
  VODA   : 10,
  CIGLA   : 0,
  DRVO    : 5,
  PIJESAK   : 5,
  DASKA   : 0,
  STALO   : 0
}

#slika igrača.
playerImg = 'player.gif'

#položaj igrača.
playerX = 0
playerY = 0

#tipke za postavljanje resursa.
placekeys = {
  ZEMLJA  : '1',
  TRAVA : '2',
  VODA : '3',
  CIGLA : '4',
  DRVO  : '5',
  PIJESAK : '6',
  DASKA : '7',
  STAKLO: '8'
}

#pravila za stvaranje novih resursa.
crafting = {
  CIGLA   : { VODA: 1, ZEMLJA : 2 },
  DASKA    : { DRVO : 3 },
  GLASS    : { SAND : 3 }
}

#tipke za stvaranje cigli.
craftkeys = {
  CIGLA : 'r',
  DASKA : 'u',
  STAKLO : 'i'
}

#upute igre koje su prikazane.
instructions =  [
  'Upute:',
  'koristi tipke WASD za pomicanje'
]
