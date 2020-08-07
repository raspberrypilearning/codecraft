#!/bin/python3

#Le variabili del gioco che possono essere cambiate!

#colore dello sfondo del gioco.
COLORESFONDO = 'white'

#variabili della mappa.
MAXCASELLE = 20
LARGHEZZAMAPPA = 10
ALTEZZAMAPPA = 10

#variabili che rappresentano le varie risorse.
TERRENO = 0
ERBA = 1
ACQUA = 2
MATTONE = 3

#una lista di tutte le risorse del gioco.
risorse = [TERRENO, ERBA, ACQUA, MATTONE]

#i nomi delle risorse.
nomi = {
  TERRENO    : 'terreno',
  ERBA   : 'erba',
  ACQUA   : 'acqua',
  MATTONE   : 'mattone'
}

#un dizionario che assegna ad ogni risorsa la sua immagine.
immagini = {
  TERRENO    : 'dirt.gif',
  ERBA   : 'grass.gif',
  ACQUA   : 'water.gif',
  MATTONE   : 'brick.gif'
}

#il numero di ogni risorsa che il giocatore ha a disposizione.
inventario = {
  TERRENO    : 10,
  ERBA   : 10,
  ACQUA   : 10,
  MATTONE   : 0
}

#l'immagine del giocatore.
immagineGiocatore = 'player.gif'

#la posizione del giocatore.
giocatoreX = 0
giocatoreY = 0

#regole per creare nuove risorse.
creazione = {
  MATTONE    : { ACQUA : 1, TERRENO : 2 }
}

#tasti per posizionare le risorse.
tastiPosizione = {
  TERRENO  : '1',
  ERBA : '2',
  ACQUA : '3',
  MATTONE : '4'
}

#tasti per creare le caselle.
tastiCreazione = {
  MATTONE : 'm'
}

#istruzioni del gioco che vengono mostrate.
istruzioni =  [
  'Istruzioni:',
  'Utilizza i tasti W, A, S, D come frecce per muoverti'
]
