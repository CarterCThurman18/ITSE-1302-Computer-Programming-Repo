import locale 

def get_month_income():
    while True:
        try:
            monthly_income = (input("Enter your monthly income:"))
            monthly_income = float(monthly_income)

            if monthly_income < 0:
                raise ValueError("You entered an invalid response, please try again.")
            
            print(f"Your monthly income is: {monthly_income}")
            return monthly_income
        except ValueError as e:
            print(f"{e}")

def get_user_expens():
    print("===============================================================================================================")
    expenses = []
    while True:
            user_expens = input("Enter your monthly expenses one by one\n(Enter 'done' to quit entering expenses): ").strip()
            if user_expens == "done":
                print("\nYou have finished entering expenses.")
                break

            try:
                try:
                    user_expens = float(user_expens)
                    print(user_expens)
                except ValueError:
                    raise ValueError("\nInvalid response, please try again.")

                if user_expens < 0:
                    raise ValueError("\nYou must enter a number equal or greater than 0.") 
                   
            except ValueError as e:
                print(f"\n{e}")
                continue

            expenses.append(user_expens)

    return expenses

def calculate_budget(monthly_income, expenses):
    total_expens = sum(expenses)
    budget_left = monthly_income - total_expens
    return total_expens, budget_left 


def main():
    print("Purpose of this program is the calculate ")
    monthly_income = get_month_income()
    expenses = get_user_expens()
    total_expens, budget_left = calculate_budget(monthly_income, expenses)
    print("===============================================================================================================")
    print(f"\nTotal Income:     ${monthly_income:,.2f}")
    print(f"Total Expenses:     ${total_expens:,.2f}")
    print(f"Remaining Budget:   ${budget_left:,.2f}")

    locale.setlocale(locale.LC_ALL, "en_US") #I finally got this correct after researching it. Took me a while and I still don't fully understand whats happening

    print("\n= Individual Expenses =")
    for i, expense in enumerate(expenses, start=1):
        formatted_expense = locale.currency(expense, grouping=True)
        print(f"{i}. {formatted_expense}")

if __name__ == "__main__":
    main()

print("Completed by, Carter Thurman")
