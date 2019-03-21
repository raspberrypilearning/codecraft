## 創造新的木材資源

讓我們創建一個新的木材資源。 為此，您需要在 `variables.py` 文件中添加一些變量。

+ 首先，您需要為新資源提供一個數字。 然後，您可以在代碼中使用單詞 `WOOD` 而不是數字4。
    
    ![截圖](images/craft-wood-const.png)

+ 您應該將新的 `WOOD` 資源添加到 `資源列表中`。
    
    ![截圖](images/craft-wood-resources.png)

+ 您還應該為資源指定一個名稱，該名稱將顯示在清單中。
    
    ![截圖](images/craft-wood-name.png)
    
    注意逗號 `，` 在上面的行的端部。

+ 您的資源還需要一張圖片。 該項目已經包含一個名為 `wood.gif`的圖像，您應該將其添加到 `texture` 字典中。
    
    ![截圖](images/craft-wood-texture.png)

+ 添加應該在 `庫存` 中的資源編號。
    
    ![截圖](images/craft-wood-inventory.png)

+ 最後，添加您要按下的鍵以將木材放入世界中。
    
    ![截圖](images/craft-wood-placekey.png)

+ 運行您的項目以進行測試。 您會看到您的庫存中現在有了一個新的“木材”資源。
    
    ![截圖](images/craft-wood-test.png)

+ 你的世界裡沒有木頭！ 要解決此問題，請單擊您的 `main.py` 文件，找到名為 `generateRandomWorld（）的函數`。
    
    ![截圖](images/craft-wood-random1.png)
    
    此代碼生成0到10之間的隨機數，並使用該數字來決定放置哪個資源：
    
    + 1或2 =水
    + 3或4 =草
    + 別的什麼= DIRT

+ 添加此代碼，只要 `randomNumber` 為5，就可以為您的世界添加木材。
    
    ![截圖](images/craft-wood-random2.png)

+ 再次測試您的項目。 這一次，您應該會看到一些木材出現在您的世界中。
    
    ![截圖](images/craft-wood-test2.png)