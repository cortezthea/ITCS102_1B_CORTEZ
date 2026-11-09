#Act no. 19 (While Loop #2)

from getpass import getpass
isLogin= False
loginAttempt= 0

u= "TheAC"
p= "888"

while isLogin == False:
    uname = input ("Input USERNAME: ")
    pword = getpass ("Input PASSWORD: ")

    if uname == u and pword == p:
        print ("Login Successfully")
        print ("Total Login Attempts", loginAttempt)
        isLogin = True

    else:
        print ("Incorrect Username and Password")
        loginAttempt += 1
        isLogin = False