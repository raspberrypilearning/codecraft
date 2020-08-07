## Fabrique des planches à partir du bois

Créons une nouvelle ressource planche qui peut être fabriquée à partir de bois.

+ D'abord, ajoute une nouvelle variable `PLANCHE` à ton jeu.
    
    ![capture d'écran](images/craft-plank-const.png)

+ Ajoute une nouvelle variable `Planche` à ton jeu.
    
    ![capture d'écran](images/craft-plank-resources.png)

+ Nomme la ressource `'Planche'`.
    
    ![capture d'écran](images/craft-plank-names.png)

+ Donne une image à ta ressource `Planche`. Le projet contient déjà une image `planche.gif`, mais tu peux créer la tienne si tu préfères.
    
    ![capture d'écran](images/craft-plank-textures.png)

+ Ajoutes des planches à ton inventaire.
    
    ![capture d'écran](images/craft-plank-inventory.png)

+ Paramètre une touche pour placer des planches.
    
    ![capture d'écran](images/craft-plank-placekeys.png)

+ Comme cette ressource peut être crée, tu dois créer une règle de fabrication qui est qu'une planche peut être fabriquée à partir de 3 tuiles de bois. Ajoute ce code au dictionnaire `fabrication`.
    
    ![capture d'écran](images/craft-plank-crafting.png)

+ Enfin, tu dois paramétrer une touche pour fabriquer des nouvelles planches.
    
    ![capture d'écran](images/craft-plank-craftkeys.png)

+ Pour tester ta nouvelle ressource planche, rassemble plusieurs tuiles bois et fabrique quelques planches à partir du bois. Tu peux maintenant placer tes nouvelles planches sur ton monde.
    
    ![capture d'écran](images/craft-plank-test.png)