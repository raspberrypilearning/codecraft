#!/bin/python3

#Variables du jeu qui peuvent être modifiées !

#couleur de fond du jeu.
COULEURDEFOND = 'white'

#variables de la carte.
MAXIMUMTUILES = 20
LARGEURCARTE = 10
HAUTEURCARTE = 10

#Variables qui représentent les différentes ressources.
TERRE    = 0
HERBE   = 1
EAU   = 2
BRIQUE   = 3

#liste de toutes les ressources du jeu.
ressources = [TERRE,HERBE,EAU,BRIQUE]

#noms des ressources.
noms = {
  TERRE    : 'terre',
  HERBE   : 'herbe',
  EAU   : 'eau',
  BRIQUE   : 'brique'
}

#dictionnaire liant les ressources aux images.
textures = {
  TERRE    : 'dirt.gif',
  HERBE   : 'grass.gif',
  EAU   : 'water.gif',
  BRIQUE   : 'brick.gif'
}

#nombre de chaque ressource que possède le joueur.
inventaire = {
  TERRE    : 10,
  HERBE   : 10,
  EAU   : 10,
  BRIQUE  : 0
}

#image du joueur.
joueurImg = 'player.gif'

#position du joueur.
joueurX = 0
joueurY = 0

#règles pour fabriquer des nouvelles ressources.
fabrication = {
  BRIQUE : { EAU: 1, TERRE : 2 }
}

#touches pour placer des ressources.
touchesPlacement = {
  TERRE : '1',
  HERBE : '2',
  EAU : '3',
  BRIQUE : '4'
}

#touches pour fabriquer les blocs.
touchesFabrication = {
  BRIQUE : 'r'
}

#instructions de jeu affichées.
instructions = [
  'Instructions:',
  'Utilise ZQSD pour te déplacer'
]
