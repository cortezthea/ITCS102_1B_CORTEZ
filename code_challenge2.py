#Code Challenge No.2


money= 18796
print ("Amount to Deposit -->", money)

print ()

a = money // 1000
print ("1000:", a)
money_left = money % 1000
#Value:18 Left:796

b = money_left // 500
print ("500 :", b)
money_left = money_left % 500
#Value:1 Left: 296

c = money_left // 200
print ("200 :", c)
money_left = money_left % 200
#Value:1 Left: 96

d = money_left //100
print ("100 :", d)
money_left = money_left % 100
#Value:0 Left:96

e = money_left // 50 
print ("50  :", e)
money_left = money_left % 50
#Value:1 Left:46

f= money_left // 20
print ("20  :", f)
money_left = money_left % 20
#Value:2 Left: 6

g = money_left // 10 
print ("10  :", g)
money_left = money_left % 10
#Value:0 Left:6

h = money_left // 5
print ("5   :", h)
money_left = money_left % 5
#Value:1 Left:1

i = money_left // 1
print ("1   :", i)
money_left = money_left % 1
#Value:1 Left:0










