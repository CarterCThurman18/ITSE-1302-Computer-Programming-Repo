import csv 

def new_contact_file(): #function for creating a new CSV files which creates a header.
    with open("contacts.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"]) #writing header

        print("A contacts file has been succesfully created") #success message

def add_contact(): #function for adding a contact to the existing CSV file we created. 
    """user input messages that takes the users data, fixes if nessesary
    and stores as variables to be used in append command"""
    name = input("Enter name:").strip().lower() 
    phone = input("Enter phone number with no special characters:").strip()
    email = input("Enter email:").strip().lower()

    """write command that takes the above user input variables and appends 
    them to the existing CSV file"""
    with open("contacts.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email])
    print("Contact was successfully added") #success message

def view_contacts(): #function for viewing/reading all contacts appended to teh CSV file.
    with open("contacts.csv", "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader: #for loop created to print all the rows of contacts in the CSV file in a somewhat readable and organized manner
            print(row[0], "\t\t", row[1], "\t\t", row[2])
            
def modify_contact(): #function for modifying a contact information 
    with open("contacts.csv", "r", newline="") as f: #same command as from the view/read function.
        reader = csv.reader(f)
        contacts_list = list(reader) #new line: takes the CSV file data and creates a list so the data can be edited
        for row in reader:
            print(row[0], "\t\t", row[1], "\t\t", row[2])

    contacts_list = contacts_list[1:] #the list derived from the CSV file will be modified to only include actual contacts and not the header

    edit_name = input("Enter the name of the contact you wish to modify:").strip().lower() #user input to select which contact to modify
    
    found = False #variable for defining if contact entered by user exists
    for row in contacts_list:
        if row and row[0].lower() == edit_name:
            found = True #variable only changes if an existing contact name matches the user input name
            print("Editing contact")
            new_phone = input("Enter new phone #:").strip()
            new_email = input("Enter new email:").strip()
            row[1] = new_phone
            row[2] = new_email
            break

    if found == False: #varible stay the same if the name the user has entered was not found
        print("Contact not found") #fail message
        return #returns the user to menu

    with open("contacts.csv", "w", newline="") as f: #write code that applies the modified list to the CSV file, replacing all data with the list.
        writer = csv.writer(f)    
        writer.writerow(["Name", "Phone", "Email"]) #writes header back into file
        writer.writerows(contacts_list) #writes modified list to file
        print("The edit was successful!") #success message




def main(): #main function
    print("This program is intended for creating, adding, storing, viewing, and modifying contacts") #explaining the purpose of the program

    while True: #while loop that brings the user back to the options menu after completing an action
        choice = int(input("Enter the number corresponding to the action you want to take:\n" \
        "1 - Create a new contact file\n" \
        "2 - Add a new contact to the csv file through the append method\n" \
        "3 - Read all the contacts in the file and output them through the console\n" \
        "4 - Modify an existing contact in the file\n" \
        "5 - Exit the program\n" 
        "Enter your choice:")) #input message that converts to a variable 
        
        # if statement that reads variable and runs corresponding function 
        if choice == 1:
            new_contact_file()
        elif choice == 2:
            add_contact()
        elif choice == 3:
            view_contacts()
        elif choice == 4:
            modify_contact()
        elif choice == 5:
            break 
        else:
            print("Sorry that is an invalid response, please choose again.") #fail statement
        
#calls on main function
if __name__ == "__main__":
    main()

print("Completed by Carter Thurman")
