contacts: dict = {}

while True:
    print("1. Add Contact")
    print("2. Show Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    user_input = input("What Do You Want To Perform? ")

    if user_input == "1":
        userContact = input("Enter Contact No. ")
        userName = input("Enter Contact Name: ")
        contacts[userName] = userContact

    elif user_input == "2":
        for i in contacts:
            print(f"{i} - {contacts[i]}")

    elif user_input == "3":
        userName = input("Enter Contact Name: ")
        if userName in contacts:
            print(f"{userName} - {contacts[userName]}")
        else:
            print("Contact Not Found!")

    elif user_input == "4":
        userName = input("Enter Contact Name: ")
        if userName in contacts:
            del contacts[userName]
            print(f"{userName} Deleted Successfully!")
        else:
            print("Contact Not Found!")

    elif user_input == "5":
        print("Quit!")
        break
