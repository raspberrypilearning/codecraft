## Bretter aus Holz herstellen

Lass uns eine neue Ressource Brett erstellen, die aus Holz gefertigt wird.

+ Füge zuerst eine neue Variable `BRETT` zu deinem Spiel hinzu.
    
    ![screenshot](images/craft-plank-const.png)

+ Füge hier den neuen Namen `BRETT` hinzu.
    
    ![screenshot](images/craft-plank-resources.png)

+ Gib dieser Ressource den Namen `'Brett'`.
    
    ![screenshot](images/craft-plank-names.png)

+ Weise der Ressource `BRETT` ein Bild zu. Das Projekt enthält bereits das `plank.gif`-Bild, aber du kannst dein eigenes erstellen, wenn du das willst.
    
    ![screenshot](images/craft-plank-textures.png)

+ Füge Bretter zu deinem Inventar hinzu.
    
    ![screenshot](images/craft-plank-inventory.png)

+ Bestimme eine Taste für das Platzieren der Bretter.
    
    ![screenshot](images/craft-plank-placekeys.png)

+ Da diese Ressource hergestellt werden kann, musst du eine Regel für die Herstellung programmieren, d. h. ein Brett kann aus 3 Elementen Holz hergestellt werden. Füge diesen Code zu deinem `herstellenMit` -Dictionary hinzu.
    
    ![screenshot](images/craft-plank-crafting.png)

+ Schließlich musst du eine Taste für die Herstellung neuer Bretter festlegen.
    
    ![screenshot](images/craft-plank-craftkeys.png)

+ Um deine neue Brett-Ressource zu testen, sammle ein paar Elemente Holz ein und stelle dann einige Bretter aus diesem Holz her. Du kannst dann diese neuen Bretter in deiner Welt platzieren.
    
    ![screenshot](images/craft-plank-test.png)