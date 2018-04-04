## 利用木材制作木板

让我们创建一个可以使用木材制作的新木板资源。

+ 首先，向你的游戏添加一个新的 `PLANK`（木板）变量。

    ![screenshot](images/craft-plank-const.png)

+ 向你的游戏添加一个新的 `PLANK`（木板）变量。

    ![screenshot](images/craft-plank-resources.png)

+ 将该资源命名为 `'plank'`（木板）。

    ![screenshot](images/craft-plank-names.png)

+ 为你的 `PLANK`（木板）资源提供一张图片。项目中已包含一张 `plank.png` 图片，但如果你愿意的话，你可以创建你自己的图片。

    ![screenshot](images/craft-plank-textures.png)

+ 向你的库存添加木板。

    ![screenshot](images/craft-plank-inventory.png)

+ 设置一个放置木板的按键。

    ![screenshot](images/craft-plank-placekeys.png)

+ 由于该资源可被制作出来，你需要创建一个制作规则，即 1 块木板可由 3 个木材块制成。向 `crafting`（制作）字典添加此代码。 

    ![screenshot](images/craft-plank-crafting.png)

+ 最后，你需要设置制作新木板的按键。

    ![screenshot](images/craft-plank-craftkeys.png)

+ 要测试你的新木板资源，将一些木材块聚集起来，然后利用这些木材块制作一些木板。你随后可以在你的世界中放置新木板。

    ![screenshot](images/craft-plank-test.png)



