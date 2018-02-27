## Latten aus Holz herstellen

Lass uns eine neue Latten-Ressource herstellen, welche aus Holz hergestellt wird.

+ Als erstes musst du eine neue `PLANK` (Holzlatte) Variable deinem Spiel hinzufügen.

    ![screenshot](images/craft-plank-const.png)

+ Füge eine neue `PLANK` (Holzlatte) Variable zu deinem Spiel hinzu.

    ![screenshot](images/craft-plank-resources.png)

+ Nenne diese Ressource `'plank'` (Holzlatte).

    ![screenshot](images/craft-plank-names.png)

+ Füge deiner `PLANK` (Holzlatte) Ressource ein Bild hinzu. Das Projekt enthält bereits ein `plank.png` (Holzlatte) Bild, aber du kannst dein eigenes Bild herstellen, wenn du willst.

    ![screenshot](images/craft-plank-textures.png)

+ Füge die Holzlatten zu deinem Inventar hinzu.

    ![screenshot](images/craft-plank-inventory.png)

+ Richte eine Taste ein, um die Holzlatten zu platzieren.

    ![screenshot](images/craft-plank-placekeys.png)

+ Da diese Ressource angefertigt werden muss, musst du eine Herstellungsregel kreieren, welche daraus besteht, dass eine Holzlatte aus 3 Holzstücken angefertigt werden muss. Füge diesen Code zu deinem `crafting` (Anfertigung) Wörterbuch hinzu. 

    ![screenshot](images/craft-plank-crafting.png)

+ Abschließend musst du eine Taste zur Anfertigung neuer Holzlatten einrichten.

    ![screenshot](images/craft-plank-craftkeys.png)

+ Um deine neue Holzlatte-Ressource zu testen, kannst du ein paar Holzstücke sammeln und dann ein paar Holzlatten aus deinem Holz anfertigen. Du kannst dann die neuen Holzlatten in deiner Welt platzieren.

    ![screenshot](images/craft-plank-test.png)



