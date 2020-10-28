#!/bin/python3

#############
# CodeCraft #
#############

#---
#Funções do Jogo
#---

#Move o jogador 1 bloco à esquerda.
def moverEsquerda():
  global posicao_x
  if(drawing == False and playerX > 0):
    oldX = playerX
    posicao_x -= 1
    drawResource(oldX, playerY)
    desenhar_recurso(posicao_x, posicao_y)
    
#Move o jogador 1 bloco à direita.
def moverDireita():
  global posicao_x, LARGURA_MAPA
  if(drawing == False and playerX < MAPWIDTH - 1):
    oldX = playerX
    posicao_x += 1
    drawResource(oldX, playerY)
    desenhar_recurso(posicao_x, posicao_y)
    
#Move o jogador 1 bloco para cima.
def moverCima():
  global posicao_y
  if(drawing == False and playerY > 0):
    oldY = playerY
    posicao_y -= 1
    drawResource(playerX, oldY)
    desenhar_recurso(posicao_x, posicao_y)
    
#Move o jogador 1 bloco para baixo.
def moverBaixo():
  global posicao_y, ALTURA_MAPA
  if(drawing == False and playerY < MAPHEIGHT - 1):
    oldY = playerY
    posicao_y += 1
    drawResource(playerX, oldY)
    desenhar_recurso(posicao_x, posicao_y)
    
#Coleta o recurso que esta na mesma posição que o jogador.
def Coletar():
  global posicao_x, posicao_y
  desenhar = True
  posicao_atual = mundo[posicao_x][posicao_y]
  #Se o jogador não tiver atingido o limite de blocos do mesmo tipo no inventário.
  if inventario[posicao_atual] < MAX_BLOCOS:
    #O jogador terá mais 1 unidade do recurso coletado
    inventario[posicao_atual] += 1
    #E o bloco da posição atual do jogador será TERRA
    mundo[posicao_x][posicao_y] = TERRA
    #Colocar a imagem do bloco TERRA na posição do jogador
    desenhar_recurso(posicao_x, posicao_y)
    #Redefinir o inventário com o recurso coletado.
    desenhar_inventario()
    #desenhar_j()

#Colocar o recurso selecionado na posição atual do jogador
def colocar(recurso):
  print('Colocando: ', nomes[recurso])
  #Só colocar o recurso se o jogador tiver disponível no inventário.
  if inventario[recurso] > 0:
    #Colocar o recurso na posição do jogador 
    posicao_atual = mundo[posicao_x][posicao_y]
    #Coletar o recurso que esta na mesma posição que o jogador
    #(Somente se não for TERRA)
    if posicao_atual is not TERRA:
      inventario[posicao_atual] += 1
    #Colocar o recurso na posição do jogador
    mundo[posicao_x][posicao_y] = recurso
    #Subtrair 1 unidade do recuso do inventário
    inventory[resource] -= 1
    #Redesenhar o inventário e o mundo
    desenhar_recurso(posicao_x, posicao_y)
    desenhar_inventario()
    #desenhar_j()
    print('   ', nomes[recurso], 'colocado')
  #E se não tiver o recurso no inventário
  else:
    print('   Você não tem', nomes[recurso], 'disponível')

#Fabricar um novo recurso
def fabricar(recurso):
  print('Fabricar: ', nomes[recurso])
  #Se o recurso puder ser fabricado
  if recurso in fabricando:
    #Verificar se há recursos suficientes
    #Para fabricar o novo recurso
    pode_ser_feito = True
    #Para cada item necessário para fabricar o recurso
    for i in fabricando[recurso]:
      #Caso não tenha recursos suficientes
      if fabricando[recurso][i] > inventario[i]:
      #O item não será feito
        pode_ser_feito = False
        break
    #Se o recurso puder se fabricado(Todos os recursos necessários estiverem no inventário)
    if pode_ser_feito == True:
      #Retirar os recursos necessários do inventário
      for i in fabricando[recurso]:
        inventario[i] -= fabricando[recurso][i]
      #Adicionar o recurso fabricado no inventário e imprimir a seguinte mensagem
      inventario[recurso] += 1
      print('   O recurso', nomes[recurso], 'foi fabricado com sucesso!')
    #Caso o recurso não possa ser fabricado e imprimir a mensagem de erro
    else:
      print('   Não foi possível fabricar', nomes[recurso])
    #Redesenhar o inventário
    desenhar_inventario()

