# Activity_22
#Lists / Dictionaries
# 2D Dimensional list

#1 (traits)
hiccup = ["courageous","responsible","He changed how humans and dragons coexist."]
astrid =  ["independent","determined","A fierce and fearless Viking warrior"]
toothless = ["loyal","intelligent","The loyal and playful Night Fury"]
stoick = ["protective","courageous","cool"]
print ()
tink = ["inventive","stubborn","A tinker fairy who can fix almost anything."]
silvermist = ["The gentle water fairy","optimistic","empathetic"]
vidia = ["sarcastic","independent","The fastest-flying fairy"]
iridessa = ["cautious","anxious","A responsible light fairy."]
rosetta = ["charming","expressive","The fashionable garden fairy"]
fawn = ["adventurous","compassionate","The adventurous animal fairy with a special love for creatures"]
print ()
woody = ["loyal","leader","Andy's loyal cowboy doll"]
buzz = ["brave","confident","The space ranger"]
jessie = ["energetic","adventurous","The energetic cowgirl with a fearless spirit"]

print ()
vee= ["friendly","optimistic","A friendly vampire girl trying to fit into the human world"]
poppy= ["creative","outgoing","The outgoing and creative best friend"]
bridget=["shy","kindhearted","The shy but sweet girl"]
print ()
elena=["courageous","determined","The brave princess destined to rule the kingdom of Avalor"]
naomi=["practical","resourceful","The clever and resourceful friend who always has a practical solution"]
skylar=["loyal","affectionate","The magical flying jaquin"]
print()
sara=["Imaginative","Resilient","The little princess who never loses her kindness"]
lavinia=["Jealous","Arrogant","A jealous classmate who constantly seeks attention"]
miss_minchin=["Cruel","Authoritarian","Greedy","The cruel headmistress"]

print ()
harry=["Courageous","Selfless","The Boy Who Lived"]
hermione=["Intelligent","Analytical","Diligent","The brightest witch of her age"]
ron=["Humorous","Loyal", "Insecure","Harry's loyal best friend"]
print ()
jesse=["Imaginative","Artistic","The artistic boy who discovers the magic of imagination"]
leslie=["Adventurous","Creative","The imaginative girl who creates the magical kingdom of Terabithia"]
print ()
jack=["Courageous","Humble","A giant-slaying hero"]
princess_isabelle=["Intelligent","Strong-willed","The adventurous princess"]
elmont=["Disciplined","Brave","The courageous leader of the royal guard"]


#2(Characters)
how_to_train_your_dragon = {"Hiccup":hiccup,"Astrid":astrid,"Toothless":toothless,"Stoick":stoick}
tinkerbell = {"Tink":tink,"Silvermist":silvermist,"Vidia":vidia,"Iridessa":iridessa,"rosetta":rosetta,"Fawn":fawn}
toy_story = {"Woody":woody,"Buzz":buzz,"Jessie":jessie}
print ()
vampirina = {"Vee":vee,"Poppy":poppy,"Bridget":bridget}
elena_of_avalor = {"Elena":elena,"Naomi":naomi,"Skylar":skylar}
princess_sarah = {"Sara":sara,"Lavinia":lavinia,"Miss":miss_minchin}
print()
harry_potter = {"Harry":harry,"Hermione":hermione,"ron":ron}
bridge_to_terabithia = {"Jesse":jesse,"Leslie":leslie}
jack_the_giant_slayer = {"Jack":jack,"Princess":princess_isabelle,"Elmont":elmont}

#3 (Categories)
peak = {"HTTYD":how_to_train_your_dragon,"Tinkerbell":tinkerbell,"Toy Story":toy_story}
animated_c = {"Vampirina":vampirina,"EOA":elena_of_avalor,"Princess Sara":princess_sarah}
fantasy = {"Harry Potter":harry_potter,"BTT":bridge_to_terabithia,"JTGS":jack_the_giant_slayer}

#4 (Main Dictionary)
shows = {"Memorable Cartoons":peak, "Fav animated cartoons":animated_c,"Loved fantasy shows":fantasy}

#1
print ("=== 1. Going one at a time ===")
print (shows["Memorable Cartoons"]["HTTYD"]["Hiccup"][1])
print ()

print ("=== 2. Loop level 1: Categories ===")
for category in shows:
    print (category)
print ()

print ("=== 3. Loop levels 1-2: Categories and Titles ===")
for category, titles in shows.items ():
    print (category)
    for title in titles:
        print (" -", title)
print ()

print ("=== 4. Loop all levels ===")
for category, titles in shows.items():
    print (category)
    for title,characters in titles.items():
        print (" " + title)
        for name,info in characters.items():
            print ("   "+ name)
            print ("     Description:", info [0])
            print ("     Traits:", info [1])
print ()

print ("=== 5. Count every character ===")
count = 0
for titles in shows.values():
    for characters in titles.values():
        for name in characters:
            count = count+1
print ("Total characters:",count)
print ()

print ("==== 6. Search for a character ===")
search = "rem"
found = False
for category, titles in shows.items ():
    for title,characters in titles.items ():
        if search in characters:
            print (search, "is from", title, "("+category+")")
            print ("Power:", characters [search][1])
            found = True
if found == False:
    print (search, "not found")
