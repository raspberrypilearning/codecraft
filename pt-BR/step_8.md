## Crafting pranchas de madeira

Vamos criar um novo recurso de prancha que seja criado a partir de madeira.

+ Primeiro, adicione uma nova variável `PLANK` ao seu jogo.
    
    ![captura de tela](images/craft-plank-const.png)

+ Adicione uma nova variável `PLANK` ao seu jogo.
    
    ![captura de tela](images/craft-plank-resources.png)

+ Nomeie o recurso `'plank'`.
    
    ![captura de tela](images/craft-plank-names.png)

+ Dê uma imagem à sua `PLANK` recurso. O projeto já contém uma imagem `plank.png` , mas você pode criar a sua própria, se preferir.
    
    ![captura de tela](images/craft-plank-textures.png)

+ Adicione tábuas ao seu inventário.
    
    ![captura de tela](images/craft-plank-inventory.png)

+ Defina uma chave para colocar as tábuas.
    
    ![captura de tela](images/craft-plank-placekeys.png)

+ Como este recurso pode ser trabalhado, você precisa criar uma regra de criação, que é que uma prancha pode ser feita a partir de 3 ladrilhos de madeira. Adicione este código ao `crafting` dicionário.
    
    ![captura de tela](images/craft-plank-crafting.png)

+ Finalmente, você precisa definir uma chave para criar novas pranchas.
    
    ![captura de tela](images/craft-plank-craftkeys.png)

+ Para testar seu novo recurso de prancha, junte alguns ladrilhos de madeira e depois faça algumas tábuas em sua madeira. Você pode então colocar suas novas tábuas em seu mundo.
    
    ![captura de tela](images/craft-plank-test.png)