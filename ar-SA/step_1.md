## المقدمة

في هذا المشروع، ستصمِّم تحسينات لنسخة ثنائية الأبعاد من لعبة ماين كرافت وتكتب تعليماتها البرمجية.

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/9ac3995d69?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/craft-finished.png">
</div>

### معلومات إضافية لقادة النادي

إذا كنت بحاجة إلى طباعة هذا المشروع، فيُرجى استخدام [نسخة سهلة الطباعة](https://projects.raspberrypi.org/en/projects/codecraft/print).


--- collapse ---
---
title: ملاحظات قادة النادي
---


## المقدمة:
في هذا المشروع، سيتعرَّف الأطفال على سمات الرسومات وتصميم الألعاب بإجراء تحسينات على نسخة أساسية ثنائية الأبعاد من لعبة ماين كرافت. حيث سينشئ الأطفال موارد جديدة وقواعد صناعة لجمع الموارد الحالية وإنشاء موارد جديدة. وسيتم ذلك بفهم المتغيرات والقوائم والقواميس واستخدامها.

## الموارد المتوفرة على الإنترنت

__يستخدم هذا المشروع Python 3.__ نوصي باستخدام [trinket](https://trinket.io/) لكتابة Python على الإنترنت. يحتوي هذا المشروع على Trinket التالية:

+ ['صناعة الأكواد' مشروع البدء -- jumpto.cc/codecraft-go](http://jumpto.cc/codecraft-go)

وهناك أيضًا trinket تحتوي على المشروع المكتمل:

+ [مشروع 'صناعة الأكواد' مُكتمل -- trinket.io/python/9ac3995d69](https://trinket.io/python/9ac3995d69)

## الموارد المتوفرة دون اتصال بالإنترنت
يمكن أن يكون هذا المشروع [مكتمل دون اتصال بالإنترنت](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/) إذا كنت تفضل ذلك. يمكنك الوصول إلى موارد المشروع من خلال النقر فوق رابط "مواد المشروع" الخاص بهذا المشروع. يحتوي هذا الرابط على قسم "موارد المشروع"، الذي يتضمن الموارد التي يحتاج إليها الأطفال لإكمال هذا المشروع من دون اتصال بالإنترنت. تأكد من أن كل طفل لديه حق الوصول إلى نسخة من هذه الموارد. يتضمن هذا القسم الملفات التالية:

+ codecraft/codecraft.py
+ codecraft/variables.py
+ codecraft/player.gif
+ codecraft/dirt.gif
+ codecraft/grass.gif
+ codecraft/water.gif
+ codecraft/brick.gif

يمكنك أيضًا العثور على نسخة كاملة من هذا المشروع في قسم "موارد المتطوعين"، الذي يحتوي على:

+ codecraft-finished/codecraft.py
+ codecraft-finished/variables.py
+ codecraft-finished/player.gif
+ codecraft-finished/dirt.gif
+ codecraft-finished/grass.gif
+ codecraft-finished/water.gif
+ codecraft-finished/brick.gif
+ codecraft-finished/wood.gif
+ codecraft-finished/plank.gif

(جميع الموارد المذكورة أعلاه قابلة للتنزيل أيضًا كملفات `.zip` للمشاريع والمتطوعين).

## أهداف التعلم
+ إنشاء الرسومات وتحريرها؛
+ تصميم الألعاب؛
+ تحرير:
	+ المتغيرات:
	+ القوائم:
	+ القواميس.

يتناول هذا المشروع عناصر من الصفوف التالية من [المناهج الرقمية الخاصة بـ Raspberry Pi](http://rpf.io/curriculum):

+ [الأصول الأساسية للتصميمات ثنائية الأبعاد وثلاثية الأبعاد](https://www.raspberrypi.org/curriculum/design/creator)

+ [دمج الإنشاءات البرمجية لحل مشكلة](https://www.raspberrypi.org/curriculum/programming/builder)

## التحديات:
+ "صمِّم عالمك" - لعب اللعبة مع وضع قوالب الموارد الحالية وصناعتها؛
+ "غيِّر حجم عالمك" - تحرير المتغيرين `MAPWIDTH` و`MAPHEIGHT` لتغيير حجم عالم اللعبة؛
+ "أنشئ مورد الرمل" - إنشاء مورد رمل جديدًا، إلى جانب استخدام بيانات اللعبة ذات الصلة.
+ "اصنع الزجاج من الرمل" - إنشاء مورد زجاج جديدًا يمكن صناعته من موارد أخرى.
+ "أنشئ موارد أخرى" - استخدام ما تم تعلمه لإنشاء قوالب موارد وقواعد صناعة أخرى.

## الأسئلة الشائعة
+ __لا تعمل صور .png مع Python في حالة عدم الاتصال. لذا تم توفير صور بصيغة .gif لاستخدامها في حالة عدم الاتصال.__
+ قد يحتاج الأطفال إلى التذكير باستخدام الفاصلة للفصل بين عناصر القاموس/القائمة. على سبيل المثال، عند إضافة عناصر مخزون ورسومات وقواعد صناعة إلى اللعبة.




--- /collapse ---


--- collapse ---
---
title: مواد المشروع
---
## موارد المشروع
* [ملف .zip يحتوي على كل موارد المشروع](resources/codecraft-project-resources.zip)
* [Trinket عبر الإنترنت يحتوي على كل موارد مشروع 'صناعة الأكواد'](http://jumpto.cc/codecraft-go)
* [codecraft/codecraft.py](resources/codecraft-codecraft.py)
* [codecraft/variables.py](resources/codecraft-variables.py)
* [codecraft/brick.gif](resources/codecraft-brick.gif)
* [codecraft/dirt.gif](resources/codecraft-dirt.gif)
* [codecraft/glass.gif](resources/codecraft-glass.gif)
* [codecraft/grass.gif](resources/codecraft-grass.gif)
* [codecraft/plank.gif](resources/codecraft-plank.gif)
* [codecraft/player.gif](resources/codecraft-player.gif)
* [codecraft/sand.gif](resources/codecraft-sand.gif)
* [codecraft/water.gif](resources/codecraft-water.gif)
* [codecraft/wood.gif](resources/codecraft-wood.gif)

## موارد قادة النادي
* [ملف .zip يحتوي على كل موارد المشاريع المكتملة](resources/codecraft-volunteer-resources.zip)
* [مشروع Trinket المكتمل على الإنترنت](https://trinket.io/python/9ac3995d69)
* [codecraft-finished/codecraft.py](resources/codecraft-finished-codecraft.py)
* [codecraft-finished/variables.py](resources/codecraft-finished-variables.py)
* [codecraft-finished/brick.gif](resources/codecraft-finished-brick.gif)
* [codecraft-finished/dirt.gif](resources/codecraft-finished-dirt.gif)
* [codecraft-finished/glass.gif](resources/codecraft-finished-glass.gif)
* [codecraft-finished/grass.gif](resources/codecraft-finished-grass.gif)
* [codecraft-finished/plank.gif](resources/codecraft-finished-plank.gif)
* [codecraft-finished/player.gif](resources/codecraft-finished-player.gif)
* [codecraft-finished/sand.gif](resources/codecraft-finished-sand.gif)
* [codecraft-finished/water.gif](resources/codecraft-finished-water.gif)
* [codecraft-finished/wood.gif](resources/codecraft-finished-wood.gif)

--- /collapse ---
