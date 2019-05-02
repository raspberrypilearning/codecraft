## 木から板をクラフトする

新しいリソース板（PLANK）を木からクラフトしましょう。

+ 最初に、`PLANK`変数を追加。
    
    ![スクリーンショット](images/craft-plank-const.png)

+ `PLANK`変数をresoucesに追加。
    
    ![スクリーンショット](images/craft-plank-resources.png)

+ リソースに `'plank'`と名付け、namesに追加。
    
    ![スクリーンショット](images/craft-plank-names.png)

+ `PLANK`リソースに画像を追加。 このプロジェクトは`plank.gif` 画像を含んでいます。しかし、自分の画像を作成してアップロードして使用することもできます。
    
    ![スクリーンショット](images/craft-plank-textures.png)

+ 持ち物リストに板を追加。
    
    ![スクリーンショット](images/craft-plank-inventory.png)

+ 板を置くキーを設定。
    
    ![スクリーンショット](images/craft-plank-placekeys.png)

+ この板リソースはクラフトできるものなので、３つの木リソースからクラフトするルールを作成。 そのルールを`crafting`辞書に追加。
    
    ![スクリーンショット](images/craft-plank-crafting.png)

+ 板リソースをクラフトするキーを追加。 
    
    ![スクリーンショット](images/craft-plank-craftkeys.png)

+ 板リソースをテストするために、木リソースを集めて板リソースをクラフトする。 ワールドに板リソースが配置できます。
    
    ![スクリーンショット](images/craft-plank-test.png)