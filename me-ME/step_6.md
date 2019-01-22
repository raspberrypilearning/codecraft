## Kreiranje novog resursa - drveta

Kreirajmo novi resurs - drvo. Da bismo to napravili, moramo dodati još neke promjenljive u tvoju datoteku `variables.py`.

+ Prvo treba da dodijeliš broj svom novom resursu. Tada ćeš u svom kôdu moći da koristiš riječ `DRVO` umjesto broja 4.
    
    ![screenshot](images/craft-wood-const.png)

+ Dodaj novi resurs `DRVO` u svoju listu `resursi`.
    
    ![screenshot](images/craft-wood-resources.png)

+ Takođe, svom resursu treba da daš naziv koji će biti prikazan u inventaru.
    
    ![screenshot](images/craft-wood-name.png)
    
    Obrati pažnju na zarez `,` na kraju reda.

+ Tvom resursu će biti potrebna i slika. The project already includes an image called `wood.gif`, which you should add to the `textures` dictionary.
    
    ![screenshot](images/craft-wood-texture.png)

+ Dodaj količinu resursa koja bi trebalo da se nalazi u tvom `inventaru` na početku.
    
    ![screenshot](images/craft-wood-inventory.png)

+ Na kraju, dodaj taster kojim ćeš postavljati drvo u svijet.
    
    ![screenshot](images/craft-wood-placekey.png)

+ Pokreni i isprobaj svoj projekat. Vidjećeš da sada imaš novi resurs 'drvo' u svom inventaru.
    
    ![screenshot](images/craft-wood-test.png)

+ U tvom svijetu nema drva! Da to popraviš, klikni na datoteku `main.py` i pronađi funkciju `generisiNasumicanSvijet()`.
    
    ![screenshot](images/craft-wood-random1.png)
    
    Ovaj kôd generiše nasumičan broj između 0 i 10 i koristi taj broj da odluči koji resurs će biti postavljen:
    
    + 1 ili 2 = voda
    + 3 ili 4 = trava
    + bilo šta drugo = ZEMLJA

+ Unesi sljedeći kôd kako bi drvo bilo dodato u tvoj svijet svaki put kada je `nasumicanBroj` 5.
    
    ![screenshot](images/craft-wood-random2.png)

+ Ponovo isprobaj svoj projekat. Ovoga puta bi trebalo da vidiš drva u svom svijetu.
    
    ![screenshot](images/craft-wood-test2.png)