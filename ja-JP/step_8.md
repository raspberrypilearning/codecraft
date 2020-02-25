## 木から板をクラフトする

新しく板（PLANK）リソースを木からクラフトしましょう。

+ 最初に、`PLANK`変数を追加します。
    
    ![スクリーンショット](images/craft-plank-const.png)

+ `PLANK`変数をresoucesに追加します。
    
    ![スクリーンショット](images/craft-plank-resources.png)

+ リソースを `'plank'`と名付け、namesに追加します。
    
    ![スクリーンショット](images/craft-plank-names.png)

+ `PLANK`リソースに画像を追加します。 このプロジェクトは`plank.gif` 画像を含んでいます。しかし、自分で画像を作成し、アップロードして使用することもできます。
    
    ![スクリーンショット](images/craft-plank-textures.png)

+ 持ち物リストに板を追加します。
    
    ![スクリーンショット](images/craft-plank-inventory.png)

+ Set a key for placing planks.
    
    ![screenshot](images/craft-plank-placekeys.png)

+ As this resource can be crafted, you need to create a crafting rule, which is that a plank can be made from 3 wood tiles. Add this code to the `crafting` dictionary.
    
    ![screenshot](images/craft-plank-crafting.png)

+ Finally, you need to set a key for crafting new planks.
    
    ![screenshot](images/craft-plank-craftkeys.png)

+ To test your new plank resource, gather up a few wood tiles and then craft some planks from your wood. You can then place your new planks in your world.
    
    ![screenshot](images/craft-plank-test.png)