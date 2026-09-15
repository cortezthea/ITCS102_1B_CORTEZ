#Activity no.13 (Business Loan)

# age (integer)
# is_employed (boolean)
# credit_score (integer)
# annual_income (float)
# has_collateral (boolean)

age = int (input("Enter your age: "))
is_employed = bool (input("Are you currently employed --> "))
crdt_score = eval (input("Enter your credit score history: "))
annual_income = eval (input("Enter your annual income: "))
has_collateral = bool (input("Do you have any collateral --> "))
#might change the bool function into : is_employed = input("Are you currently employed --> ") == "True"
#might change the bool function into : has_collateral= input("Do you have any collateral --> ") == "True"
print (".................................")

# Business Logic and Results
# Baseline eligibility 
# Financial Evaluation: Tier 1, Tier 2, Tier 3

if age >= 21 and is_employed == True: 

    if crdt_score >= 750:
        base_interest_rate = 5.0
        if annual_income >= 100000:
                base_interest_rate = 4.5
        print ("Your final rate is 4.5%")
    
    elif 600 <= crdt_score < 750:
        base_interest_rate = 8.0
        if has_collateral == True:
            base_interest_rate = 7.0
        elif annual_income < 40000:
            base_interest_rate = 9.5
        print ("Your final rate is", base_interest_rate,"%")

    elif crdt_score < 600:
        print ("Rejected: Credit score too low")
        
else: 
    print ("Rejected: Fails baseline criteria")
