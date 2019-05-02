## नया लकड़ी का संसाधन बनाना

Let's create a new wood resource. To do this, you'll need to add to some variables in your `variables.py` file.

+ First, you need to give your new resource a number. You'll then be able to use the word `WOOD` in your code instead of the number 4.
    
    ![स्क्रीनशॉट](images/craft-wood-const.png)

+ You should add your new `WOOD` resource to your list of `resources`.
    
    ![स्क्रीनशॉट](images/craft-wood-resources.png)

+ You should also give your resource a name, which will be displayed in the inventory.
    
    ![स्क्रीनशॉट](images/craft-wood-name.png)
    
    Notice the comma `,` at the end of the line above.

+ Your resource will also need an image. The project already includes an image called `wood.gif`, which you should add to the `textures` dictionary.
    
    ![स्क्रीनशॉट](images/craft-wood-texture.png)

+ Add the number of your resource that should be in your `inventory` to start with.
    
    ![स्क्रीनशॉट](images/craft-wood-inventory.png)

+ Finally, add the key that you'll press to place wood in the world.
    
    ![स्क्रीनशॉट](images/craft-wood-placekey.png)

+ Run your project to test it. You'll see that you now have a new 'wood' resource in your inventory.
    
    ![स्क्रीनशॉट](images/craft-wood-test.png)

+ There's no wood in your world! To fix this, click on your `main.py` file and find the function called `generateRandomWorld()`.
    
    ![स्क्रीनशॉट](images/craft-wood-random1.png)
    
    This code generates a random number between 0 and 10, and uses the number to decide which resource to place:
    
    + 1 or 2 = water
    + 3 or 4 = grass
    + anything else = DIRT

+ Add this code to add wood to your world whenever the `randomNumber` is 5.
    
    ![स्क्रीनशॉट](images/craft-wood-random2.png)

+ Test your project again. This time, you should see some wood appear in your world.
    
    ![स्क्रीनशॉट](images/craft-wood-test2.png)