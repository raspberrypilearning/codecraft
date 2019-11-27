#!/bin/python3

#変更可能なゲーム変数！

#ゲームの背景色
BACKGROUNDCOLOUR = 'white'

#ゲームマップ（地図上）の変数
MAXTILES = 20  #持ち物リストに入れられるリソースの最大量
MAPWIDTH = 10  #マップの幅
MAPHEIGHT = 10 #マップの高さ

#リソースをあらわす変数
DIRT    = 0
GRASS   = 1
WATER   = 2
BRICK   = 3

#ゲームのリソース
resources = [DIRT,GRASS,WATER,BRICK]

#リソースの名前
names = {
  DIRT : u'土',
  GRASS: u'草',
  WATER: u'水',
  BRICK   : u'レンガ'
}

#リソースを画像にリンクするディクショナリ（辞書）
textures = {
  DIRT    : 'dirt.gif',
  GRASS   : 'grass.gif',
  WATER   : 'water.gif',
  BRICK   : 'brick.gif'
}

#各プレイヤーが持つリソースの数
inventory = {
  DIRT    : 10,
  GRASS   : 10,
  WATER   : 10,
  BRICK   : 0
}

#プレイヤーの画像
playerImg = 'player.gif'

#プレイヤーの位置
playerX = 0
playerY = 0

#新しいリソースを作るために押すキー
crafting = {
  BRICK    : { WATER : 1, DIRT : 2 }
}

#新しいリソースを作るために必要なリソースの数（レンガを作るためには土を２つと水を１つ必要）
placekeys = {
  DIRT  : '1',
  GRASS : '2',
  WATER : '3',
  BRICK : '4'
}

#keys for crafting tiles.
craftkeys = {
  BRICK : 'r'
}

#画面に表示されるゲームの説明（ルール
instructions =  [
  '説明:',
  'プレイヤーを左右上下に移動する場合、WASDキーを押してください'
]
