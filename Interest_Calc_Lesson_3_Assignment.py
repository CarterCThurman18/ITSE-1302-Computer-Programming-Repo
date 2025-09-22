# Code for amount of money the user would like to invest, variable and input
monthly_investment = int(input("Enter an amount between 0 and 50000 you would like to invest: "))

while monthly_investment < int(0) or monthly_investment > int(50000):
    print("You have entered an invalid amount, please enter a number between 0 and 50000")
    monthly_investment = int(input("Enter amount you would like to invest: "))

print(f"Your investment amount of ${monthly_investment} is valid")
#
#
# Code for desired yearly interest rate variable and input     
int_rt_intgr_yrly = int(input("Enter your desired interest rate between 0 and 15: "))

while int_rt_intgr_yrly < int(0) or int_rt_intgr_yrly > int(15):
    print("You have entered an invalid interest rate, please enter a number between 0 and 15")
    int_rt_intgr_yrly = int(input("Enter your desired interest rate: "))

    print(f"You have entered a valid interest rate of {int_rt_intgr_yrly}%")
#
#
# Code for number of years variable and input
investment_duration_yrs = int(input("Enter number of years you would like to invest: "))

while investment_duration_yrs < int(0):
    print("You have entered an invalid amount, please enter a number greater than 0")
    investment_duration_yrs = int(input("Enter number of years you would like to invest: "))

    print(f"You have entered a valid number of {investment_duration_yrs}.")
#
#
# Math to convert number of yearss investing to months
investment_duration_months = investment_duration_yrs * 12 
# Math to convert yearly interest rate to the equivalent monthly interest rate
monthly_interest_rate = (int_rt_intgr_yrly / 12) / 100
# Variable for future total
future_total = 0
#
#
years = 0
#
# for statement which does all the compounding 
for investment_duration_months in range(investment_duration_months):
    future_total += monthly_investment
    interest = future_total * monthly_interest_rate
    future_total += interest
    if (investment_duration_months + 1) % 12 == 0:
            years = (investment_duration_months + 1) // 12
            print(f"Year {years}: ${round(future_total, 2)}")
#
#
int_rt_intgr_yrly = float(int_rt_intgr_yrly)#Turn the interest into a float value
# Final print statements
print(f"Investment Duration: {investment_duration_yrs} years")
print(f"Yearly Interest Rate: {int_rt_intgr_yrly}%")
print(f"Monthly Investment Amount: ${monthly_investment}")
print(f"Total amount after Compounding: ${round(future_total, 2)}")
#
print("============================================")
print("Completed by, Carter Thurman")