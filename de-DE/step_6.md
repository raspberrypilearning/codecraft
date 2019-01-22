## Eine neue Ressource schaffen: Holz

Schaffen wir eine neue Ressource: Holz. Dazu musst du einige Variablen in der Datei `variables.py` hinzufügen.

+ Zuerst musst du deiner neuen Ressource eine Nummer geben. Du kannst dann im Code das Wort `HOLZ` statt der Nummer 4 verwenden.
    
    ![screenshot](images/craft-wood-const.png)

+ Du musst dann die neue `HOLZ`-Ressource zu deiner `ressourcen`- Liste hinzufügen.
    
    ![screenshot](images/craft-wood-resources.png)

+ Du musst deiner Ressource auch einen Namen geben, der im Inventar angezeigt wird.
    
    ![screenshot](images/craft-wood-name.png)
    
    Denke an das Komma `,` am Ende der obenstehenden Zeile.

+ Deine Ressource benötigt auch ein Bild. The project already includes an image called `wood.gif`, which you should add to the `textures` dictionary.
    
    ![screenshot](images/craft-wood-texture.png)

+ Füge die Anzahl Elemente von dieser Ressource hinzu, die zu Beginn in deinem `inventar` sein sollen.
    
    ![screenshot](images/craft-wood-inventory.png)

+ Und zum Schluss musst du noch die Taste angeben, die gedrückt werden muss, um Holz in deine Welt zu setzen.
    
    ![screenshot](images/craft-wood-placekey.png)

+ Führe dein Projekt aus, um es zu testen. Du wirst sehen, dass du jetzt eine neue 'Holz' -Ressource in deinem Inventar hast.
    
    ![screenshot](images/craft-wood-test.png)

+ In deiner Welt gibt es aber kein Holz! Um das zu beheben, klicke auf deine `main.py` Datei und suche die Funktion `erschaffeZuffallsWelt()`.
    
    ![screenshot](images/craft-wood-random1.png)
    
    Dieser Code generiert eine Zufallszahl zwischen 0 und 10 und bestimmt anhand der Nummer, welche Ressource platziert werden soll:
    
    + 1 oder 2 = Wasser
    + 3 oder 4 = Gras
    + alles andere = ERDE

+ Füge diesen Code hinzu, um Holz auf deiner Welt zu platzieren, wenn die `zufallsZahl` gleich 5 ist.
    
    ![screenshot](images/craft-wood-random2.png)

+ Teste dein Projekt erneut. Diesmal solltest du etwas Holz in deiner Welt sehen.
    
    ![screenshot](images/craft-wood-test2.png)