#Act no. 17 (Box)

for x in range (5):
    for y in range (5):
        if y == 4 or x == 0 or x == 4 or y == 0:
            print ("*", end = " ")
        else:
            print (" ", end = " ")
    print ()