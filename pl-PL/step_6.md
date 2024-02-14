## Tworzenie nowego zasobu drewna

Do utworzenia nowego zasobu drewna, potrzebne będą zmiany wartości niektórych zmiennych w pliku `variables.py`.

+ Najpierw należy przypisać wartość liczbową nowemu zasobowi, Najpierw należy przypisać wartość liczbową nowemu zasobowi, aby później móc używać słowa `WOOD` w swoim kodzie zamiast liczby 4.
    
    ![zrzut ekranu](images/craft-wood-const.png)

+ Dodaj nowy zasób `DREWNO` do listy `zasobów`.
    
    ![zrzut ekranu](images/craft-wood-resources.png)

+ Nadaj swojemu nowemu zasobowi nazwę, która będzie wyświetlana w ekwipunku.
    
    ![zrzut ekranu](images/craft-wood-name.png)
    
    Zwróć uwagę na przecinek `,` na końcu powyższej linii!

+ Twój zasób także będzie potrzebował obrazka. W obrazkach projektu znajdziesz `wood.gif`. Dodaj go do słownika `textury`.
    
    ![zrzut ekranu](images/craft-wood-texture.png)

+ Zacznij od dodania numeru swojego zasobu jaki powinien mieć w `inventory`.
    
    ![zrzut ekranu](images/craft-wood-inventory.png)

+ Następnie dodaj klawisz, którego wciśnięcie wstawi drewno do świata.
    
    ![zrzut ekranu](images/craft-wood-placekey.png)

+ Uruchom swój projekt, aby go przetestować. W Twoim ekwipunku powinien się znajdować nowy zasób „drewno”.
    
    ![zrzut ekranu](images/craft-wood-test.png)

+ W Twoim świecie nie ma drewna, aby to zmienić, kliknij na pliku `main.py` i odszukaj funkcję `generateRandomWorld()`.
    
    ![zrzut ekranu](images/craft-wood-random1.png)
    
    Ten kod generuje losową liczbę z zakresu od 0 do 10 i używa tej liczby do określenia, który zasób należy umieścić:
    
    + 1 lub 2 = woda
    + 3 lub 4 = trawa
    + cokolwiek innego = ZIEMIA

+ Dodaj ten kod, aby wstawić w Twoim świecie drewno, gdy `LosowaLiczba` ma wartość 5.
    
    ![zrzut ekranu](images/craft-wood-random2.png)

+ Przetestuj swój projekt ponownie. Tym razem powinieneś zobaczyć trochę drewna pojawiającego się w twoim świecie.
    
    ![zrzut ekranu](images/craft-wood-test2.png)