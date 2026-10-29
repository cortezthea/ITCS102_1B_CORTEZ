#Code Challenge no. 6
# THE X

for x in range (5):
    for y in range (5):
        if x+y == 4 or x == y: 
            print ("*", end = "")
        else: 
            print (" ", end = "")
    print ()