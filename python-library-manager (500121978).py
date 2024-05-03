# changes I made after half evaluation : ask user to select admin or user define opertion for admin and user seprately.

'''Library Management System with Admin and User Interfaces'''

library = {} # Dictionary to store books in the library
users = {}# Dictionary to store users of the system
admin_password = "chirag1250"# Admin password required to access admin functionalities

def add_book(title, author):
    library[title] = author
    print(f"Book '{title}' by {author} added to the library.")

def remove_book(title):
    if title in library:
        del library[title]
        print(f"Book '{title}' removed from the library.")
    else:
        print(f"Book '{title}' is not in the library.")

def display_books():
    if library:
        print("Books in the library:")
        for title, author in library.items():
            print(f"{title} by {author}")
    else:
        print("The library is empty.")

def add_user(user_id, name):
    if user_id in users:
        print(f"User with ID {user_id} already exists.")
    else:
        password = user_id[-4:]  # Set password as last four digits of user ID
        users[user_id] = {'name': name, 'password': password}
        print(f"User '{name}' with ID {user_id} added.")

def remove_user(user_id):
    if user_id in users:
        del users[user_id]
        print(f"User with ID {user_id} removed.")
    else:
        print(f"User with ID {user_id} not found.")

def issue_book(title, user_id, password):
    if title in library:
        if user_id in users:
            if password == users[user_id]['password']:
                print(f"Book '{title}' issued to {users[user_id]['name']}.")
            else:
                print("Incorrect password.")
        else:
            print(f"User with ID {user_id} not found.")
    else:
        print(f"Book '{title}' is not available in the library.")

def return_book(title, user_id):
    if title in library:
        print(f"Book '{title}' returned by {users[user_id]['name']}.")
    else:
        print(f"Book '{title}' is not available in the library.")

def admin_menu():
    while True:
        print("\nAdmin Menu")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Display Books")
        print("4. Add User")
        print("5. Remove User")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            add_book(title, author)
        elif choice == '2':
            title = input("Enter the title of the book to remove: ")
            remove_book(title)
        elif choice == '3':
            display_books()
        elif choice == '4':
            user_id = input("Enter the user ID: ")
            name = input("Enter the name of the user: ")
            add_user(user_id, name)
        elif choice == '5':
            user_id = input("Enter the user ID to remove: ")
            remove_user(user_id)
        elif choice == '6':
            print("Exiting admin menu.")
            break
        else:
            print("Invalid choice. Please try again.")

def user_menu():
    while True:
        print("\nUser Menu")
        print("1. Display Books")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            display_books()
        elif choice == '2':
            title = input("Enter the title of the book: ")
            user_id = input("Enter your user ID: ")
            password = input("Enter your password: ")
            issue_book(title, user_id, password)  # Pass the password
        elif choice == '3':
            title = input("Enter the title of the book to return: ")
            user_id = input("Enter your user ID: ")
            return_book(title, user_id)
        elif choice == '4':
            print("Exiting user menu.")
            break
        else:
            print("Invalid choice. Please try again.")

def main():            # Main function to start the program
    print("Welcome to the Library Management System")
    while True:
        user_type = input("Are you an admin or a user? Enter 'admin' or 'user': ")
        if user_type.lower() == 'admin':
            password = input("Enter admin password: ")
            if password == admin_password:
                admin_menu()
            else:
                print("Incorrect password. Access denied.")
        elif user_type.lower() == 'user':
            user_menu()
        else:
            print("Invalid user type.")

        cont = input("Do you want to continue? (yes/no): ")
        if cont.lower() != 'yes':
            print("Exiting the program.")
            break

main()                 # Call the main function directly
