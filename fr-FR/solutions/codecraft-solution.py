#!/bin/python3

#############
# CodeCraft #
#############

#---
# CodeCraft #
#---

#déplacer le joueur d'une tuile vers la gauche.
def deplaceGauche():
  global xJoueur
  if(drawing == False and playerX > 0):
    oldX = playerX
    xJoueur -= 1
    drawResource(oldX, playerY)
    dessineRessource(xJoueur, yJoueur)
    
#déplacer le joueur d'une tuile vers la droite.
def deplaceDroite():
  global xJoueur, LARGEURCARTE
  if(drawing == False and playerX < MAPWIDTH - 1):
    oldX = playerX
    xJoueur += 1
    drawResource(oldX, playerY)
    dessineRessource(xJoueur, yJoueur)
    
#déplacer le joueur d'une tuile vers le haut.
def deplaceHaut():
  global yJoueur
  if(drawing == False and playerY > 0):
    oldY = playerY
    yJoueur -= 1
    drawResource(playerX, oldY)
    dessineRessource(xJoueur, yJoueur)
    
#déplacer le joueur d'une tuile vers le bas.
def deplaceBas():
  global yJoueur, HAUTEURCARTE
  if(drawing == False and playerY < MAPHEIGHT - 1):
    oldY = playerY
    yJoueur += 1
    drawResource(playerX, oldY)
    dessineRessource(xJoueur, yJoueur)
    
#ramasser les ressources à la position du joueur.
def ramasse():
  global xJoueur, yJoueur
  dessine = True
  tuileActuelle = carte[xJoueur][yJoueur]
  #si l'utilisateur n'en a pas déjà trop...
  if inventaire[tuileActuelle] < MAXIMUMTUILES:
    #le joueur a donc un de plus de cette ressource
    inventaire[tuileActuelle] += 1
    #le joueur se tient maintenant sur de la terre
    carte[xJoueur][yJoueur] = TERRE
    #dessiner une nouvelle tuile de terre
    dessineRessource(xJoueur, yJoueur)
    #redessiner l'inventaire avec les nouvelles ressources.
    dessineInventaire()
    #dessineJoueur()

#placer une ressource à la position actuelle du joueur
def place(ressource):
  print('Placement de', noms[ressource])
  #seulement si le joueur en a encore dans son inventaire...
  if inventaire[ressource] > 0:
    #trouver la ressource à la position actuelle du joueur
    tuileActuelle = carte[xJoueur][yJoueur]
    #ramasser la ressource sur laquelle se trouve le joueur
    #(si ce n'est pas de la TERRE)
    if tuileActuelle is not TERRE:
      inventaire[tuileActuelle] += 1
    #place la ressource à la position actuelle du joueur
    carte[xJoueur][yJoueur] = ressource
    #retire la ressource à l'inventaire
    inventaire[ressource] -= 1
    #met à jour l'affichage (carte et inventaire)
    dessineRessource(xJoueur, yJoueur)
    dessineInventaire()
    #dessineJoueur()
    print('    Placement de', noms[ressource], 'terminé')
  #... et s'il n'y en a plus ...
  else:
    print('    Vous n\'avez plus de', noms[ressource])

#fabriquer de nouvelles ressources
def fabrique(ressource):
  print('Fabrication de', noms[ressource])
  #si les ressources peuvent être fabriquées...
  if ressource in fabrication:
    #garde une trace de si l'on a de ces ressources
    #pour fabriquer cet élément
    peutEtreFabrique = True
    #pour chaque élément nécessaire pour fabriquer cette ressource
    for i in fabrication[ressource]:
      #... is l'on n'en a pas assez...
      if fabrication[ressource][i] > inventaire[i]:
      #... on peut le fabriquer !
        peutEtreFabrique = False
        break
    #si l'on peut le fabriquer (que l'on a les ressources nécessaires)
    if peutEtreFabrique == True:
      #prendre chacun des éléments de l'inventaire
      for i in fabrication[ressource]:
        inventaire[i] -= fabrication[ressource][i]
      #ajoute le bloc fabriqué à l'inventaire
      inventaire[ressource] += 1
      print('    Fabrication de', noms[ressource], 'effectuée')
    #sinon la ressource ne peut être fabriquée...
    else:
      print('    ', noms[ressources],'ne peut être fabriqué')
    #met à jour l'affichage de l'inventaire
    dessineInventaire()

