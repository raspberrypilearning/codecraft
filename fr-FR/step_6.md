## Créer une nouvelle ressource en bois

Créons une nouvelle ressource en bois. Pour faire ceci, il faudrait ajouter quelques variables à ton fichier `variables.py`.

+ D'abord, tu as besoin d'assigner un chiffre à ta nouvelle ressource. Puis tu vas pouvoir utiliser le mot `WOOD` (bois) dans ton code à la place du chiffre 4.

    ![screenshot](images/craft-wood-const.png)

+ Tu devrais ajouter ta nouvelle ressource `WOOD` à ta liste de `ressources`.

    ![screenshot](images/craft-wood-resources.png)

+ Tu devrais également assigner un nom à ta ressource, ce qui sera affiché dans l'inventaire.

    ![screenshot](images/craft-wood-name.png)

    Remarque la virgule `,` à la fin de la ligne ci-dessus.

+ Ta ressources aura besoin aussi d'une image. Le projet comprend déjà une image nomée`wood.png`, que tu devrais ajouter au dictionnaire `textures`.

    ![screenshot](images/craft-wood-texture.png)

+ Ajoute le chiffre de ta ressource qui devrait être dans ton `inventaire` pour démarrer.

    ![screenshot](images/craft-wood-inventory.png)

+ Enfin, ajoute la clé que tu vas appuyer pour placer le bois dans le monde.

    ![screenshot](images/craft-wood-placekey.png)

+ Exécuter ton projet pour le tester. Tu vas voir que tu as une nouvelle ressource 'wood' dans ton inventaire.

    ![screenshot](images/craft-wood-test.png)

+ Il n'y a pas de bois dans ton monde ! Pour régler ça, clique sur le fichier `main.py` et trouve la fonction nommée `generateRandomWorld()`.

    ![screenshot](images/craft-wood-random1.png)    

    Ce code génére un chiffre aléatoire entre 0 et 10, et l'utilise pour décider quelle ressource à placer :

    + 1 ou 2 = water
    + 3 ou 4 = grass
    + tout autre chiffre = DIRT

+ Ajoute ce code pour ajouter du bois dans ton monde quand `randomNumber` (chiffre aléatoire) est 5.

    ![screenshot](images/craft-wood-random2.png)

+ Teste ton projet de nouveau. Cette fois-ci, tu devrais voir du bois apparaître dans ton monde.

    ![screenshot](images/craft-wood-test2.png)

