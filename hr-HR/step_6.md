## Stvori novi resurs - drvo

Stvorimo novi resurs - drvo. Da bi to napravili, moramo dodati još neke varijable u datoteku `variables.py`.

+ Prvo moraš odabrati broj za svoj novi resurs. Tada ćeš, umjesto broja 4, moći koristiti riječ DRVO u kôdu.
    
    ![screenshot](images/craft-wood-const.png)

+ Dodaj novi resurs `DRVO` unutar svoje liste `resursi`.
    
    ![screenshot](images/craft-wood-resources.png)

+ Također moraš svom resursu dati naziv koji će se prikazivati u inventaru.
    
    ![screenshot](images/craft-wood-name.png)
    
    Primijeti da se na kraju linija nalazi zarez`,`.

+ Tvoj resurs trebat će i sliku. U projektu se već nalazi slika pod nazivom `wood.gif` koju ćeš dodati u rječnik naziva `teksture`.
    
    ![screenshot](images/craft-wood-texture.png)

+ Za početak, u rječnik `inventar` dodaj broj koji si pridružio resursu.
    
    ![screenshot](images/craft-wood-inventory.png)

+ Zatim dodaj tipku kojom ćeš postaviti drvo u svijet.
    
    ![screenshot](images/craft-wood-placekey.png)

+ Pokreni i testiraj projekt. Vidjet ćeš da sada imaš novi resurs 'drvo' u svom inventaru.
    
    ![screenshot](images/craft-wood-test.png)

+ U tvom svijetu nema drva! Popravi to tako da odabereš datoteku `main.py` i pronađeš funkciju `generateRandomWorld()`.
    
    ![screenshot](images/craft-wood-random1.png)
    
    Ovaj kôd nasumično generira broj između 0 i 10, a dobiveni broj odlučuje koji element će se postaviti u svijet:
    
    + 1 ili 2 = voda
    + 3 ili 4 = trava
    + bilo što drugo = ZEMLJA

+ Unesi sljedeći kôd kako bi dodao drvo u svoj svijet svaki put kada je `randomNumber` 5.
    
    ![screenshot](images/craft-wood-random2.png)

+ Ponovno testiraj projekt. Ovoga bi se puta drvo trebalo pojaviti u tvom svijetu.
    
    ![screenshot](images/craft-wood-test2.png)