#!/bin/python3

#Ігрові змінні, які можна змінити!

#Колір фону.
BACKGROUNDCOLOUR = 'lightblue'

#змінні карти.
MAXTILES  = 40
MAPWIDTH  = 20
MAPHEIGHT = 15

#змінні, що представляють різні ресурси.
DIRT    = 0
GRASS   = 1
WATER   = 2
BRICK   = 3
WOOD    = 4
SAND    = 5
PLANK   = 6
GLASS   = 7

#список усіх ігрових ресурсів.
resources = [DIRT,GRASS,WATER,BRICK,WOOD,SAND,PLANK,GLASS]

#назви ресурсів.
names = {
  DIRT: "земля",
  GRASS : 'трава',
  WATER : 'вода',
  BRICK : 'цегла',
  WOOD : 'дерево',
  SAND : 'пісок',
  PLANK : 'дошка',
  GLASS : 'скло'
}

#словник, що зв'язує ресурси з зображеннями.
textures = {
  DIRT    : 'dirt.gif',
  GRASS   : 'grass.gif',
  WATER   : 'water.gif',
  BRICK   : 'brick.gif',
  WOOD    : 'wood.gif',
  SAND    : 'sand.gif',
  PLANK   : 'plank.gif',
  GLASS   : 'glass.gif'
}

#кількість кожного ресурсу який має гравець.
inventory = {
  DIRT    : 10,
  GRASS   : 10,
  WATER   : 10,
  BRICK   : 0,
  WOOD    : 5,
  SAND    : 5,
  PLANK   : 0,
  GLASS   : 0
}

#зображення гравця.
playerImg = 'player.gif'

#позиція гравця.
playerX = 0
playerY = 0

#кнопки для розміщення ресурсів.
placekeys = {
  DIRT  : '1',
  GRASS : '2',
  WATER : '3',
  BRICK : '4',
  WOOD  : '5',
  SAND  : '6',
  PLANK : '7',
  GLASS : '8'
}

#правила для створення нових ресурсів.
crafting = {
  BRICK    : { WATER : 1, DIRT : 2 },
  PLANK    : { WOOD : 3 },
  GLASS    : { SAND : 3 }
}

#кнопки для створення ресурсів.
craftkeys = {
  BRICK : 'r',
  PLANK : 'u',
  GLASS : 'i'
}

#ігрові інструкцій, що показуються у грі.
інструкції =  [
  'Інструкції:',
  "Використовуйте WASD для переміщення"
]
