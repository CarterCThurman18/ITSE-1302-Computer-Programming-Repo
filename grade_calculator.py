def main(): 
    import random

    grades_list = []
    grade_input = 0

    while grade_input > -1: 
        if (len(grades_list)) < 1:
            grade_input = int(input("Input student grades as a whole number one at a time or \nenter the value -1 to stop entering grades: ")) 
            #You need the "int" on line 5 or else anything you enter will convert "grade_input" into a str which is no bueno.
        else:
            grade_input = int(input("Input student grade: ")) 

        if grade_input == -1:
            break
        else:
            grades_list.append(grade_input)
    print(grades_list)
    #=============================================
    print("=============================================")
    print("|REMOVING LOWEST GRADE|")
    print(min(grades_list))
    grades_list.pop(grades_list.index(min(grades_list)))
    print(grades_list)
    #=============================================
    print("=============================================")
    print("|REMOVING RANDOM GRADE|")
    grades_list.remove(random.choice(grades_list))
    print(grades_list)
    #=============================================
    print("=============================================")
    print("|EDITING GRADE|")

    for counter, item in enumerate(grades_list, start=1): #This will not print the correct index for each item. It will be +1 of original index because starting at 1. Line 49 ->

        print(f"{counter}. {item}")

    #Get input for what grade to edit
    
    while True:
        index_ = int(input("Which grade do you want to edit?:"))
        if 1 <= index_ <= len(grades_list):
            break
        print("Invalid input, please try again.")
        
    index_ -= 1 #Converting back to original index count
            
    new_grade = int(input("Enter new grade:")) #User enters new grade

    grades_list.pop (index_) #Old grade is replaced with new grade
    grades_list.insert(index_, new_grade)
    
    print("Updated list:", grades_list)
    #=============================================
    print("=============================================")
    print("SORTING AND REVERSING LIST")
    grades_list.sort()
    grades_list.reverse()
    print(grades_list)
    #=============================================
    print("=============================================")
    print("Total", sum(grades_list))
    average_grade = (sum(grades_list)) / (len(grades_list))
    print("Average:", average_grade)

if __name__ == "__main__":
    main()

print("Completed by Carter Thurman")