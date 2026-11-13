#TASK #1-3

#TASK #1
amount = float(input("Your Loan Amount: "))
year = int(input("Input years to pay: "))
months = year*12
principal = amount/months
rem_balance = amount

print ("\n Payment Schedule \n Month \t|    Monthly Payment    |    Interest   | \t Principal \t|\t Remaining Loan")
print ("------------------------------------------------------------------------------------------------")
for count in range (1, months +1):
    rem_balance -= principal
    interest = rem_balance * 0.00256
    pay = interest + principal
    print (f"|  {count}\t|\t{round(pay,2)}\t\t|\t{round(interest,2)}\t|\t{round(principal,2)}\t\t|\t{round(rem_balance,2)}\t\t|")

print ()
print ()

#TASK #2
#dayamond
for x in range (7):
    for y in range (13):
        if x+y == 6 or y - x == 6 or x == 6:
            print ("*", end = "")
        else: 
            print (" ", end = "")
    print ()
print ()
print ()

#Task #3
#letter zi
for x in range (5):
    for y in range (5):
        if x == 0 or x + y == 4 or x == 4:
            print ("*", end = "")
        else:
            print (" ", end = "")
    print ()
print ()
