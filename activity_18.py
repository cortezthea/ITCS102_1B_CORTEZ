# #Act no. 18 (While Loop)
# Boolean varlable
tuloy = True

while tuloy == True:
    ask = input ("Do you wish to continue this program (yes/no): ")

    if ask.lower () == "yes":
        print ("Continuing...")
        continue
    else:
        print ("Stopping now.")
        break

