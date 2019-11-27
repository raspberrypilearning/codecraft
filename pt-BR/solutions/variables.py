#!/bin/python3

#Variáveis do jogo que podem ser alteradas!

#Cor do pano de fundo do jogo.
COR_PANODEFUNDO = 'lightblue'

#Variáveis do mapa.
MAX_BLOCOS = 40
LARGURA_MAPA = 20
ALTURA_MAPA = 15

#Variáveis dos diferentes tipos de recursos e atribuição de um número para cada variável.
TERRA = 0
GRAMA = 1
AGUA = 2
TIJOLO = 3
MADEIRA = 4
AREIA = 5
TABUA = 6
VIDRO = 7

#A lista 'recursos' com todos os recursos do jogo.
recursos = [TERRA, GRAMA, AGUA, TIJOLO, MADEIRA, AREIA, TABUA, VIDRO]

#Dicionário atribuindo um nome para cada um dos recursos.
nomes = {
  TERRA : 'Terra',
  GRAMA : 'Grama',
  AGUA : 'Água',
  TIJOLO : 'Tijolo',
  MADEIRA : 'Madeira',
  AREIA : 'Areia',
  TABUA : 'Tábua',
  VIDRO : 'Vidro'
}

#Dicionário atribuindo imagens para cada um dos recursos recursos.
texturas = {
  TERRA : 'dirt.gif',
  GRAMA : 'grass.gif',
  AGUA : 'water.gif',
  TIJOLO : 'brick.gif',
  MADEIRA : 'wood.gif',
  AREIA : 'sand.gif',
  TABUA : 'plank.gif',
  VIDRO : 'glass.gif'
}

#A quantidade de cada recursos que o jogador terá no início do jogo.
inventario = {
  TERRA : 10,
  GRAMA : 10,
  AGUA : 10,
  TIJOLO : 0,
  MADEIRA : 5,
  AREIA : 5,
  TABUA : 0,
  VIDRO : 0
}

#A imagem do jogador.
img_jogador = 'player.png'

#A posição do jogador.
posicao_x = 0
posicao_y = 0

#Dicionário com as chaves para colocar cada recuso no mapa.
chaves_colocar = {
  TERRA : '1',
  GRAMA : '2',
  AGUA : '3',
  TIJOLO : '4',
  MADEIRA : '5',
  AREIA : '6',
  TABUA : '7',
  VIDRO : '8'
}

#Regras para fabricar novos recursos.
fabricando = {
  TIJOLO : { AGUA : 1, TERRA : 2 },
  TABUA : { MADEIRA : 3 },
  VIDRO : { AREIA : 3 }
}

#Dicionário com as chaves para fabricar novos recursos.
chaves_fabricar = {
  TIJOLO : 'r',
  TABUA : 'u',
  VIDRO : 'i'
}

#Instruções do jogo que serão exibidas.
instrucoes = [
  'Instruções:',
  'Use as teclas WASD para mover o seu personagem'
]
