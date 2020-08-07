#!/bin/python3

#Le variabili del gioco che possono essere cambiate!

#colore dello sfondo del gioco.
COLORESFONDO = 'lightblue'

#variabili della mappa.
MAXCASELLE = 40
LARGHEZZAMAPPA = 20
ALTEZZAMAPPA = 15

#variabili che rappresentano le varie risorse.
TERRENO = 0
ERBA = 1
ACQUA = 2
MATTONE = 3
LEGNO = 4
SABBIA = 5
ASSE = 6
VETRO = 7

#una lista di tutte le risorse del gioco.
risorse = [TERRENO, ERBA, ACQUA, MATTONE, LEGNO, SABBIA, ASSE, VETRO]

#i nomi delle risorse.
nomi = {
  TERRENO    : 'terreno',
  ERBA   : 'erba',
  ACQUA   : 'acqua',
  MATTONE   : 'mattone',
  LEGNO    : 'legno',
  SABBIA    : 'sabbia',
  ASSE   : 'asse',
  VETRO   : 'vetro'
}

#un dizionario che assegna ad ogni risorsa la sua immagine.
immagini = {
  TERRENO    : 'dirt.gif',
  ERBA   : 'grass.gif',
  ACQUA   : 'water.gif',
  MATTONE   : 'brick.gif',
  LEGNO    : 'wood.gif',
  SABBIA    : 'sand.gif',
  ASSE   : 'plank.gif',
  VETRO   : 'glass.gif'
}

#il numero di ogni risorsa che il giocatore ha a disposizione.
inventario = {
  TERRENO    : 10,
  ERBA   : 10,
  ACQUA   : 10,
  MATTONE   : 0,
  LEGNO    : 5,
  SABBIA    : 5,
  ASSE   : 0,
  VETRO   : 0
}

#l'immagine del giocatore.
immagineGiocatore = 'player.gif'

#la posizione del giocatore.
giocatoreX = 0
giocatoreY = 0

#tasti per posizionare le risorse.
tastiPosizione = {
  TERRENO  : '1',
  ERBA : '2',
  ACQUA : '3',
  MATTONE : '4',
  LEGNO  : '5',
  SABBIA  : '6',
  ASSE : '7',
  VETRO : '8'
}

#regole per creare nuove risorse.
creazione = {
  MATTONE    : { ACQUA : 1, TERRENO : 2 },
  ASSE    : { LEGNO : 3 },
  VETRO    : { SABBIA : 3 }
}

#tasti per creare le caselle.
tastiCreazione = {
  MATTONE : 'm',
  ASSE : 'p',
  VETRO : 'v'
}

#istruzioni del gioco che vengono mostrate.
istruzioni =  [
  'Istruzioni:',
  'Utilizza i tasti W, A, S, D come frecce per muoverti'
]
