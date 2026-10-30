#Code Challenge no. 8
# DIAMOND (LOOPS)

for x in range (1, 5):   #top-half
    for y in range (4 - x):
        print ("  ", end = " ")
    for y in range (x):
        print (" *   ", end = " ")
    print ()

for x in range (3,0,-1):    #bottom-half
    for y in range (4 - x):
        print ("  ", end = " ")
    for y in range (x):
        print (" *   ", end = " ")
    print ()






