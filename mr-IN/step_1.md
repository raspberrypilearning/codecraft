## प्रस्तावना

या प्रकल्पात तुम्ही Minecraft च्या 2D आवृत्तीमध्ये डिझाइन आणि कोड सुधारणा कराल.

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/ebc5b0148b?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/craft-finished.png">
</div>

### क्लब प्रमुखांसाठी अधिक माहिती

आपल्याला जर हा प्रकल्प प्रिंट करायचा असेल तर आपण [प्रिंटर अनुकूल आवृत्ती](https://projects.raspberrypi.org/mr-IN/projects/codecraft/print) चा वापर करू शकता.

--- collapse ---
---
title: क्लब प्रमुखांसाठी टिप
---

## प्रस्तावना:

या प्रकल्पात मुले मूलभूत 2D Minicraft clone मध्ये सुधारणा करुन ग्राफिक्स आणि खेळ डिझाइनचे करायचे पैलू जाणून घेतील. मुले नवीन संसाधने तयार करतील, तसेच संसाधने एकत्रित करण्यासाठी नवीन craft नियम तयार करतील. व्हेरिएबल्स, याद्या आणि शब्दकोष समजून घेऊन हाताळण्याद्वारे उद्देश साध्य होईल.

## ऑनलाईन संसाधने

हा प्रकल्प **Python 3** चा वापर करतो. Python ऑनलाईन लिहिण्यासाठी आम्ही [trinket](https://trinket.io/) वापरण्याचा सल्ला देतो. या प्रकल्पात पुढील Trinkets आहेत:

+ ['CodeCraft' स्टार्टर प्रकल्प - rpf.io/codecraft-on](https://rpf.io/codecraft-on)

येथे पूर्ण झालेले प्रकल्प असलेले एक trinket देखील आहे:

+ ['CodeCraft' समाप्त - trinket.io/python/ebc5b0148b](https://trinket.io/python/ebc5b0148b)

## ऑफलाइन संसाधने

तुम्हाला पसंत असल्यास हा प्रकल्प [ऑफलाइन पूर्ण केला जाऊ शकतो](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/)केला जाऊ शकतो. तुम्ही या प्रकल्पाची संसाधने 'Project Materials' link वर​ क्लिक करून मिळवू शकता. ह्या लिंक मध्ये एक 'Project Resources' नामक विभाग आहे, ज्यामध्ये मुलांना हा प्रकल्प ऑफलाइन पूर्ण करण्यासाठी लागणारी संसाधने आहेत. प्रत्येक मुलाकडे संसाधनांची प्रत असल्याचे सुनिश्चित करा. या विभागात खालील फायली समाविष्ट आहेत:

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

तुम्हाला या प्रकल्पातील आव्हानांची पूर्ण आवृत्ती 'Volunteer Resources' विभागात सापडेल, ज्यात खालील बाबी आहेत:

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

(वरील सर्व प्रकल्प संसाधने `.zip` फायली म्हणून डाउनलोड करण्यायोग्य देखील आहेत.)

## शिकण्याचे उद्दिष्टे

+ ग्राफिक्स तयार करणे आणि संपादित करणे;
+ खेळ संरचना;
+ संपादन: 
    + व्हेरियेबल;
    + याद्या;
    + शब्दकोश.

या प्रकल्पात [Raspberry Pi Digital Making Curriculum](https://rpf.io/curriculum) चे खालील घटक समाविष्ट आहेत:

+ [मूलभूत 2Dआणि 3D मालमत्ता डिझाइन करा.](https://www.raspberrypi.org/curriculum/design/creator)

+ [समस्या सोडवण्यासाठी प्रोग्रामिंग संकल्पना एकत्र करा.](https://www.raspberrypi.org/curriculum/programming/builder)

## आव्हाने

+ "Build your world" - खेळ खेळणे, अस्तित्वातील अवरोध ठेवणे आणि हस्तकला तयार करणे
+ "Change your world size" - `MAPWIDTH` आणि `MAPHEIGHT` world चा आकार बदलण्यासाठी variables संपादित करा;
+ "Creating sand" - खेळाच्या संबंधित डेटासह नवीन वाळू संसाधन तयार करणे.
+ "Crafting glass from sand" - नवीन कलायोग्य काचेचे संसाधने तयार करणे.
+ "अधिक संसाधने तयार करा" - अधिक अवरोध आणि हस्तकला नियम तयार करण्यासाठी काय शिकले आहे ते वापरा.

## वारंवार विचारले जाणारे प्रश्न

+ शब्दकोष / सूचीचे घटक स्वल्पविरामाने विभक्त केले आहेत हे मुलांना स्मरण करून देण्याची आवश्यकता असू शकते. उदाहरणार्थ, खेलामधील साहित्य याद्या, ग्राफिक्स आणि हस्तकला करण्याचे नियम.

--- /collapse ---

--- collapse ---
---
title: प्रकल्प साहित्य
---

## प्रकल्प संसाधने

+ [सर्व प्रकल्पाची संसाधने असलेली.zip फाइल](resources/codecraft-resources.zip)
+ [ऑनलाईन Trinketज्यात सर्व 'CodeCraft' प्रकल्प संसाधने आहेत](https://rpf.io/codecraft-on)

## क्लब प्रमुखसाठी संसाधने

+ [सर्व पूर्ण प्रकल्पाची संसाधने असलेली.zip फाइल](solutions/codecraft-solution.zip)
+ [ऑनलाईन पूर्ण Trinket प्रकल्प](https://trinket.io/python/ebc5b0148b)

--- /collapse ---
