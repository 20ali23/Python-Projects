from Library import Library
lib = Library()

print("\nWelcome to the Library Management System")

control = True
while control:

    print("\n------MENU------" + "\n1)List Books" + "\n2)Add Book" + "\n3)Remove Book\n")

    select = input("Select a process step? ")

    if select.lower() == "q":
        control = False

    elif select == "1":
        lib.list_books()

    elif select == "2":
        lib.add_book()

    elif select == "3":
        lib.remove_book()

    else:
        print("Undefined Login Made")
        print("Try Again")