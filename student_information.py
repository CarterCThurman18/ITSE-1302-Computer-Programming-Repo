def main():
    stu_info={
        "Owen":{
        "id":"67",
        "gpa":"1.0",
        "credits completed":"35",
        "grades":"[67, 75, 42, 0, 100]"
        },
        "Carter":{
        "id":"18",
        "gpa":"3.7",
        "credits completed":"28",
        "grades":"[80, 75, 88, 98, 100]"
        }}
    print(stu_info)
    print("================================= \nStudent names:")

    for key in stu_info:
        print(key)
    
    print("\nStudent information:")
    print("Name\tID\tGPA\tCredits Completed\tGrades")
    for key in stu_info:
        print(f"{key}\t{stu_info[key]["id"]}\t{stu_info[key]["gpa"]}\t\t{stu_info[key]["credits completed"]}\t\t{stu_info[key]["grades"]}")

    print("\nGetting info using Key in a loop:")
    for key in stu_info:
        print(f"{key}: {stu_info[key]}")

    print("\nCarter has been removed from dictionary:")
    stu_info.pop("Carter")
    for key in stu_info:
        print(f"{key}: {stu_info[key]}")

    print("\nGetting GPA information:")
    for key in stu_info:
        print(f"{key}: {stu_info[key]["gpa"]}")

    print("\nCLEARING STUDENT REGISTRY!!!:")
    stu_info.clear()
    print(f"{stu_info}")

if __name__ == "__main__":
    main()

print("Completed by Carter Thurman")