#Cria uma função para colocar cada recurso
def colocar_r(recurso):
  return lambda: colocar(recurso)

#Vincula a função 'colocando' a cada vez que a tecla 'x' for pressionada
def vinc_colocando():
  for k in chaves_colocar:
    tela.onkey(colocar_r(k), chaves_colocar[k])

#Cria uma função para fabricar cada recurso
def fabricar_r(recurso):
  return lambda: fabricar(recurso)

#Vincular a função 'fabricar' a cada vez que a tecla 'x' for pressionada
def vinc_fabricar():
  for k in chaves_fabricar:
    tela.onkey(fabricar_r(k), chaves_fabricar[k])

#Desenha o recurso na posição (y,x)
def desenhar_recurso(y, x):
  #Esta variável impede que outros recursos sejam desenhados simultaneamente
  global desenhar
  #Somente desenhar se nenhum outro recurso estiver sendo desenhado
  if desenhar == False:
    #Algo esta sendo desenhado agora
    desenhar = True
    #Desenha o recurso na posição do mapa, usando a imagem correta
    tornar_r.goto( (y * TAMANHO_BLOCO) + 20, altura - (x * TAMANHO_BLOCO) - 20 )
    #Desenha o bloco com a imagem correta
    textura = texturas[mundo[y][x]]
    tornar_r.shape(textura)
    tornar_r.stamp()
    if playerX == y and playerY == x:
      rendererT.shape(playerImg)
      tornar_r.stamp()
    tela.update()
    #Nada esta sendo desenhado no momento
    desenhar = False
    
#Desenha o mapa do jogo
def desenhar_m():
  #Desenhar uma linha por vez
  for linha in range(ALTURA_MAPA):
    #Desenha todas as colunas dentro de cada linha
    for coluna in range(LARGURA_MAPA):
      #Desenha o recurso em cada posição do mapa
      desenhar_recurso(coluna, linha)

#Desenha o inventário
def desenhar_inventario():
  #Esta variável impede que outros recursos sejam desenhados simultaneamente
  global desenhar
  #Somente desenhar se nenhum outro recurso estiver sendo desenhado
  if desenhar == False:
    #Algo esta sendo desenhado agora
    desenhar = True
    #Use um retângulo para definir a cor do pano de fundo do inventário
    tornar_r.color(COR_PANODEFUNDO)
    tornar_r.goto(0,0)
    tornar_r.begin_fill()
    #Tornar_r.setheading(0)
    for i in range(2):
      tornar_r.forward(inventario_altura - 60)
      tornar_r.right(90)
      tornar_r.forward(largura)
      tornar_r.right(90)
    tornar_r.end_fill()
    rendererT.color('black')
    #Mostrar os nomes das linhas do inventário
    for i in range(1,num_linhas+1):
      tornar_r.goto(20, (altura - (ALTURA_MAPA * TAMANHO_BLOCO)) - 20 - (i * 100))
      tornar_r.write("Colocar")
      tornar_r.goto(20, (altura - (ALTURA_MAPA * TAMANHO_BLOCO)) - 40 - (i * 100))
      tornar_r.write("Fabricar")
    #Definir a posição do inventário
    inventario_x = 70
    yPostition = height - (MAPHEIGHT * TILESIZE) - 60
    itemNum = 0
    for i, item in enumerate(recursos):
      #Adicionar as imagens
      rendererT.goto(xPosition + 10, yPostition)
      tornar_r.shape(texturas[item])
      tornar_r.stamp()
      #Adiciona os números das quantidades dos recursos no inventário
      tornar_r.goto(inventario_x, inventario_y - TAMANHO_BLOCO)
      tornar_r.write(inventario[item])
      #add the name
      tornar_r.goto(inventario_x, inventario_y - TAMANHO_BLOCO - 20)
      rendererT.write('[' + names[item] + ']')
      #Adiciona as teclas para adicionar cada um dos recursos no inventário
      tornar_r.goto(inventario_x, inventario_y - TAMANHO_BLOCO - 40)
      tornar_r.write(chaves_colocar[item])
      #Adiciona as teclas para fabricar os recursos
      if fabricando.get(item) != None:
        rendererT.goto(xPosition, yPostition - TILESIZE - 60)
        tornar_r.write(chaves_fabricar[item])     
      #Coloca cada um dos recursos no inventário
      inventario_x += 50
      itemNum += 1
      #Adiciona uma nova linha no inventários a cada 10 itens
      if itemNum % INV_LARGURA == 0:
        inventario_x = 70
        itemNum = 0
        inventario_y -= TAMANHO_BLOCO + 80
    desenhar = False

