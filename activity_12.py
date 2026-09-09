#Activity no.12 (Multiple if and elif condition) 

print ("===================AGE GROUP===================")

name = input ("Enter your name:")
age = int (input("Enter your age:"))

if age >=0 and age <=5:
	print ("That age is considered as Infant")
elif age >=6 and age <=12:
	print ("That age is considered as Kid")
elif age >=13 and age <=15:
	print ("That age is considered as Pre teen")
elif age >=16 and age <=19:
	print ("That age is considered as Teenager")
elif age >=20 and age <=29:
	print ("That age is considered as Early Adult")
elif age >=30 and age <=58:
	print ("That age is considered as Adult")
elif age >=59 and age <=150:
	print ("That age is considered as Senior")
else: 
	print ("Age invalid")







