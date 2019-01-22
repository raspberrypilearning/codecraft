## Criando um novo recurso de madeira

Vamos criar um novo recurso de madeira. Para fazer isso, você precisará adicionar algumas variáveis ​​em seu arquivo `variables.py`.

+ Primeiro, você precisa dar um novo número ao seu novo recurso. Você poderá usar a palavra `WOOD` em seu código, em vez do número 4.
    
    ![captura de tela](images/craft-wood-const.png)

+ Você deve adicionar seu novo recurso `WOOD` à sua lista de recursos ``.
    
    ![captura de tela](images/craft-wood-resources.png)

+ Você também deve dar um nome ao seu recurso, que será exibido no inventário.
    
    ![captura de tela](images/craft-wood-name.png)
    
    Observe a vírgula `,` no final da linha acima.

+ Seu recurso também precisará de uma imagem. The project already includes an image called `wood.gif`, which you should add to the `textures` dictionary.
    
    ![captura de tela](images/craft-wood-texture.png)

+ Adicione o número do seu recurso que deve estar no `inventário` para começar.
    
    ![captura de tela](images/craft-wood-inventory.png)

+ Por fim, adicione a chave que você pressionará para colocar a madeira no mundo.
    
    ![captura de tela](images/craft-wood-placekey.png)

+ Execute seu projeto para testá-lo. Você verá que agora tem um novo recurso "de madeira" em seu inventário.
    
    ![captura de tela](images/craft-wood-test.png)

+ Não há madeira no seu mundo! Para corrigir isso, clique no seu arquivo `main.py` e encontre a função `generateRandomWorld ()`.
    
    ![captura de tela](images/craft-wood-random1.png)
    
    Esse código gera um número aleatório entre 0 e 10 e usa o número para decidir qual recurso colocar:
    
    + 1 ou 2 = água
    + 3 ou 4 = grama
    + qualquer outra coisa = DIRT

+ Adicione este código para adicionar madeira ao seu mundo sempre que o `randomNumber` for 5.
    
    ![captura de tela](images/craft-wood-random2.png)

+ Teste seu projeto novamente. Desta vez, você deve ver alguma madeira aparecer em seu mundo.
    
    ![captura de tela](images/craft-wood-test2.png)