books = {}
users = {}
adm_user = "admin"
adm_pass = "password"

choice = ''
while choice != 3:
    print("\nMAIN MENU")
    print("1. Admin")
    print("2. User")
    print("3. Exit")
    choice = input("Enter your choice(1-3) : ")

    if choice == '1':
        username = input("Enter admin username : ")
        password = input("Enter admin password : ")

        if username == adm_user and password == adm_pass:
            choice1 = ''
            while choice1 !=5 :
                print("\nADMIN MENU")
                print("1. Add Book")
                print("2. Update Book")
                print("3. Delete Book")
                print("4. Display All Books")
                print("5. Exit")
                choice1 = input("Enter your choice: ")

                if choice1 == '1':
                    book_id = input("Enter Book ID: ")
                    if book_id in books:
                        print("Book ID already exists.")
                    else:
                        title = input("Enter Title : ")
                        author = input("Enter Author : ")
                        quantity = input("Enter Quantity : ")
                        books[book_id] = {"title": title, "author": author, "quantity": quantity}
                        print("Book added")

                elif choice1 == '2':
                    book_id = input("Enter Book ID to update: ")
                    if book_id in books:
                        print("1. Update Title")
                        print("2. Update Author")
                        print("3. Update Quantity")
                        choice2 = input("Choose what to update: ")

                        if choice2 == '1':
                            books[book_id]['title'] = input("Enter new title : ")
                        elif choice2 == '2':
                            books[book_id]['author'] = input("Enter new author : ")
                        elif choice2 == '3':
                            books[book_id]['quantity'] = input("Enter new quantity : ")
                        else:
                            print("Invalid option")
                        print("Book updated")
                    else:
                        print("Book ID not found")

                elif choice1 == '3':
                    book_id = input("Enter Book ID to delete : ")
                    if book_id in books:
                        del books[book_id]
                        print("Book deleted")
                    else:
                        print("Book ID not found")

                elif choice1 == '4':
                    a = 0
                    for book_id in books:
                        a = 1
                        b = books[book_id]
                        print("ID:", book_id, " Title:", b['title'], " Author:", b['author'], " Quantity:", b['quantity'])
                    if a == 0:
                        print("No books available")

                elif choice1 == '5':
                    choice1 = 5
                    print("Exit")

                else:
                    print("Invalid option.")
        else:
            print("Invalid admin credentials")

    elif choice == '2':
        choice3 = ''
        while choice3 != 3:
            print("\nUSER SECTION")
            print("1. Register")
            print("2. Login")
            print("3. Back to Main Menu")
            choice3 = input("Enter your choice : ")

            if choice3 == '1':
                username = input("Enter username : ")
                if username in users:
                    print("Username already exists")
                else:
                    phone = input("Enter phone number : ")
                    c = 0
                    for u in users:
                        if users[u]['phone'] == phone:
                            c = 1
                    if c == 1:
                        print("Phone number already used")
                    else:
                        name = input("Enter name : ")
                        age = input("Enter age : ")
                        address = input("Enter address : ")
                        password = input("Enter password : ")
                        users[username] = {"name": name, "age": age, "address": address, "phone": phone, "password": password}
                        print("Registration successful")

            elif choice3 == '2':
                username = input("Enter username : ")
                password = input("Enter password : ")
                if username in users and users[username]['password'] == password:
                    print("Login successful")
                    choice4 = ''
                    while choice4 !=3 :
                        print("\nUSER MENU")
                        print("1. Display All Books")
                        print("2. Search Book by Name")
                        print("3. Exit")
                        choice4 = input("Enter your choice : ")

                        if choice4 == '1':
                            d = 0
                            for book_id in books:
                                d = 1
                                b = books[book_id]
                                print("ID:", book_id, "| Title:", b['title'], "| Author:", b['author'], "| Quantity:", b['quantity'])
                            if d == 0:
                                print("No books available")

                        elif choice4 == '2':
                            search = input("Enter Book to search: ")
                            e = 0
                            for book_id in books:
                                if books[book_id]['title'].lower() == search.lower():
                                    b = books[book_id]
                                    print("ID:", book_id, "| Title:", b['title'], "| Author:", b['author'], "| Quantity:", b['quantity'])
                                    e = 1
                            if e == 0:
                                print("Book not found")

                        elif choice4 == '3':
                            choice4 = 3
                            print("Exit")
                        else:
                            print("Invalid option")
                else:
                    print("Invalid username or password")

            elif choice3 == '3':
                choice3 = 3
                print("Exit")
            else:
                print("Invalid option.")

    elif choice == '3':
        choice = 3
        print("Exiting program")

    else:
        print("Invalid main menu choice.")
