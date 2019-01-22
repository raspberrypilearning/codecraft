## Izrada dasaka od drva

Napravimo novi resurs, dasku, koja može biti izrađena od drva.

+ Prvo dodaj u svoju igru novu promjenljivu `DASKA`.
    
    ![screenshot](images/craft-plank-const.png)

+ Dodaj novu promjenljivu `DASKA` u svoju igru.
    
    ![screenshot](images/craft-plank-resources.png)

+ Resursu daj naziv `'daska'`.
    
    ![screenshot](images/craft-plank-names.png)

+ Resursu `DASKA` dodijeli sliku. Projekat već sadrži sliku `plank.gif`, ali možeš da napraviš sopstvenu sliku ako želiš.
    
    ![screenshot](images/craft-plank-textures.png)

+ Dodaj daske u svoj inventar.
    
    ![screenshot](images/craft-plank-inventory.png)

+ Odredi taster za postavljanje dasaka.
    
    ![screenshot](images/craft-plank-placekeys.png)

+ S obzirom na to da ovaj resurs može biti izrađen od drugih resursa, treba da definišeš pravilo za izradu: da daska može biti izrađena od tri pločice drveta. Dodaj ovaj kôd u svoj rječnik `izrada`.
    
    ![screenshot](images/craft-plank-crafting.png)

+ Na kraju, treba da odrediš taster za izradu novih dasaka.
    
    ![screenshot](images/craft-plank-craftkeys.png)

+ Da isprobaš svoj novi resurs - dasku, sakupi nekoliko pločica drveta i od njih izradi daske. Zatim postavi nove daske u svoj svijet.
    
    ![screenshot](images/craft-plank-test.png)