## लकड़ी से तख्ते बनाना

Let's create a new plank resource that be crafted from wood.

+ First, add a new `PLANK` variable to your game.
    
    ![स्क्रीनशॉट](images/craft-plank-const.png)

+ Add a new `PLANK` variable to your game.
    
    ![स्क्रीनशॉट](images/craft-plank-resources.png)

+ Name the resource `'plank'`.
    
    ![स्क्रीनशॉट](images/craft-plank-names.png)

+ Give your `PLANK` resource an image. The project already contains a `plank.gif` image, but you can create your own if you prefer.
    
    ![स्क्रीनशॉट](images/craft-plank-textures.png)

+ Add planks to your inventory.
    
    ![स्क्रीनशॉट](images/craft-plank-inventory.png)

+ Set a key for placing planks.
    
    ![स्क्रीनशॉट](images/craft-plank-placekeys.png)

+ As this resource can be crafted, you need to create a crafting rule, which is that a plank can be made from 3 wood tiles. Add this code to the `crafting` dictionary.
    
    ![स्क्रीनशॉट](images/craft-plank-crafting.png)

+ Finally, you need to set a key for crafting new planks.
    
    ![स्क्रीनशॉट](images/craft-plank-craftkeys.png)

+ To test your new plank resource, gather up a few wood tiles and then craft some planks from your wood. You can then place your new planks in your world.
    
    ![स्क्रीनशॉट](images/craft-plank-test.png)