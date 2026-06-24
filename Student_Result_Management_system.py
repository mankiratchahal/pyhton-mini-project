# Student Result Management System

students = {}  # Dictionary to store student records

while True:
    print("\n===== Student Result Management System =====")
    print("1. Add Student")
    print("2. View All Results")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")

        marks = []  # List to store marks

        for i in range(3):
            mark = int(input(f"Enter marks for Subject {i+1}: "))
            marks.append(mark)

        total = sum(marks)
        percentage = total / len(marks)

        # Conditional statements
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 40:
            grade = "C"
        else:
            grade = "Fail"

        # Tuple for storing result summary
        result = (total, percentage, grade)

        # Dictionary to store complete student details
        students[roll_no] = {
            "Name": name,
            "Marks": marks,
            "Result": result
        }

        print("Student record added successfully!")

    elif choice == "2":
        if not students:
            print("No student records found.")
        else:
            print("\n----- Student Results -----")

            # Set to store unique grades
            grades_set = set()

            for roll_no, details in students.items():
                grades_set.add(details["Result"][2])

                print(f"\nRoll No: {roll_no}")
                print(f"Name: {details['Name']}")
                print(f"Marks: {details['Marks']}")
                print(f"Total: {details['Result'][0]}")
                print(f"Percentage: {details['Result'][1]:.2f}%")
                print(f"Grade: {details['Result'][2]}")

            print("\nUnique Grades Awarded:", grades_set)

    elif choice == "3":
        search_roll = input("Enter Roll Number to Search: ")

        if search_roll in students:
            details = students[search_roll]

            print("\nStudent Found!")
            print("Name:", details["Name"])
            print("Marks:", details["Marks"])
            print("Total:", details["Result"][0])
            print("Percentage:", round(details["Result"][1], 2))
            print("Grade:", details["Result"][2])
        else:
            print("Student record not found.")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
