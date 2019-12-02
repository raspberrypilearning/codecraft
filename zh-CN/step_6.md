## 创建一个新的木材资源

让我们创建一个新的木材资源。 为此，您需要在` variables.py中添加一些变量`文件。

+ 首先，您需要给新资源一个数字。 然后，您将可以使用单词` WOOD `在您的代码中而不是数字4中。
    
    ![screenshot](images/craft-wood-const.png)

+ 您应该添加新的` WOOD `资源到您的`资源列表中` 。
    
    ![screenshot](images/craft-wood-resources.png)

+ 您还应该给资源指定一个名称，该名称将显示在清单中。
    
    ![screenshot](images/craft-wood-name.png)
    
    注意逗号`， `在上面一行的末尾。

+ 您的资源还将需要一张图片。 该项目已经包含名为` wood.gif的图像。 ` ，应将其添加到`纹理中`字典。
    
    ![screenshot](images/craft-wood-texture.png)

+ 添加应该在您的`库存中的资源编号`首先。
    
    ![screenshot](images/craft-wood-inventory.png)

+ 最后，添加您要在世界上放置木头的按键。
    
    ![screenshot](images/craft-wood-placekey.png)

+ 运行你的代码进行测试。 您会看到清单中现在有了新的“木材”资源。
    
    ![screenshot](images/craft-wood-test.png)

+ 您的世界没有木头！ 要解决此问题，请单击您的` main.py `文件并找到名为` generateRandomWorld（）的函数` 。
    
    ![screenshot](images/craft-wood-random1.png)
    
    此代码生成一个介于0到10之间的随机数，并使用该数字来决定放置哪个资源：
    
    + 1或2 =水
    + 3或4 =草
    + 其他= DIRT

+ 当`随机编号` 是5时，添加此代码以添加木头到你的世界。
    
    ![screenshot](images/craft-wood-random2.png)

+ 再次测试你的程序。 这次，您应该看到世界上出现了一些木头。
    
    ![screenshot](images/craft-wood-test2.png)