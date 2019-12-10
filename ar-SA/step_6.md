## إنشاء مورد خشب جديد

لننشئ مورد خشب جديدًا. لتفعل ذلك، ستحتاج إلى إضافة بعض المتغيرات في الملف `variables.py`.

+ أولًا، تحتاج إلى تعيين رقم إلى المورد الجديد. وسيمكنك عندئذٍ استخدام الكلمة `WOOD` في التعليمات البرمجية بدلًا من الرقم 4.
    
    ![screenshot](images/craft-wood-const.png)

+ يجب أن تضيف مورد `WOOD` الجديد إلى القائمة `resources`.
    
    ![screenshot](images/craft-wood-resources.png)

+ يجب أن تعيِّن اسمًا إلى هذا المورد أيضًا، بحيث يظهر في المخزون.
    
    ![screenshot](images/craft-wood-name.png)
    
    لاحظ وجود الفاصلة `,` في نهاية الأسطر أعلاه.

+ سيحتاج هذا المورد إلى صورة أيضًا. يحتوى المشروع بالفعل على صورة تُسمى `wood.png` يجب أن تضيفها إلى القاموس `textures`.
    
    ![screenshot](images/craft-wood-texture.png)

+ أضف عدد مربعات المورد التي يجب أن تكون موجودة في `inventory` عندما تبدأ.
    
    ![screenshot](images/craft-wood-inventory.png)

+ وأخيرًا، أضف المفتاح الذي ستضغط عليه لوضع الخشب في عالمك.
    
    ![screenshot](images/craft-wood-placekey.png)

+ شغِّل مشروعك لتختبره. سترى الآن أن المورد 'wood' الجديد قد أضيف إلى المخزون.
    
    ![screenshot](images/craft-wood-test.png)

+ لا يوجد خشب في عالمك! لإصلاح ذلك، انقر فوق الملف`main.py` وابحث عن الدالة `()generateRandomWorld`.
    
    ![screenshot](images/craft-wood-random1.png)
    
    تنشئ هذه التعليمة البرمجية عددًا عشوائيًا بين 0 و10، وتستخدم العدد لتحديد المورد الذي سيتم وضعه على خريطة عالمك:
    
    + 1 أو 2 = الماء
    + 3 أو 4 = الحشائش
    + غير ذلك = التراب

+ أضف هذه التعليمة البرمجية لإضافة خشب إلى عالمك متى كانت قيمة `randomNumber` هي 5.
    
    ![screenshot](images/craft-wood-random2.png)

+ اختبر مشروعك مرة أخرى. في هذه المرة، ستلاحظ ظهور بعض مربعات الخشب على خريطة عالمك.
    
    ![screenshot](images/craft-wood-test2.png)