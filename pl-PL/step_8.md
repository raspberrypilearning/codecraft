## Wytwarzanie desek z drewna

Stwórzmy nowy materiał deski, który będzie wykonany z drewna.

+ First, add a new `PLANK` variable to your game.
    
    ![zrzut ekranu](images/craft-plank-const.png)

+ Add a new `PLANK` variable to your game.
    
    ![zrzut ekranu](images/craft-plank-resources.png)

+ Nazwij zasób `"deskę"`.
    
    ![zrzut ekranu](images/craft-plank-names.png)

+ Podaj swój `PLANK` zasób obraz. The project already contains a `plank.gif` image, but you can create your own if you prefer.
    
    ![zrzut ekranu](images/craft-plank-textures.png)

+ Dodaj deski do ekwipunku.
    
    ![zrzut ekranu](images/craft-plank-inventory.png)

+ Ustaw klucz do układania desek.
    
    ![zrzut ekranu](images/craft-plank-placekeys.png)

+ Ponieważ ten zasób może zostać stworzony, musisz stworzyć regułę tworzenia, która polega na tym, że deskę można wykonać z 3 drewnianych płytek. Dodaj ten kod do słownika `crafting`.
    
    ![zrzut ekranu](images/craft-plank-crafting.png)

+ Na koniec musisz ustawić klucz do tworzenia nowych desek.
    
    ![zrzut ekranu](images/craft-plank-craftkeys.png)

+ Aby przetestować nowy zasób deski, zebrać kilka drewnianych płytek, a następnie wykuć deski z drewna. Możesz wtedy umieścić swoje nowe deski w swoim świecie.
    
    ![zrzut ekranu](images/craft-plank-test.png)