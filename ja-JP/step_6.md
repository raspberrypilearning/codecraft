## 新しい木のリソースを作成

新しい木のリソース（WOOD）を作りましょう。 そのために、`variables.py` ファイルにいくつかの変数を追加します。

+ 最初に、新しいリソースに番号を振ります 。 それで、単語 `WOOD` を数字の4の代わりとして使うことができるようになります。
    
    ![スクリーンショット](images/craft-wood-const.png)

+ 新しいリソース`WOOD` を`resources`リストに追加します。
    
    ![スクリーンショット](images/craft-wood-resources.png)

+ リソースには持ち物リストに表示される名前を付ける必要があります。
    
    ![スクリーンショット](images/craft-wood-name.png)
    
    1つ上の行の最後にコンマ”`,`”を追加するのを忘れないように。

+ 新しいリソースには画像も必要です。 このプロジェクトはすでに`wood.gif`という画像が含まれています。それを`textures` ディクショナリに追加してください。
    
    ![スクリーンショット](images/craft-wood-texture.png)

+ `Inventory` のWOOD リソース個数の初期値を設定します。
    
    ![スクリーンショット](images/craft-wood-inventory.png)

+ Finally, add the key that you'll press to place wood in the world.
    
    ![screenshot](images/craft-wood-placekey.png)

+ Run your project to test it. You'll see that you now have a new 'wood' resource in your inventory.
    
    ![screenshot](images/craft-wood-test.png)

+ There's no wood in your world! To fix this, click on your `main.py` file and find the function called `generateRandomWorld()`.
    
    ![screenshot](images/craft-wood-random1.png)
    
    This code generates a random number between 0 and 10, and uses the number to decide which resource to place:
    
    + 1 or 2 = water
    + 3 or 4 = grass
    + anything else = DIRT

+ Add this code to add wood to your world whenever the `randomNumber` is 5.
    
    ![screenshot](images/craft-wood-random2.png)

+ Test your project again. This time, you should see some wood appear in your world.
    
    ![screenshot](images/craft-wood-test2.png)