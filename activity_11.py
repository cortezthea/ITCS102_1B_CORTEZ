#Activity no.11 (Import demo) 

import getpass #folder 

username = "altheaAC"
password = "cortez18"

u= input ("Username:")
p= getpass.getpass ("Enter your password:")

if u == username and p == password:
	print ("Username and password correct")

else: 
	print ("Incorrect.Recheck your username and password.")
