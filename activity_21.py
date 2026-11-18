#The Interactive Jeepney

#Part I
passengers = ["Ana","Ben", "Carla"]
passengers.append ("Dan")
passengers.insert (0, "Lola")
passengers.remove ("Ben")
x = passengers.pop ()
y = passengers.pop (0)
len (passengers)
passengers.reverse ()
print (passengers)

#Part II
route = ["Terminal", "Perez park", "Pacific Mall"]
passengers = [] #during execution
seats = 6
fare = 13
total = 0

while True:
    print()
    print("Sakay:", passengers)
    print(len(passengers), "of", seats, "seats")
    print("1 Sakay\n2 Priority seat \n3 Para po!")
    print("\n4 Baba sa pinto \n5 Baba sa harap")
    print("\n6 Seat check \n7 Balikan \n8 Exit")
    choice = input("Choice: ")

    if choice == "1":
        if len (passengers) == seats: #how many items
            print ("Puno na!")
        else:
            name = input ("Name: ")
            passengers.append (name)
            total = total + fare
            print (name, "boarded at the back")

    elif choice == "2":
        if len (passengers) == seats:
            print ("Puno na!")
        else:
            name = input ("Name: ")
            passengers.insert (0, name)
            total = total + fare
            print (name, "took the priority seat")

    elif choice == "3":
        name = input("who is getting off? ")
        if name in passengers:
            passengers.remove (name) #remove specifix
            print (name, "got off. Ingat!")
        else:
            print (name, "is not on this jeep")

    elif choice == "4":
        if len (passengers) == 0:
            print ("The jeep is empty")
        else:
            left = passengers.pop () #index
            print (left, "got off at the door")

    elif choice == "5":
        if len (passengers) == 0:
            print ("The jeepney is empty")
        else:
            front = passengers.pop ()
            print (front, "got off at the front")

    elif choice == "6":
        for i in range (len(passengers)):
            print ("Seat", i + 1, passengers [i])

    elif choice == "7":
        route.reverse ()
        print ("route:", route)

    elif choice == "8":
        print ("Total fare today:", total)
        break

    else:
        print ("Invalid choice.")
