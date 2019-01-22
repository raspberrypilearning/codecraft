## 나무 아이템 만들기

나무 아이템을 새롭게 만들어 봅시다. 나무를 추가하기 위해서는, `variables.py` 에 일부 변수를 추가해야 합니다.

+ 먼저, 새로운 나무 아이템에 번호를 부여해야 합니다. `WOOD` 대신 4를 리소스 번호로 사용합니다.
    
    ![스크린샷](images/craft-wood-const.png)

+ 새로운 `WOOD` 아이템을 `resources` 리스트에 추가합니다.
    
    ![스크린샷](images/craft-wood-resources.png)

+ 또한 인벤토리에 표시되는 아이템 명은 아래처럼 추가할 수 있습니다.
    
    ![스크린샷](images/craft-wood-name.png)
    
    각 라인의 끝에는 마지막 요소를 제외하고 `,`가 추가되어야 합니다.

+ 리소스에는 이미지도 필요합니다. The project already includes an image called `wood.gif`, which you should add to the `textures` dictionary.
    
    ![스크린샷](images/craft-wood-texture.png)

+ 게임을 처음 시작할 때 플레이어의 `inventory` 에 입력되는 아이템의 개수를 지정할 수 있습니다.
    
    ![스크린샷](images/craft-wood-inventory.png)

+ 마지막으로, 월드에 나무를 배치하기 위해 누르는 키를 추가하세요.
    
    ![스크린샷](images/craft-wood-placekey.png)

+ 테스트를 위해 프로젝트를 실행해 보세요. 새로운 '나무' 자원이 아래와 같이 추가된 것을 볼 수 있습니다.
    
    ![스크린샷](images/craft-wood-test.png)

+ 그런데 나무가 없어요! 이 문제를 해결하기 위해서는 `main.py` 파일의 `generateRandomWorld()` 함수를 찾아 보세요. 
    
    ![스크린샷](images/craft-wood-random1.png)
    
    이 코드는 0부터 10까지의 랜덤 숫자를 생성하는데, 이 숫자를 기반으로 어떤 블럭이 세계에 배치되는지 정하게 됩니다.
    
    + 1이나 2 = 물 블록
    + 3이나 4 = 초원 블록
    + 이외 = 흙 블록

+ 아래와 같이 `randomNumber`가 5인 경우, 나무가 월드 안에 추가되도록 코드를 설계하세요.
    
    ![스크린샷](images/craft-wood-random2.png)

+ 프로젝트를 다시 테스트해 보세요. 이제 월드에서 아래와 같이 나무가 보일 것입니다.
    
    ![스크린샷](images/craft-wood-test2.png)