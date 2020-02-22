#!/bin/python3

#変更可能なゲーム変数！

#ゲームの背景色
BACKGROUNDCOLOUR = 'lightblue'

#ゲームマップ（地図上）の変数
MAXTILES = 40  #持ち物リストに入れられるリソースの最大量
MAPWIDTH  = 20 #マップの幅
MAPHEIGHT = 15 #マップの高さ

#リソースをあらわす変数
DIRT    = 0
GRASS   = 1
WATER   = 2
BRICK   = 3
WOOD    = 4
SAND    = 5
PLANK   = 6
GLASS   = 7

#ゲームのリソース
resources = [DIRT,GRASS,WATER,BRICK,WOOD,SAND,PLANK,GLASS]

#リソースの名前
names = {
  DIRT : u'土',
  GRASS: u'草',
  WATER: u'水',
  BRICK: u'レンガ',
  WOOD: u'木',
  SAND:  u'砂',
  PLANK : u'板',
  GLASS   : u'ガラス'
}

#リソースを画像にリンクするディクショナリ（辞書）
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

#プレイヤーが持つ各リソースの個数
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

#プレイヤーの画像
playerImg = 'player.gif'

#プレイヤーの位置
playerX = 0
playerY = 0

#リソースを配置するキー
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

#新しいリソースを作るルール
crafting = {
  BRICK    : { WATER : 1, DIRT : 2 },
  PLANK    : { WOOD : 3 },
  GLASS    : { SAND : 3 }
}

#タイルを作るキー
craftkeys = {
  BRICK : 'r',
  PLANK : 'u',
  GLASS : 'i'
}

#画面に表示されるゲームの説明
instructions =  [
  '説明:',
  'プレイヤーを左右上下に移動する場合、WASDキーを押してください'
]
