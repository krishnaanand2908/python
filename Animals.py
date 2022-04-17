from pickle import TRUE


while(TRUE):
    cat = "The cat is a domestic species of small carnivorous mammal. It is the only domesticated species in the family Felidae and is often referred to as the domestic cat to distinguish it from the wild members of the family."
    dog = "The dog or domestic dog is a domesticated descendant of the wolf which is characterized by an upturning tail. The dog is derived from an ancient, extinct wolf, and the modern wolf is the dog's nearest living relative. "
    cow = "Cattle are large, domesticated, cloven-hooved herbivores. They are a prominent modern member of the subfamily Bovinae and the most widespread species of the genus Bos. Adult females are referred to as cows and adult males are referred to as bulls."
    snake = "Snakes are elongated, limbless, carnivorous reptiles of the suborder Serpentes. Like all other squamates, snakes are ectothermic, amniote vertebrates covered in overlapping scales."
    salamander = "Salamanders are a group of amphibians typically characterized by their lizard-like appearance, with slender bodies, blunt snouts, short limbs projecting at right angles to the body, and the presence of a tail in both larvae and adults. All ten extant salamander families are grouped together under the order Urodela"
    elephant = "Elephants are the largest existing land animals. Three living species are currently recognised: the African bush elephant, the African forest elephant, and the Asian elephant. They are an informal grouping within the proboscidean family Elephantidae."
    eagle = "Eagle is the common name for many large birds of prey of the family Accipitridae. Eagles belong to several groups of genera, some of which are closely related. Most of the 60 species of eagle are from Eurasia and Africa"
    shark = "Sharks are a group of elasmobranch fish characterized by a cartilaginous skeleton, five to seven gill slits on the sides of the head, and pectoral fins that are not fused to the head. Modern sharks are classified within the clade Selachimorpha and are the sister group to the rays."
    humans = "Humans are the most abundant and widespread species of primate, characterized by bipedalism and large, complex brains. This has enabled the development of advanced tools, culture, and language."

    cath = "बिल्ली छोटे मांसाहारी स्तनपायी की घरेलू प्रजाति है। यह फेलिडे परिवार में एकमात्र पालतू प्रजाति है और इसे अक्सर परिवार के जंगली सदस्यों से अलग करने के लिए घरेलू बिल्ली के रूप में जाना जाता है।"
    dogh = "कुत्ता या घरेलू कुत्ता भेड़िये का एक पालतू वंशज है जो एक उलटी पूंछ की विशेषता है। कुत्ता एक प्राचीन, विलुप्त भेड़िये से निकला है, और आधुनिक भेड़िया कुत्ते का निकटतम जीवित रिश्तेदार है।"
    cowh = "मवेशी बड़े, पालतू, कटे हुए खुर वाले शाकाहारी होते हैं। वे सबफ़ैमिली बोविना के एक प्रमुख आधुनिक सदस्य हैं और जीनस बोस की सबसे व्यापक प्रजाति हैं। वयस्क मादा को गाय और वयस्क नर को बैल कहा जाता है।"
    snakeh = "सांप उप-वर्ग सर्पों के लंबे, अंगहीन, मांसाहारी सरीसृप हैं। अन्य सभी स्क्वैमेट्स की तरह, सांप एक्टोथर्मिक होते हैं, एमनियोट कशेरुक अतिव्यापी तराजू में ढके होते हैं।"
    salamanderh = "सैलामैंडर उभयचरों का एक समूह है जो आमतौर पर उनकी छिपकली जैसी उपस्थिति की विशेषता होती है, जिसमें पतले शरीर, कुंद थूथन, शरीर के समकोण पर प्रक्षेपित छोटे अंग और लार्वा और वयस्कों दोनों में एक पूंछ की उपस्थिति होती है। सभी दस मौजूदा समन्दर परिवारों को यूरोडेल के क्रम में एक साथ समूहीकृत किया गया है"
    elephanth = "हाथी सबसे बड़े मौजूदा भूमि जानवर हैं। तीन जीवित प्रजातियों को वर्तमान में मान्यता प्राप्त है: अफ्रीकी झाड़ी हाथी, अफ्रीकी वन हाथी और एशियाई हाथी। वे सूंड परिवार एलिफेंटिडे के भीतर एक अनौपचारिक समूह हैं।"
    eagleh = "ईगल परिवार Accipitridae के शिकार के कई बड़े पक्षियों का सामान्य नाम है। ईगल पीढ़ी के कई समूहों से संबंधित हैं, जिनमें से कुछ निकट से संबंधित हैं। ईगल की 60 प्रजातियों में से अधिकांश यूरेशिया और अफ्रीका से हैं"
    sharkh = "शार्क एक कार्टिलाजिनस कंकाल, सिर के किनारों पर पांच से सात गिल स्लिट्स, और चोटीदार पंख जो सिर से जुड़े नहीं हैं, की विशेषता इलास्मोब्रांच मछली का एक समूह है। आधुनिक शार्क को क्लैड सेलाचिमोर्फा के भीतर वर्गीकृत किया गया है और वे किरणों की बहन समूह हैं।"
    humansh = "मनुष्य प्राइमेट की सबसे प्रचुर और व्यापक प्रजाति है, जो द्विपादवाद और बड़े, जटिल दिमाग की विशेषता है। इसने उन्नत उपकरणों, संस्कृति और भाषा के विकास को सक्षम बनाया है।"

    name = input("Choose your animal:\n cat\n dog\n cow\n snake\n salamander\n elephant\n eagle\n shark\n humans\n")
    l = input("Choose your language:\n H[HINDI]\n E[ENGLISH]\n")
    if name == "cat" and l == "H":
        print(cath)
    elif name == "cat" and l == "E":
        print(cat)
    elif name == "dog" and l == "H":
        print(dogh)
    elif name == "dog" and l == "E":
        print(dog)
    elif name == "cow" and l == "H":
        print(cowh)
    elif name == "cow" and l == "E":
        print(cow)
    elif name == "snake" and l == "H":
        print(snakeh)
    elif name == "snake" and l == "E":
        print(snake)
    elif name == "salamander" and l == "H":
        print(salamanderh)
    elif name == "salamander" and l == "E":
        print(elephant)
    elif name == "elephant" and l == "H":
        print(elephanth)
    elif name == "elephant" and l == "E":
        print(elephant)
    elif name == "eagle" and l == "H":
        print(eagleh)
    elif name == "eagle" and l == "E":
        print(eagle)
    elif name == "shark" and l == "H":
        print(sharkh)
    elif name == "shark" and l == "E":
        print(shark)
    elif name == "humans" and l == "H":
        print(humansh)
    elif name == "humans" and l == "E":
        print(humans)
    else:
        print("The entered name, language or both are WRONG!\n Please try again." )
        
    continue