import math

#prints opening message
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")

#user_choice asks which of the 2 choices the user would like to pick - investment or bond
#.upper() ensures which ever choice they pick it will be understood,
#whether it's inputted using capital letters or lowercase or mix of both.
# i used float so the user can input numbers with a deciamal point.

#user inputs the intial amount, interest rate & how many years they plan on investing
#then the user gets the choice whether they want to choose simple or compound. then the formula runs.

user_choice = input("Please enter your choice: ")
if user_choice.upper() == "INVESTMENT":
    initial_amount = float(input("How much would you like to deposit?: "))
    interest_rate = float(input("What is the interest rate?: "))
    years = int(input("How many years are you planning on investing?: "))

    investment_choice = input("Which would you prefer, simple or compound?: ")
    if investment_choice.upper() == "SIMPLE":
        simple_calculation = initial_amount * (1+(interest_rate / 100) * years)
        print(simple_calculation)
    else:
        investment_choice.upper() == "COMPOUND"
        compound_calculation = initial_amount * math.pow((1+(interest_rate / 100)), years)
        print(compound_calculation)


#here is the elif for 'bond'.
#similar princaple to the part above, user gets asked to input following info.
#then the formula runs.

else:
    user_choice.upper() == "BOND"
    house_value = float(input("How much is the value of the house?: "))
    bond_interest = float(input("What is the interest rate?: "))
    bond_months = int(input("How many months in total are you planning to repay the bond for?: "))

    repayment = ((bond_interest / 100 / 12) * house_value)/(1 - (1 + bond_interest / 100 / 12)**(-bond_months))
    print(f"{repayment:.2f}")

#:.2f will show second decimals even if it's a 0. cuts off extra decimals