#Code Challenge No.2


money= input ("Amount:")
print ()
print ("========================= PH BANK DENOMINATION =========================")
print ("Amount to Deposit -->", money)

print ()

a = int (money) // 1000
print ("1000:", a)
money_left = int (money) % 1000

b = int (money_left) // 500
print ("500 :", b)
money_left = int (money_left) % 500

c = int (money_left) // 200
print ("200 :", c)
money_left = int (money_left) % 200

d = int (money_left) //100
print ("100 :", d)
money_left = int (money_left) % 100

e = int (money_left) // 50 
print ("50  :", e)
money_left = int (money_left) % 50

f= int (money_left) // 20
print ("20  :", f)
money_left = int (money_left) % 20

g = int (money_left) // 10 
print ("10  :", g)
money_left = int (money_left) % 10

h = int (money_left) // 5
print ("5   :", h)
money_left = int (money_left) % 5

i = int (money_left) // 1
print ("1   :", i)
money_left = int (money_left) % 1










