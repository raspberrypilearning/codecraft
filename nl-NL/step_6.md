## Maak een nieuwe bron voor hout

Laten we een nieuwe bron voor hout creëren. Daarvoor moet je enkele variabelen in het bestand `variables.py` toevoegen.

+ Eerst moet je de nieuwe bron een nummer geven. Je kunt dan het woord `HOUT` gebruiken in het programma, in plaats van nummer 4.
    
    ![screenshot](images/craft-wood-const.png)

+ Je moet de nieuwe bron `HOUT` toevoegen aan je lijst met `bronnen`.
    
    ![screenshot](images/craft-wood-resources.png)

+ Je moet de bron ook een naam geven die in de inventaris wordt weergegeven.
    
    ![screenshot](images/craft-wood-name.png)
    
    Let op de komma `,` aan het einde van de regel hierboven.

+ Je bron heeft ook een afbeelding nodig. Het project bevat al een afbeelding met de naam `wood.png`, die je zou moeten toevoegen aan het `materialen` woordenboek.
    
    ![screenshot](images/craft-wood-texture.png)

+ Om te beginnen voeg je het nummer van de bron toe aan de `inventaris`.
    
    ![screenshot](images/craft-wood-inventory.png)

+ Voeg tenslotte de toets toe die je wilt gebruiken om hout in de wereld te plaatsen.
    
    ![screenshot](images/craft-wood-placekey.png)

+ Voer je project uit om het te testen. Je zult zien dat je nu een nieuwe 'hout' bron in je inventaris hebt.
    
    ![screenshot](images/craft-wood-test.png)

+ Er is geen hout in jouw wereld! Om dit op te lossen, klikt je op je `main.py` bestand en zoekt je de functie `genereerWillekeurigeWereld()`.
    
    ![screenshot](images/craft-wood-random1.png)
    
    Deze code genereert een willekeurig getal tussen 0 en 10 en gebruikt het nummer om te bepalen welke bron moet worden geplaatst:
    
    + 1 of 2 = water
    + 3 of 4 = gras
    + iets anders = VUIL

+ Voeg deze code toe om hout aan je wereld toe te voegen wanneer `willekeurigGetal` 5 is.
    
    ![screenshot](images/craft-wood-random2.png)

+ Test je project opnieuw. Deze keer zou je wat hout in je wereld moeten zien verschijnen.
    
    ![screenshot](images/craft-wood-test2.png)