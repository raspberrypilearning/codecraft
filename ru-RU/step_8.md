## Сделать доски из дерева

Давайте создадим новый ресурс «доска», который будет сделан из дерева.

+ Сначала определите в вашей игре новую переменную `PLANK`.
    
    ![screenshot](images/craft-plank-const.png)

+ Добавьте новую переменную `PLANK` в список ресурсов вашей игры.
    
    ![screenshot](images/craft-plank-resources.png)

+ Дайте этому ресурсу имя `'plank'`.
    
    ![screenshot](images/craft-plank-names.png)

+ Задайте изображение для своего ресурса `PLANK`. The project already contains a `plank.gif` image, but you can create your own if you prefer.
    
    ![screenshot](images/craft-plank-textures.png)

+ Добавьте блок «доска» к своим запасам в словарь inventory.
    
    ![screenshot](images/craft-plank-inventory.png)

+ Задайте клавишу для размещения досок в мире.
    
    ![screenshot](images/craft-plank-placekeys.png)

+ Поскольку этот ресурс может быть создан, вам необходимо создать правило создания, состоящее в том, что доску можно сделать из 3 деревянных блоков. Добавьте этот код в словарь `crafting`.
    
    ![screenshot](images/craft-plank-crafting.png)

+ Наконец, вам нужно задать клавишу для создания новых досок.
    
    ![screenshot](images/craft-plank-craftkeys.png)

+ Чтобы проверить свой новый ресурс «доска», соберите несколько блоков «дерево», а затем сделайте несколько досок из дерева. Затем вы можете разместить ваши новые доски в своем мире.
    
    ![screenshot](images/craft-plank-test.png)