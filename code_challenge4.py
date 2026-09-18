#Activity no.13 (Bank loan and interset rate approver)

# age (integer)
# is_employed (boolean)
# credit_score (integer)
# annual_income (float)
# has_collateral (boolean)

#need login 
#username, password
#loanee first name and job description 

#prompt user to enter name/description of collateral e.g motorcycle, land, house 
#prompt user the value of the collateral anything less than 30k is invalid 

#maximum age for loan is 65 
#ask user amount to loan, and the calculated interest rate using base rate 

#LOGIN 
print ("============== LOG IN ==============")
import getpass
username = "altheaAC"
password = "18"

u = input ("Enter username:")
p = getpass.getpass ("Enter your password:")

if u == username and p == password:
	print ("Username and password correct. Let's proceed to the next part.")
     
    print ("============ LOANEE'S INFORMATION ============")

    name = input ("Enter complete name: ")
    job = input ("Enter your Job Description ")

#=======================================================================================
    age = int (input("Enter your age: "))
    is_employed = input("Are you currently employed --> ") == "True"
    crdt_score = eval (input("Enter your credit score history: "))
    annual_income = eval (input("Enter your annual income: "))
    has_collateral= input("Do you have any collateral --> ") == "True"
    print (".................................")

# Business Logic and Results
# Baseline eligibility 
# Financial Evaluation

    if age >= 21 and is_employed == True: #Tier 1
        if crdt_score >= 750:
            base_interest_rate = 5.0
            if annual_income >= 100000:
                base_interest_rate = 4.5
            print ("Your final rate is", base_interest_rate)

        elif 600 <= crdt_score < 750: #Tier 2
            base_interest_rate = 8.0
            if has_collateral == True:
                base_interest_rate = 7.0
            elif annual_income < 40000:
                base_interest_rate = 9.5
        print ("Your final rate is", base_interest_rate,"%")

        elif crdt_score < 600: #Tier 3
            print ("Rejected: Credit score too low")
    else: 
        print ("Rejected: Fails baseline criteria")
