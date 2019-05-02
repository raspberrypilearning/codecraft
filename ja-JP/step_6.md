## 新しい木のリソースを作成

新しい木のリソース（WOOD）を作りましょう。 そのために、`variables.py` ファイルにいくつかの変数を追加します。

+ 最初に、新しいリソースに番号を振る 。 そして、単語 `WOOD` を4として使う。
    
    ![スクリーンショット](images/craft-wood-const.png)

+ 新しいリソース`WOOD` を`resources`リストに追加。
    
    ![スクリーンショット](images/craft-wood-resources.png)

+ リソースにはインベントリに表示される名前を付ける必要があります。
    
    ![スクリーンショット](images/craft-wood-name.png)
    
    リストに新しいアイテムを追加する際、”`,`”を追加するのを忘れないように。

+ 新しいリソースには画像が必要。 このプロジェクトはすでに`wood.gif`という画像が含まれています。それを`textures` に追加してください。
    
    ![スクリーンショット](images/craft-wood-texture.png)

+ `Inventory` のWOOD リソースに初期値を設定。
    
    ![スクリーンショット](images/craft-wood-inventory.png)

+ 最後に、木をワールドに配置するための数字をplacekeysに追加。
    
    ![スクリーンショット](images/craft-wood-placekey.png)

+ プロジェクトを実行し、テスト。 木のリソース（WOOD）が持ち物リストにあることを確認。
    
    ![スクリーンショット](images/craft-wood-test.png)

+ ワールドに木がない！ `main.py`ファイルを開き、関数`generateRandomWorld()`を修正します。
    
    ![スクリーンショット](images/craft-wood-random1.png)
    
    このコードは0から10の乱数を生成し、その番号によりどのリソースをはいちするかけっていします。
    
    + 1 か 2 = 水
    + 3 か 4 = 草
    + それ以外 = 土

+ コードを追加し、`randomNumber` が 5だったら木を追加するようにする。
    
    ![スクリーンショット](images/craft-wood-random2.png)

+ プロジェクトをテストする。 今回はワールドに木があるはずです。
    
    ![スクリーンショット](images/craft-wood-test2.png)