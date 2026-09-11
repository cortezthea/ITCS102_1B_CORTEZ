#Code Challenge no.3 
#Global Freight Calculator

print ("=========== ITEM INFORMATION ===========")

#Inputs
sender_name = input ("Sender's name:")
item_type = input ("Type of Item:")
is_fragile = input("Fragile (Yes/No):")
weight = float (input("Weight (kg):"))
distance = float (input("Distance (km): "))
is_express = bool(input("Is the delivery express? (yes/no): ") == "yes")
is_international = bool(input("Is the item international? (yes/no): ") == "yes")


#(Calculation)

#Calculate Base Cost 
base_cost = (weight * 2.50) + (distance * 0.15)

#Pricing Tiers 
if weight <= 2.0 and distance <= 100 and not is_express and not is_international:
	total = 0.00

elif is_international and is_express: 
	total = (base_cost * 1.40) + 50

elif is_express or (is_international and weight >20):
	total = (base_cost * 1.20) + 25

elif weight > 30 or distance >1000:
	total = base_cost + 30 

else:
	total = base_cost
	

print ()
print ("=========TOTAL SHIPPING DETAILS=========")
print ("Sender Name     :", sender_name)
print ("Type of Item    :", item_type)
print ("Fragile (Yes|No):", is_fragile) 
print ("Weight          :", weight)
print ("Distance        :", distance)
print ("Express (Yes|No):", is_express)
print ("Int'l (Yes|No)  :", is_international)
print ()
print ("...... TOTAL PRICE  : Php", total, "........")
	 




