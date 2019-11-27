#!/bin/python3

#Ігрові змінні, які можна змінити!

#Колір фону.
BACKGROUNDCOLOUR = 'white'

#змінні карти.
MAXTILES  = 20
MAPWIDTH  = 10
MAPHEIGHT = 10

#змінні, що представляють різні ресурси.
DIRT    = 0
GRASS   = 1
WATER   = 2
BRICK   = 3

#список усіх ігрових ресурсів.
resources = [DIRT,GRASS,WATER,BRICK]

#назви ресурсів.
names = {
  DIRT: "земля",
  GRASS : 'трава',
  WATER : 'вода',
  BRICK : 'цегла'
}

#словник, що зв'язує ресурси з зображеннями.
textures = {
  DIRT    : 'dirt.gif',
  GRASS   : 'grass.gif',
  WATER   : 'water.gif',
  BRICK   : 'brick.gif'
}

#кількість кожного ресурсу який має гравець.
inventory = {
  DIRT    : 10,
  GRASS   : 10,
  WATER   : 10,
  BRICK   : 0
}

#зображення гравця.
playerImg = 'player.gif'

#позиція гравця.
playerX = 0
playerY = 0

#правила для створення нових ресурсів.
crafting = {
  BRICK    : { WATER : 1, DIRT : 2 }
}

#кнопки для розміщення ресурсів.
placekeys = {
  DIRT  : '1',
  GRASS : '2',
  WATER : '3',
  BRICK : '4'
}

#кнопки для створення ресурсів.
craftkeys = {
  BRICK : 'r'
}

#ігрові інструкцій, що показуються у грі.
інструкції =  [
  'Інструкції:',
  "Використовуйте WASD для переміщення"
]