#créer une fonction pour placer chacune des ressources
def faireplace(ressource):
  return lambda: place(ressource)

#attacher une fonction "placer" à chaque touche appuyé
def lieTouchesPlacements():
  for k in touchesPlacement:
    ecran.onkey(faireplace(k),touchesPlacement[k])

#créer une fonction pour fabriquer chaque ressource
def faireLaFabrication(ressource):
  return lambda: fabrique(ressource)

#attacher une fonction "fabriquer" à chaque touche appuyée
def lieToucheFabrication():
  for k in touchesFabrication:
    ecran.onkey(faireLaFabrication(k),touchesFabrication[k])

#dessiner une ressource à la position (y,x)
def dessineRessource(y, x):
  #cette variable arrête toute les autres choses qui sont en train d'être dessinées
  global dessine
  #dessine seulement si rien d'autre n'est dessiné
  if dessine == False:
    #quelque chose se dessine donc
    dessine = True
    #dessine la ressource à cette position sur la carte, en utilisant la bonne image
    TdeRendu.goto( (y * TAILLETUILE) + 20, hauteur - (x * TAILLETUILE) - 20 )
    #dessine la tuile avec la bonne texture
    texture = textures[carte[y][x]]
    tdeRendu.shape(texture)
    TdeRendu.stamp()
    if playerX == y and playerY == x:
      rendererT.shape(playerImg)
      TdeRendu.stamp()
    ecran.update()
    #rien d'autre n'est dessiné maintenant
    dessine = False
    
#dessiner la carte du monde
def dessineCarte():
  #boucle pour chaque ligne
  for ligne in range(HAUTEURCARTE):
    #boucle pour chaque colonne dans la ligne
    for colonne in range(LARGEURCARTE):
      #dessine la tuile à la position actuelle
      dessineRessource(colonne, ligne)

#dessiner l'inventaire à l'écran
def dessineInventaire():
  #cette variable arrête toute les autres choses qui sont en train d'être dessinées
  global dessine
  #dessine seulement si rien d'autre n'est dessiné
  if dessine == False:
    #quelque chose se dessine donc
    dessine = True
    #utilise un rectangle pour couvrir l'inventaire actuel
    TdeRendu.color(COULEURDEFOND)
    TdeRendu.goto(0,0)
    TdeRendu.begin_fill()
    #TdeRendu.setheading(0)
    for i in range(2):
      TdeRendu.forward(hauteur_inventaire - 60)
      TdeRendu.right(90)
      TdeRendu.forward(largeur)
      TdeRendu.right(90)
    TdeRendu.end_fill()
    rendererT.color('black')
    #affiche le texte de "placement" et de "fabrication"
    for i in range(1,nb_ligne+1):
      TdeRendu.goto(20, (hauteur - (HAUTEURCARTE * TAILLETUILE)) - 20 - (i * 100))
      TdeRendu.write('placer')
      TdeRendu.goto(20, (hauteur - (HAUTEURCARTE * TAILLETUILE)) - 40 - (i * 100))
      TdeRendu.write('fabriquer')
    #paramètre la position de l’inventaire
    xPosition = 70
    yPosition = hauteur- (HAUTEURCARTE* TAILLETUILE) - 80
    numElement = 0
    for i, element in enumerate(ressources):
      #ajoute l'image
      TdeRendu.goto(xPosition, yPosition)
      TdeRendu.shape(textures[element])
      TdeRendu.stamp()
      #ajoute le numéro dans l'inventaire
      TdeRendu.goto(xPosition, yPosition - TAILLETUILE)
      TdeRendu.write(inventaire[element])
      #ajoute la touche de placement
      TdeRendu.goto(xPosition, yPosition - TAILLETUILE - 20)
      TdeRendu.write(touchesPlacement[element])
      #ajoute la touche de fabrication
      if fabrication.get(element) != None:
        TdeRendu.goto(xPosition, yPosition - TAILLETUILE - 40)
        TdeRendu.write(touchesFabrication[element])     
      #se déplace sur la longueur pour placer l'élément d'inventaire suivant
      xPosition += 50
      numElement += 1
      #Retourne à la ligne au bout de 10 éléments
      if numElement % LARGEURINV == 0:
        xPosition = 70
        numElement = 0
        yPosition -= TAILLETUILE + 80
    dessine = False

