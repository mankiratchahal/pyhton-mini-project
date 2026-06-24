# Library Management System

library = {}  # Dictionary to store books

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        # Tuple to store book information
        book_info = (title, author)

        # Dictionary entry
        library[book_id] = {
            "BookInfo": book_info,
            "Status": "Available"
        }

        print("Book added successfully!")

    elif choice == "2":
        if not library:
            print("No books available in the library.")
        else:
            print("\n----- Book List -----")

            # Set for unique authors
            authors = set()

            for book_id, details in library.items():
                authors.add(details["BookInfo"][1])

                print(f"\nBook ID: {book_id}")
                print(f"Title: {details['BookInfo'][0]}")
                print(f"Author: {details['BookInfo'][1]}")
                print(f"Status: {details['Status']}")

            print("\nUnique Authors:", authors)

    elif choice == "3":
        book_id = input("Enter Book ID to Issue: ")

        if book_id in library:
            if library[book_id]["Status"] == "Available":
                student_name = input("Enter Student Name: ")

                # List to store issued student names
                if "IssuedTo" not in library[book_id]:
                    library[book_id]["IssuedTo"] = []

                library[book_id]["IssuedTo"].append(student_name)
                library[book_id]["Status"] = "Issued"

                print("Book issued successfully!")
            else:
                print("Book is already issued.")
        else:
            print("Book not found.")

    elif choice == "4":
        book_id = input("Enter Book ID to Return: ")

        if book_id in library:
            if library[book_id]["Status"] == "Issued":
                library[book_id]["Status"] = "Available"
                print("Book returned successfully!")
            else:
                print("Book is already available.")
        else:
            print("Book not found.")

    elif choice == "5":
        search_title = input("Enter Book Title to Search: ").lower()

        found = False

        for book_id, details in library.items():
            if details["BookInfo"][0].lower() == search_title:
                print("\nBook Found!")
                print("Book ID:", book_id)
                print("Title:", details["BookInfo"][0])
                print("Author:", details["BookInfo"][1])
                print("Status:", details["Status"])
                found = True
                break

        if not found:
            print("Book not found.")

    elif choice == "6":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
