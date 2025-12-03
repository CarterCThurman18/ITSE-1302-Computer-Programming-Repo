
def string_detect(main_str, sub_str):
    if sub_str in main_str:
        print(f"The string was found at index {main_str.find(sub_str)}")
        return main_str.find(sub_str)
    else:
        print(f"'{sub_str}' was not detected within '{main_str}'.")
        return -1        

def string_input():
    main_str = str(input("Enter the main string you would like to search through:"))
    sub_str = str(input("Enter the sub-string you would like to search for:"))

    return main_str, sub_str
def main():
    print("\n| The Purpose of this Program is to Replace a String or Sections of a String |")
    print("="*78)

    main_str, sub_str = string_input()
    index = string_detect(main_str, sub_str)

    while index >= 0:
        answer = input("Would you like to replace the substring with a new string? (y/n):")
        if answer.lower() == "y" or answer.lower() == "yes":
            print("="*78)
            new_string = input("Please enter the new string:")
            main_str = main_str.replace(sub_str, new_string)
            print(f"\nNew String: {main_str}")
            break
        elif answer.lower() == "n" or answer.lower() == "no":
            print("!No Replacement Was Made And The Program Will Now End!")
            break
        else:
            print("Response not valid, please try again!") 
            
    print("="*78, "\nCompleted by, Carter Thurman")  

if __name__ == "__main__":
    main()