#générer les instructions ainsi que les règles de fabrication
def genereInstructions():
  instructions.append('Règles de fabrications:')
  #pour chaque ressource qui peuvent être fabriquées...
  for regle in fabrication:
    #crée le texte de la règle de fabrication
    regleFabrication = noms[regle] + '='
    for ressource, nombre in fabrication[regle].items():
      regleFabrication += str(nombre) + ' ' + noms[ressource] + ' '
    #ajoute la règle de fabrication aux instructions
    instructions.append(regleFabrication)
  #affiche les instructions
  yPos = hauteur - 20
  for element in instructions:
    TdeRendu.goto( LARGEURCARTE *TAILLETUILE + 40, yPos)
    TdeRendu.write(element)
    yPos-=20

#génération d'un monde aléatoire
def genereUnMondeAleatoire():
  #boucle pour chaque ligne
  for ligne in range(HAUTEURCARTE):
    #boucle pour chaque colonne dans la ligne
    for colonne in range(LARGEURCARTE):
      #choisit un nomre aléatoire ente 0 et 10
      nombreAleatoire = random.randint(0,10)
      #EAU si le nombre aléatoire est entre 1 et 2
      if nombreAleatoire in [1,2]:
        tuile= EAU
      #HERBE si le nombre aléatoire est entre 3 et 4
      elif nombreAleatoire in [3,4]:
        tuile = HERBE
      #BOIS si c'est un 5
      elif nombreAleatoire == 5:
        tuile = BOIS
      #SABLE si c'est un 6
      elif nombreAleatoire == 6:
        tuile = SABLE
      #sinon c'est de la TERRE
      else:
        tuile = TERRE
      #paramètre à la position de la carte, la tuile choisie aléatoirement
      carte[colonne][ligne] = tuile

#---
#le code commence à être exécuté ici
#---

#importation des modules et des variables requises
import turtle
import random
from variables import *
from math import ceil

TAILLETUILE = 20
#le nombre de ressource par rangée de l'inventaire
LARGEURINV = 8
dessine = False

#crée un nouvel objet 'ecran'
ecran = turtle.Screen()
#calcule la largeur et la hauteur
largeur = (TAILLETUILE * LARGEURCARTE) + max(200,LARGEURINV * 50)
nb_ligne = int(ceil((len(ressources) / LARGEURINV)))
hauteur_inventaire = nb_ligne * 120  + 40
hauteur = (TAILLETUILE * HAUTEURCARTE) + hauteur_inventaire

ecran.setup(largeur, hauteur)
ecran.setworldcoordinates(0,0,largeur,hauteur)
ecran.bgcolor(COULEURDEFOND)
ecran.listen()

#déclare l'image du joueur  
ecran.register_shape(imgJoueur)
#déclare toutes les images des ressources
for texture in textures.values():
  ecran.register_shape(texture)

#crée une autre tortue pour faire les dessins grafiques
TdeRendu = turtle.Turtle()
TdeRendu.hideturtle()
TdeRendu.penup()
TdeRendu.speed(0)
TdeRendu.setheading(90)

#crée un monde avec des ressources aléatoires.
carte = [ [TERRE for l in range(HAUTEURCARTE)] for h in range(LARGEURCARTE) ]

#tracer les touches pour se déplacer et récolter des ressources avec les bonnes fonctions.
ecran.onkey(deplaceHaut, 'z')
ecran.onkey(deplaceBas, 's')
ecran.onkey(deplaceGauche, 'q')
ecran.onkey(deplaceDroite, 'd')
ecran.onkey(ramasse, 'space')

#paramètre les touches pour placer et fabriquer chaque ressource
lieTouchesPlacements()
lieToucheFabrication()

#ces fonctions sont définies ci-dessus
genereUnMondeAleatoire()
dessineCarte()
dessineInventaire()
genereInstructions()


