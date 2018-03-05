## Creazione di una nuova risorsa di legno

Creiamo una nuova risorsa di legno. Per farlo, devi prima aggiungere delle variabili al tuo file"variables.py".

+ Per prima cosa devi dare un numero alla tua nuova risorsa. Potrai quindi usare la parola "WOOD" (che significa legno in inglese) nel codice, invece del numero 4.

    ![screenshot](images/craft-wood-const.png)

+ Devi aggiungere la tua nuova risorsa "WOOD" al tuo elenco di risorse in "resources".

    ![screenshot](images/craft-wood-resources.png)

+ Devi anche dare alla tua risorsa un nome che verrà visualizzato nell'inventario.

    ![screenshot](images/craft-wood-name.png)

    Nota che c'è una virgola alla fine della riga precedente.

+ La tua risorsa avrà anche bisogno di un'immagine. Il progetto contiene già un'immagine chiamata "wood.png" che dovresti aggiungere al tuo dizionario delle immagini ("textures").

    ![screenshot](images/craft-wood-texture.png)

+ Aggiungi il numero della tua risorsa che deve essere nell'inventario all'inizio.

    ![screenshot](images/craft-wood-inventory.png)

+ Per finire, aggiungi il tasto che bisogna premere per mettere il legno nel mondo.

    ![screenshot](images/craft-wood-placekey.png)

+ Lancia il progetto per vedere se funziona. Vedrai che hai ora una nuova risorsa di legno ("wood") nell'inventario.

    ![screenshot](images/craft-wood-test.png)

+ Ma nel mondo di legno non ce n'è! Per correggere questo intoppo, fai clic sul file "main.py" e cerca la funzione denominata "generateRandomWorld()".

    ![screenshot](images/craft-wood-random1.png)    

    Questo codice genera un numero casuale compreso tra 0 e 10 e utilizza questo numero per decidere quali risorse inserire:

    + 1 o 2 = acqua
    + 3 o 4 = erba
    + tutti gli altri = terra

+ Aggiungi questo codice per aggiungere legno al mondo ogni volta che il numero casuale di "randomNumber" è 5.

    ![screenshot](images/craft-wood-random2.png)

+ Prova di nuovo il progetto. Questa volta dovresti vedere che del legno comincia ad apparire nel mondo.

    ![screenshot](images/craft-wood-test2.png)

