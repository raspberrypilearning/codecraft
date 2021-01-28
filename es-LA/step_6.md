## Crear un nuevo recurso de madera

Vamos a crear un nuevo recurso de madera. Para hacer esto, necesitarás añadir algunas variables en tu archivo `variables.py`.

+ Primero, debes darle un número a tu nuevo recurso. Entonces podrás usar la palabra `MADERA` en tu código en lugar del número 4.
    
    ![captura de pantalla](images/craft-wood-const.png)

+ Debes añadir tu nuevo recurso `MADERA` a tu lista de `recursos`.
    
    ![captura de pantalla](images/craft-wood-resources.png)

+ También debes darle un nombre a tu recurso, que se mostrará en el inventario.
    
    ![captura de pantalla](images/craft-wood-name.png)
    
    Observa la coma `,` al final de la línea de arriba.

+ Tu recurso también necesitará una imagen. El proyecto ya incluye una imagen llamada `wood.gif`, que debes añadir al diccionario de `texturas`.
    
    ![captura de pantalla](images/craft-wood-texture.png)

+ Añade el número de tu recurso que debería estar en tu `inventario` para empezar.
    
    ![captura de pantalla](images/craft-wood-inventory.png)

+ Finalmente, añade la tecla que presionarás para poner la madera en el mundo.
    
    ![captura de pantalla](images/craft-wood-placekey.png)

+ Ejecuta tu proyecto para probarlo. Verás que ahora tienes un nuevo recurso de "madera" en tu inventario.
    
    ![captura de pantalla](images/craft-wood-test.png)

+ ¡No hay madera en tu mundo! Para solucionar esto, haz clic en tu archivo `main.py` y encuentra la función llamada `generarMundoAleatorio()`.
    
    ![captura de pantalla](images/craft-wood-random1.png)
    
    Este código genera un número aleatorio entre 0 y 10, y usa el número para decidir qué recurso poner:
    
    + 1 o 2 = agua
    + 3 o 4 = césped
    + cualquier otro número = TIERRA

+ Añade este código para añadir madera a tu mundo cuando el `numeroAleatorio` sea 5.
    
    ![captura de pantalla](images/craft-wood-random2.png)

+ Prueba tu proyecto de nuevo. Esta vez, deberías ver que la madera aparece en tu mundo.
    
    ![captura de pantalla](images/craft-wood-test2.png)