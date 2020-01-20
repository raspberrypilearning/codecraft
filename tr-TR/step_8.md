## Crafting planks from wood

Let's create a new plank resource that be crafted from wood.

+ First, add a new `PLANK` variable to your game.
    
    ![ekran görüntüsü](images/craft-plank-const.png)

+ Add a new `PLANK` variable to your game.
    
    ![ekran alıntısı](images/craft-plank-resources.png)

+ Name the resource `'plank'`.
    
    ![ekran görüntüsü](images/craft-plank-names.png)

+ Give your `PLANK` resource an image. The project already contains a `plank.gif` image, but you can create your own if you prefer.
    
    ![ekran görüntüsü](images/craft-plank-textures.png)

+ Add planks to your inventory.
    
    ![ekran görüntüsü](images/craft-plank-inventory.png)

+ Set a key for placing planks.
    
    ![ekran görüntüsü](images/craft-plank-placekeys.png)

+ As this resource can be crafted, you need to create a crafting rule, which is that a plank can be made from 3 wood tiles. Add this code to the `crafting` dictionary.
    
    ![ekran görüntüsü](images/craft-plank-crafting.png)

+ Finally, you need to set a key for crafting new planks.
    
    ![ekran görüntüsü](images/craft-plank-craftkeys.png)

+ To test your new plank resource, gather up a few wood tiles and then craft some planks from your wood. You can then place your new planks in your world.
    
    ![ekran görüntüsü](images/craft-plank-test.png)