# Activity_22
#Lists / Dictionaries
# 2D Dimensional list

#1 (traits)
hiccup = ["courageous","a leader","compassionate"]
astrid =  ["independent","determined","brave"]
toothless = ["loyal","intelligent","playful"]
stoick = ["protective","courageous","cool"]
print ()
tink = ["inventive","stubborn","curious"]
silvermist = ["gentle","optimistic","empathetic"]
vidia = ["sarcastic","independent","competitive"]
iridessa = ["cautious","anxious","responsible"]
rosetta = ["charming","expressive","elegant"]
fawn = ["adventurous","compassionate","fearless"]
print ()
woody = ["loyal","leader","responsible"]
buzz = ["brave","confident","heroic"]
jessie = ["energetic","adventurous","emotional"]

print ()
vee= ["friendly","optimistic","adaptable"]
poppy= ["creative","outgoing","supportive"]
bridget=["shy","kindhearted","thoughtful"]
print ()
elena=["courageous","determined","strong"]
naomi=["practical","resourceful","assertive"]
skylar=["loyal","affectionate","energetic"]
print()
sara=["Imaginative","Resilient","Generous"]
lavinia=["Jealous","Arrogant","Insecure"]
miss_minchin=["Cruel","Authoritarian","Greedy","Prideful"]

print ()
harry=["Courageous","Selfless","Impulsive"]
hermione=["Intelligent","Analytical","Diligent","Perfectionistic"]
ron=["Humorous","Loyal", "Insecure","Protective"]
print ()
jesse=["Imaginative","Artistic","Sensitive"]
leslie=["Adventurous","Creative","Fearless"]
print ()
jack=["Courageous","Humble","Selfless"]
princess_isabelle=["Intelligent","Strong-willed","Compassionate"]
elmont=["Disciplined","Brave","Loyal"]


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
            print ("     Power:", info [1])
print ()

print ("=== 5. Count every character ===")
count = 0
for titles in shows.values ():
    for characters in title.values ():
        for name in characters:
            count = count+1
print ("Total characters:",count)
print ()

print ("==== 6. Search for a character ===")
search = "rem"
found = False
for category, titles in anime.items ():
    for title,characters in titles.items ():
        if search in characters:
            print (search, "is from", title, "("+category+")")
            print ("Power:", characters [search][1])
            found = True
if found == False:
    print (search, "not found")
