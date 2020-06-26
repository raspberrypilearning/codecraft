## 創造新的木材資源

讓我們創建一個新的木材資源。 為此，您需要在 `variables.py` 的檔案中添加一些變數。

+ 首先，您需要先設定一個數字給新資源。 然後，您可以在程式碼中使用單字 `WOOD` 而不是數字4。
    
    ![截圖](images/craft-wood-const.png)

+ 您應該將新的 `WOOD` 資源添加到 `resources`列表中。
    
    ![截圖](images/craft-wood-resources.png)

+ 您也應該為資源指定一個名稱，該名稱將會顯示在儲存庫中。
    
    ![截圖](images/craft-wood-name.png)
    
    注意逗號 `，` 在上面圖中的最後一列的底部。

+ 您的資源也需要一張圖片。 此專案已經包含一個名稱為 `wood.gif`的圖像檔案，您可以將其添加到 `texture` 的字典中。
    
    ![截圖](images/craft-wood-texture.png)

+ 首先，添加應該在 `inventory` 中的資源數量。
    
    ![截圖](images/craft-wood-inventory.png)

+ 最後，添加將木材放入世界中您需要按下的數字鍵。
    
    ![截圖](images/craft-wood-placekey.png)

+ 執行您的專案來進行測試。 您會看到您的儲存庫中現在有了一個新的“木材”資源。
    
    ![截圖](images/craft-wood-test.png)

+ 你的世界裡沒有木材！ 要解決此問題，請點擊 `main.py` 檔案，找到名為 `generateRandomWorld()`的功能鍵。
    
    ![截圖](images/craft-wood-random1.png)
    
    此程式碼生成0到10之間的隨機數，並使用該數字來決定放置哪個資源：
    
    + 1或2 =水
    + 3或4 =草
    + 除此之外= 土

+ 添加此程式碼，只要 `randomNumber` 是5，就可以為您的世界添加木材。
    
    ![截圖](images/craft-wood-random2.png)

+ 再次測試您的專案。 這一次，您應該會看到一些木材出現在您的世界中。
    
    ![截圖](images/craft-wood-test2.png)