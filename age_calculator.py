first_name = input("|First name: ")
last_name = input("|Last name: ")
current_year = int(input("|What is the current year?\n|"))
birth_year = int(input("|What year were you born?\n|"))
age = current_year - birth_year

print("|Greetings", str(first_name), str(last_name) + ", using my totally legit powers \n"
"|I know that in the year of our Lord", int(current_year) ,"you are", int(age), "years old.")

age += 1
current_year += 1
print("\n")
print(f"|I can also predict that in the year of our Lord {current_year} you will be {age}", end = "!") 
print("\n")
print("Completed by, Carter Thurman")


