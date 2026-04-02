import os

while True:
    print("\n===== BOOKIFY SYSTEM =====")
    print("1. Signup")
    print("2. Login")
    print("3. Book Ticket")
    print("4. View Ticket")
    print("5. Search Train")
    print("6. Cancel Ticket")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        os.system("python signup.py")
    elif choice == "2":
        os.system("python login.py")
    elif choice == "3":
        os.system("python book_ticket.py")
    elif choice == "4":
        os.system("python view_ticket.py")
    elif choice == "5":
        os.system("python search_train.py")
    elif choice == "6":
        os.system("python cancel_ticket.py")
    elif choice == "7":
        break
