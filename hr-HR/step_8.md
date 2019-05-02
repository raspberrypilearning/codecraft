## Izradi daske od drva

Napravimo novi resurs, dasku, koji se može izraditi od drva.

+ Prvo stvori u igri novu varijablu `DASKA`.
    
    ![screenshot](images/craft-plank-const.png)

+ Dodaj igri novu varijablu `DASKA`.
    
    ![screenshot](images/craft-plank-resources.png)

+ Nazovi resurs `'daska'`.
    
    ![screenshot](images/craft-plank-names.png)

+ Pridruži resursu `DASKA` sliku. U projektu se već nalazi slika `plank.gif`, ali možeš stvoriti i vlastitu ako želiš.
    
    ![screenshot](images/craft-plank-textures.png)

+ Dodaj daske u svoj inventar.
    
    ![screenshot](images/craft-plank-inventory.png)

+ Odredi tipku kojom će se daske postavljati u svijet.
    
    ![screenshot](images/craft-plank-placekeys.png)

+ S obzirom da je ovo resurs koji može biti izrađen od drugih resursa, moraš utvrditi po kojim pravilima može biti izrađen. Neka pravilo bude da se daska može izraditi od 3 komada drveta. Dodaj ovaj kôd u svoj rječnik `izrada`.
    
    ![screenshot](images/craft-plank-crafting.png)

+ Na kraju, moraš odrediti kojom tipkom će se izrađivati nove daske.
    
    ![screenshot](images/craft-plank-craftkeys.png)

+ Testiraj svoj novi resurs dasku. Sakupi nekoliko komada drveta i od njih izradi daske. Zatim postavi svoje nove daske u svijet.
    
    ![screenshot](images/craft-plank-test.png)