#!/bin/python3

#Variables du jeu qui peuvent être modifiées !

#couleur de fond du jeu.
COULEURDEFOND = 'lightblue'

#variables de la carte.
MAXIMUMTUILES = 40
LARGEURCARTE = 20
HAUTEURCARTE = 15

#Variables qui représentent les différentes ressources.
TERRE    = 0
HERBE   = 1
EAU   = 2
BRIQUE   = 3
BOIS    = 4
SABLE    = 5
PLANCHE   = 6
VERRE   = 7

#liste de toutes les ressources du jeu.
ressources = [TERRE,HERBE,EAU,BRIQUE,BOIS,SABLE,PLANCHE,VERRE]

#noms des ressources.
noms = {
  TERRE    : 'terre',
  HERBE   : 'herbe',
  EAU   : 'eau',
  BRIQUE   : 'brique',
  BOIS    : 'bois',
  SABLE    : 'sable',
  PLANCHE   : 'planche',
  VERRE   : 'verre'
}

#dictionnaire liant les ressources aux images.
textures = {
  TERRE    : 'dirt.gif',
  HERBE   : 'grass.gif',
  EAU   : 'water.gif',
  BRIQUE   : 'brick.gif',
  BOIS    : 'wood.gif',
  SABLE    : 'sand.gif',
  PLANCHE   : 'plank.gif',
  VERRE   : 'glass.gif'
}

#nombre de chaque ressource que possède le joueur.
inventaire = {
  TERRE    : 10,
  HERBE   : 10,
  EAU   : 10,
  BRIQUE  : 0,
  BOIS    : 5,
  SABLE    : 5,
  PLANCHE   : 0,
  VERRE   : 0
}

#image du joueur.
joueurImg = 'player.gif'

#position du joueur.
joueurX = 0
joueurY = 0

#touches pour placer des ressources.
touchesPlacement = {
  TERRE  : '1',
  HERBE : '2',
  EAU : '3',
  BRIQUE : '4',
  BOIS : '5',
  SABLE : '6',
  PLANCHE : '7',
  VERRE : '8'
}

#règles pour fabriquer des nouvelles ressources.
fabrication = {
  BRIQUE : { EAU: 1, TERRE : 2 },
  PLANCHE : {BOIS : 3},
  VERRE : { SABLE : 3 }
}

#touches pour fabriquer les blocs.
touchesFabrication = {
  BRIQUE : 'r',
  PLANCHE : 'u',
  VERRE : 'i'
}

#instructions de jeu affichées.
instructions = [
  'Instructions:',
  'Utilise ZQSD pour te déplacer'
]
