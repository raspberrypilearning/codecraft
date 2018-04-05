## भूमिका

इस प्रोजेक्ट में, आप माइनक्राफ्ट के 2D संस्करण डिज़ाइन और सुधार के लिए कोड करेंगे।

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/9ac3995d69?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/craft-finished.png">
</div>

### क्लब लीडर्स के लिए अतिरिक्त जानकारी

यदि आप इस प्रोजेक्ट को प्रिंट करना चाहते हैं तो कृपया [प्रिंटर के लिए अनुकूल संस्करण](https://projects.raspberrypi.org/en/projects/codecraft/print) का उपयोग करें।


--- collapse ---
---
title: क्लब लीडर के नोट्स
---


## भूमिका:
इस प्रोजेक्ट में, बच्चे आधारभूत 2D माइनक्राफ्ट क्लोन में सुधार करके ग्राफिक्स और गेम डिज़ाइन सीखेंगे। बच्चे नए संसाधन बनाने के लिए संसाधनों के संयोजन के लिए, क्राफ्टिंग नियमों के साथ साथ नए संसाधन बनाएँगे। यह वेरिएबल, सूचियों और डिक्शनरीज़ को समझ और हेरफेर द्वारा हासिल किया जा सकता है।

## ऑनलाइन संसाधन

__यह प्रोजेक्ट Python 3 का उपयोग करता है।__ हम Python ऑनलाइन लिखने के लिए [trinket](https://trinket.io/) का उपयोग करने की अनुशंसा करते हैं। इस प्रोजेक्ट में निम्नलिखित Trinkets शामिल होते हैं:

+ ['कोडक्राफ्ट' आरंभ बिंदु -- jumpto.cc/codecraft-go](http://jumpto.cc/codecraft-go)

ऐसा भी ट्रिंकेट है, जिसमें पूर्ण प्रोजेक्ट शामिल होता है:

+ [‘कोडक्राफ्ट’ पूर्ण -- trinket.io/python/9ac3995d69](https://trinket.io/python/9ac3995d69)

## ऑफ़लाइन संसाधन
इस प्रोजेक्ट को [ऑफ़लाइन पूरा] किया जा सकता है (https://www.codeclubprojects.org/en-GB/resources/python-working-offline/) यदि वरीय हो। आप इस प्रोजेक्ट के लिए 'प्रोजेक्ट सामग्री' लिंक पर क्लिक करके प्रोजेक्ट के संसाधनों तक पहुँच कर सकते हैं। इस लिंक में 'प्रोजेक्ट संसाधन' भाग शामिल है, जिसमें ऐसे स्रोत शामिल हैं जिनकी आवश्यकता बच्चों को अपने प्रोजेक्ट ऑफ़लाइन पूरा करने के लिए हो सकती है। सुनिश्चित करें कि प्रत्येक बच्चे की इन संसाधनों तक पहुँच है। इस भाग में निम्नलिखित फाइलें शामिल हैं:

+ codecraft/codecraft.py
+ codecraft/variables.py
+ codecraft/player.gif
+ codecraft/dirt.gif
+ codecraft/grass.gif
+ codecraft/water.gif
+ codecraft/brick.gif

आप इस प्रोजेक्ट का पूर्ण संस्करण 'स्वैच्छिक संसाधन' भाग में भी देख सकते हैं, जिसमें ये शामिल हैं:

+ codecraft-finished/codecraft.py
+ codecraft-finished/variables.py
+ codecraft-finished/player.gif
+ codecraft-finished/dirt.gif
+ codecraft-finished/grass.gif
+ codecraft-finished/water.gif
+ codecraft-finished/brick.gif
+ codecraft-finished/wood.gif
+ codecraft-finished/plank.gif

(ऊपर्युक्त सभी संसाधन, प्रोजेक्ट और स्वैच्छिक `.zip` फाइलों के रूप में डाउनलोड योग्य भी होते हैं।)

## अधिगम उद्देश्य
+ ग्राफिक्स बनाना और संपादित करना;
+ गेम डिज़ाइन;
+ संपादन:
	+ चर;
	+ सूचियाँ;
	+ डिक्शनरीज़।

इस प्रोजेक्ट में [Raspberry Pi डिजिटल निर्माण पाठ्यचर्या](http://rpf.io/curriculum) के निम्नलिखित चीज़ों के तत्व शामिल होते हैं:

+ [आधारभूत 2D और 3D संपदाएँ डिज़ाइन करें](https://www.raspberrypi.org/curriculum/design/creator)

+ [समस्या का हल करने के लिए प्रोग्रामिंग निर्माण का संयोजन करें।](https://www.raspberrypi.org/curriculum/programming/builder)

## चुनौतियाँ
+ "अपनी दुनिया बनाएँ" – गेम खेलना, मौजूदा ब्लॉक्स जोड़ना और क्राफ्ट करना;
+ "अपनी दुनिया का आकार बदलें" – दुनिया का आकार बदलने के लिए `MAPWIDTH` (मानचित्र चौड़ाई) और `MAPHEIGHT` (मानचित्र ऊँचाई) वेरिएबल को संपादित करना;
+ "रेत बनाना" – संबंधित गेम डेटा के साथ रेत का संसाधन बनाना।
+ "रेत से काँच क्राफ्ट करना" – नया क्राफ्ट करने योग्य काँच बनाना।
+ "और संसाधन बनाएँ" – और ब्लॉक्स बनाने और क्राफ्टिंग के नियमों के बारे में सीखी हर चीज़ का उपयोग करें।

## अक्सर पूछे जाने वाले प्रश्न
+ __ऑफ़लाइन Python .png चित्रों का उपयोग नहीं करता है। .gif ऑनलाइन__उपयोग के लिए प्रदान किए गए हैं।__
+ बच्चों को यह याद दिलाना पड़ सकता है कि डिक्शनरी/सूची के एलिमेंट्स को कॉमा द्वारा अलग किया जाता है। उदाहरण के लिए, गेम में इन्वेंटरी आइटम, ग्राफिक्स और क्राफ्टिंग नियम जोड़ते समय।




--- /collapse ---


--- collapse ---
---
title: प्रोजेक्ट सामग्री
---
## प्रोजेक्ट संसाधन
* [प्रोजेक्ट के सभी संसाधनों सहित .zip फाइल](resources/codecraft-project-resources.zip)
* ['CodeCraft' प्रोजेक्ट के सभी संसाधनों सहित ऑनलाइन ट्रिंकेट](http://jumpto.cc/codecraft-go)
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

## क्लब लीडर के संसाधन
* [प्रोजेक्ट के पूर्ण किए गए सभी संसाधनों सहित .zip फाइल](resources/codecraft-volunteer-resources.zip)
* [ऑनलाइन पूर्ण ट्रिंकेट प्रोजेक्ट](https://trinket.io/python/9ac3995d69)
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
