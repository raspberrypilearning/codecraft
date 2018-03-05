## Creación de un nuevo recurso: madera

Creemos el recurso "madera". Para ello, necesitarás añadir algunas variables a tu archivo `variables.py`.

+ Primero, debes proporcionar un número a tu nuevo recurso. A continuación, podrás usar la palabra `WOOD` en tu código en lugar del número 4.

    ![screenshot](images/craft-wood-const.png)

+ Debes añadir tu nuevo recurso `WOOD` a la lista `resources`.

    ![screenshot](images/craft-wood-resources.png)

+ También debes proporcionar a tu recurso un nombre que será visualizado en el inventario.

    ![screenshot](images/craft-wood-name.png)

    Ten en cuenta la coma `,` al final de la línea anterior.

+ Tu recurso también necesitará una imagen. El proyecto ya incluye una imagen con el nombre `wood.png` que deberás añadir al diccionario `textures`.

    ![screenshot](images/craft-wood-texture.png)

+ Añade el número de recursos de este tipo que tendrás en tu `inventory` al inicio.

    ![screenshot](images/craft-wood-inventory.png)

+ Por último, añade la tecla que deberás pulsar para colocar el recurso en tu mundo. 

    ![screenshot](images/craft-wood-placekey.png)

+ Ejecuta el proyecto para probarlo. Verás que ahora tienes el nuevo recurso 'wood' en tu inventario.

    ![screenshot](images/craft-wood-test.png)

+ ¡No hay madera en tu mundo! Para solucionarlo, haz clic en el archivo `main.py` y localiza la función `generateRandomWorld()`.

    ![screenshot](images/craft-wood-random1.png)    

    Este código genera un número aleatorio entre 0 y 10 y usa el número para decidir qué recurso colocar:

    + 1 o 2 = agua
    + 3 o 4 = césped
    + cualquier otro = SUCIEDAD

+ Agrega este código para añadir madera a tu mundo cada vez que `randomNumber` sea 5. 

    ![screenshot](images/craft-wood-random2.png)

+ Vuelve a probar tu proyecto. Esta vez deberías ver madera en tu mundo.

    ![screenshot](images/craft-wood-test2.png)