#Cria as instruções, inclusive as regras para fabricar recursos
def criar_instrucoes():
  instrucoes.append('Regras para fabricar novos recursos:')
  #Para cada recurso que pose ser fabricado
  for regra in fabricando:
    #Criar um texto com os recursos necessários
    fabricar_regra = nomes[regra] + ' = '
    for recurso, numero in fabricando[regra].items():
      fabricar_regra += str(numero) + ' ' + nomes[recurso] + ' '
    #Adiciona as regras para fabricar às instruções
    instrucoes.append(fabricar_regra)
  #Exibir instruções
  instrucoes_y = altura - 20
  for item in instrucoes:
    tornar_r.goto( LARGURA_MAPA*TAMANHO_BLOCO + 40, instrucoes_y)
    tornar_r.write(item)
    instrucoes_y-=20

#Criar um mundo aleatório a cada jogo
def criar_mundo_alt():
  #Desenhar uma linha por vez
  for linha in range(ALTURA_MAPA):
    #Desenhar em todas as colunas de cada linha
    for coluna in range(LARGURA_MAPA):
      #Seleciona aleatoriamente um número de 1 a 10
      numero_alt = random.randint(0,10)
      #AGUA se o número for 1 ou 2
      if numero_alt in [1,2]:
        bloco = AGUA
      #GRAMA se o número for 3 ou 4
      elif numero_alt in [3,4]:
        bloco = GRAMA
      #Os demais número serão TERRA
      else:
        bloco = TERRA
      #Definir a posição no mapa para o recurso escolhido aleatoriamente
      mundo[coluna][linha] = bloco

#---
#O código começa a ser executado aqui
#---

#Importar os módulos e variáveis necessárias
import turtle
import random
from variables import *
from math import ceil

TAMANHO_BLOCO = 20
#O número de recursos no inventário por linha
INV_LARGURA = 8
desenhar = False

#Cria um novo objeto para a 'tela'
tela = turtle.Screen()
#Calcula a largura e a altura da tela
largura = (TAMANHO_BLOCO * LARGURA_MAPA) + max(200,INV_LARGURA * 50)
num_linhas = int(ceil((len(recursos) / INV_LARGURA)))
inventario_altura =  num_linhas * 120 + 40
altura = (TAMANHO_BLOCO * ALTURA_MAPA) + inventario_altura

tela.setup(largura, altura)
tela.setworldcoordinates(0,0,largura,altura)
tela.bgcolor(COR_PANODEFUNDO)
tela.listen()

#Registra a imagem do jogador  
tela.register_shape(img_jogador)
#Registra a imagem de cada um dos recursos
for textura in texturas.values():
  tela.register_shape(textura)

#Cria outra turtle para desenhar o mapa
tornar_r = turtle.Turtle()
tornar_r.hideturtle()
tornar_r.penup()
tornar_r.speed(0)
tornar_r.setheading(90)

#Cria um mundo com recursos aleatórios
mundo = [ [TERRA for w in range(ALTURA_MAPA)] for h in range(LARGURA_MAPA) ]

#Define as teclas para mover o personagem, e coletar os recursos. Para coletar os recursos, pressione a tecla 'Espaço'
tela.onkey(moverCima, 'w')
tela.onkey(moverBaixo, 's')
tela.onkey(moverEsquerda, 'a')
tela.onkey(moverDireita, 'd')
tela.onkey(Coletar, ' ')

#Define as teclas para 'colocar' e 'fabricar' cada recurso
vinc_colocando()
vinc_fabricar()

#Esta funções foram definidas acima
criar_mundo_alt()
desenhar_m()
desenhar_inventario()
criar_instrucoes()
