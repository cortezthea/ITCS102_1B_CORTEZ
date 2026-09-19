#AcTivity no. 13 (Bank loan and interest rate approver)

#age (integer)
#is_employed (boolean)
#credit_score (integer)
#annual_income (float)
#has_collateral (boolean)

#need login
#username, password
#loanee first name and job description

#prompt user to enter name/description of collateral
#prompt user the value of the collateral anything less than 30k is invalid

#maximum age for loan is 65
#ask user amount to loan, and the calculated interest rate using base rate


#LOGIN
print("============== LOG IN ==============")
import getpass

username = "altheaAC"
password = "18"

u = input("Enter username: ")
p = getpass.getpass("Enter your password: ")

if u == username and p == password:
    print("Username and password correct. Let's proceed to the next part.")

    #age, code won't run if age is more than 65
    age = int(input("Enter your age: "))

    if age < 21 or age > 65:
        print("Your age must be between 21 and 65.")

    else:
        print("============ LOANEE'S INFORMATION ============")
        name = input("Enter complete name: ")
        job = input("Enter your Job Description: ")

        print(".................................")
        has_collateral = input("Do you have any collateral? ") == "True"

        if has_collateral == True:
            name_collateral = input("What is your collateral (description): ")
            collateral_value = float(input("Enter the value of the collateral: "))
            if collateral_value < 30000:
                print("The value of the collateral must not be less than 30 000")
            else:
                print("Collateral accepted")

        #=======================================================================================
        #inputs
        is_employed = input("Are you currently employed --> ") == "True"
        crdt_score = int(input("Enter your credit score history: "))
        annual_income = float(input("Enter your annual income: "))
        print(".................................")

        #Business Logic and Results
        #Baseline eligibility
        #Financial Evaluation

        if 21 <= age <= 65 and is_employed == True:

            if crdt_score >= 750: #Tier 1
                base_interest_rate = 5.0
                if annual_income >= 100000:
                    base_interest_rate = 4.5
                print("Your final rate is", base_interest_rate, "%")

                #LOAN
                amount_to_loan = float(input("Enter amount to loan: "))
                #INTEREST VALUE
                interest = amount_to_loan * (base_interest_rate / 100)
                total_amount = amount_to_loan + interest

                print(".................................")
                print("Loan Amount:", amount_to_loan)
                print("Interest Rate:", base_interest_rate, "%")
                print("Interest:", interest)
                print("TOTAL AMOUNT:", total_amount)

            elif 600 <= crdt_score < 750: #Tier2
                base_interest_rate = 8.0
                if has_collateral == True and collateral_value >= 30000:
                    base_interest_rate = 7.0
                elif annual_income < 40000:
                    base_interest_rate = 9.5
                print("Your final rate is", base_interest_rate, "%")

                #LOAN
                amount_to_loan = float(input("Enter amount to loan: "))
                #INTEREST VALUE
                interest = amount_to_loan * (base_interest_rate / 100)
                total_amount = amount_to_loan + interest

                print(".................................")
                print("Loan Amount:", amount_to_loan)
                print("Interest Rate:", base_interest_rate, "%")
                print("Interest:", interest)
                print("TOTAL AMOUNT:", total_amount)

            elif crdt_score < 600: #Tier 3
                print("Rejected: Credit score too low")

        else:
            print("Rejected: Fails baseline criteria")

else:
    print("Incorrect. Type your username and password again.")
