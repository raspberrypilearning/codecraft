## भूमिका

इस प्रोजेक्ट में, आप Minecraft के 2D संस्करण में डिज़ाइन और कोड सुधार करेंगे।

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/ebc5b0148b?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/craft-finished.png">
</div>

### क्लब लीडर्स के लिए अतिरिक्त जानकारी

अगर आपको इस प्रोजेक्ट को प्रिंट करने की आवश्यकता है, तो कृप्या [प्रिंटर अनुकूल वर्ज़न](https://projects.raspberrypi.org/en/projects/codecraft/print) का उपयोग करें।

## \--- collapse \---

## title: क्लब नेता नोट्स

## भूमिका:

इस प्रोजेक्ट में, बच्चे एक मूल 2D Minecraft क्लोन में सुधार करके ग्राफिक्स और गेम डिज़ाइन के पहलुओं को जानेंगे। बच्चे नए संसाधन बनाएंगे, साथ ही नए संसाधन बनाने के लिए मौजूदा संसाधनों का उपयोग करने के लिए नियम बनाएंगे। यह वेरिएबल्स, सूचियों और शब्दकोशों को समझने और हेरफेर करने से प्राप्त होगा।

## ऑनलाइन संसाधन

**इस प्रोजेक्ट में Python 3 का उपयोग किया जाता है।**Python को ऑनलाइन लिखने के लिए हम [trinket](https://trinket.io/) का उपयोग करने की सलाह देते हैं। इस प्रोजेक्ट में निम्नलिखित Trinkets शामिल हैं:

+ ['कोडक्राफ्ट' शुरूआती प्रोजेक्ट - rpf.io/codecraft-on](http://rpf.io/codecraft-on)

एक ऐसा trinket भी है जिसमें पूरा प्रोजेक्ट है:

+ ['कोडक्राफ्ट' पूर्ण - trinket.io/python/ebc5b0148b](https://trinket.io/python/ebc5b0148b)

## ऑफ़लाइन संसाधन

यदि चाहें तो इस प्रोजेक्ट को [ऑफ़लाइन पूरा](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/) किया जा सकता है। आप इस प्रोजेक्ट के लिए 'प्रोजेक्ट सामग्री' लिंक पर क्लिक करके प्रोजेक्ट के संसाधनों पर पहुँच प्राप्त कर सकते हैं। इस लिंक में 'प्रोजेक्ट संसाधन' खंड है, जिसमें ऐसे संसाधन सम्मिलित हैं जिनकी बच्चों को इस प्रोजेक्ट को ऑफ़लाइन पूरा करने के लिए ज़रूरत होगी। सुनिश्चित करें कि प्रत्येक बच्चे को इन संसाधनों की कॉपी तक पहुँच प्राप्त होती है। इस खंड में निम्नलिखित फाइलें शामिल हैं:

+ codecraft/codecraft.py
+ codecraft/variables.py
+ codecraft/brick.gif
+ codecraft/dirt.gif
+ codecraft/glass.gif
+ codecraft/grass.gif
+ codecraft/plank.gif
+ codecraft/player.gif
+ codecraft/sand.gif
+ codecraft/water.gif
+ codecraft/wood.gif

आप इस प्रोजेक्ट का पूर्ण संस्करण ‘स्वयंसेवक संसाधन’ भाग में भी देख सकते हैं, जिसमें ये शामिल हैं:

+ codecraft-finished/codecraft.py
+ codecraft-finished/variables.py
+ codecraft-finished/brick.gif
+ codecraft-finished/dirt.gif
+ codecraft-finished/glass.gif
+ codecraft-finished/grass.gif
+ codecraft-finished/plank.gif
+ codecraft-finished/player.gif
+ codecraft-finished/sand.gif
+ codecraft-finished/water.gif
+ codecraft-finished/wood.gif

(उपर्युक्त सभी संसाधन `.zip` फ़ाइलों के रूप में भी डाउनलोड किए जा सकते हैं।)

## अध्ययन के उद्देश्य

+ ग्राफिक्स बनाना और एडिट करना;
+ गेम डिजाइन;
+ एडिटिंग: 
    + वेरिएबल;
    + सूचियाँ;
    + शब्दकोश।

यह प्रोजेक्ट [Raspberry Pi डिजिटल निर्माण पाठ्यक्रम](http://rpf.io/curriculum) के निम्नलिखित तत्वों को सम्मिलित करता है:

+ [बुनियादी 2D और 3D संपदाएँ डिज़ाइन करें |](https://www.raspberrypi.org/curriculum/design/creator)

+ [समस्या को हल करने के लिए प्रोग्रामिंग संरचनाओं को जोड़े।](https://www.raspberrypi.org/curriculum/programming/builder)

## चुनौतियाँ

+ "अपनी दुनिया बनाएँ" - गेम खेलना, मौजूदा ब्लॉकों को रखना और बनाना;
+ "अपनी दुनिया का आकार बदलें" - `MAPWIDTH` और `MAPHEIGHT` वेरिएबल को एडिट करना दुनिया के आकार को बदलने के लिए;
+ "रेत बनाना" - संबंधित खेल डेटा के साथ एक नया रेत संसाधन बनाना।
+ "रेत से काँच बनाना" - एक नया बनाने लायक कांच संसाधन बनाना।
+ "और संसाधन बनाएँ" - अधिक ब्लॉक और क्राफ्टिंग नियम बनाने के लिए जो सीखा गया है उसका उपयोग करें।

## अक्सर पूछे जाने वाले सवाल

+ बच्चों को यह याद दिलाने की आवश्यकता हो सकती है कि शब्दकोश/सूची के तत्व अल्पविराम द्वारा अलग किए गए हैं। उदाहरण के लिए, खेल में इन्वेंट्री वस्तुएं, ग्राफिक्स और क्राफ्टिंग नियमों को जोड़ने पर।

\--- /collapse \---

## \--- collapse \---

## title: प्रोजेक्ट सामग्री

## प्रोजेक्ट संसाधन

+ [सभी प्रोजेक्ट संसाधनों वाली .zip फ़ाइल](http://rpf.io/p/en/codecraft-go)
+ [ऑनलाइन Trinket जिसमें सभी 'कोडक्राफ्ट' प्रोजेक्ट संसाधन हैं](http://rpf.io/codecraft-on)

## क्लब लीडर ले लिए संसाधन

+ [पूरे प्रोजेक्ट संसाधनों वाली .zip फ़ाइल](http://rpf.io/p/en/codecraft-get)
+ [ऑनलाइन पूरा किया गया Trinket प्रोजेक्ट](https://trinket.io/python/ebc5b0148b)

\--- /collapse \---