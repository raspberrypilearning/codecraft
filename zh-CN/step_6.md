## 创建一个新的木材资源

让我们来创建一个新的木材资源。为此，你将需要在 `variables.py` 文件中添加一些变量。

+ 首选你需要给你的新资源一个编号。随后，你就可以在代码中使用 `WOOD`（木材）这个词来代替数字 4。

    ![screenshot](images/craft-wood-const.png)

+ 你应将新的 `WOOD`（木材）资源添加到你的 `resources`（资源）列表。

    ![screenshot](images/craft-wood-resources.png)

+ 你还应为你的资源命名，名称将显示在库存中。

    ![screenshot](images/craft-wood-name.png)

    请注意上文行末的逗号 `,`。

+ 你的资源还需要一张图片。项目中已包含一张名为 `wood.png` 的图片，你应该将其添加到 `textures`（材质）词典。

    ![screenshot](images/craft-wood-texture.png)

+ 添加你的 `inventory`（库存）中应包含的资源的起始数量。

    ![screenshot](images/craft-wood-inventory.png)

+ 最后，添加将木材放在世界中需要按下的按键。 

    ![screenshot](images/craft-wood-placekey.png)

+ 运行你的项目来进行测试。你会看到现在你的库存中有了一个新的“wood”（木材）资源。

    ![screenshot](images/craft-wood-test.png)

+ 你的世界中没有木材！为解决这个问题，点击你的 `main.py` 文件，找到名为 `generateRandomWorld()`（生成随机世界）的函数。

    ![screenshot](images/craft-wood-random1.png)    

    此代码会生成一个 0 到 10 之间的随机数字，并使用该数字来决定放置哪种资源：

    + 1 或 2 = water（水）
    + 3 或 4 = grass（草）
    + 任何其他数字 = DIRT（泥土）

+ 添加此代码，从而每当 `randomNumber`（随机数字）为 5 时就向你的世界添加木材。

    ![screenshot](images/craft-wood-random2.png)

+ 再次测试你的项目。这次，你会看到你的世界中出现一些木材。

    ![screenshot](images/craft-wood-test2.png)

