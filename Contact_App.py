contacts: dict = {}

while True:

    # Start Program
    user_input = input("\nPress Enter to Continue / Type 'q' to Quit!\n")

    if user_input == "q":
        break
    else:
        pass


    print("1. Add Contact")
    print("2. Show Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")

    # type option number to perform a task
    user_input = input("What Do You Want To Perform? ")

    # add contacts
    if user_input == "1":
        userContact = input("Enter Contact No. ")
        userName = input("Enter Contact Name: ")
        userName = userName.capitalize()
        contacts[userName] = userContact

    # show contacts
    elif user_input == "2":
        for i in contacts:
            print(f"{i} - {contacts[i]}")

    # search contacts
    elif user_input == "3":
        userName = input("Enter Contact Name: ")
        userName = userName.capitalize()
        if userName in contacts:
            print(f"\n{userName} - {contacts[userName]}")
        else:
            print("Contact Not Found!")

    # delete contacts
    elif user_input == "4":
        userName = input("Enter Contact Name: ")
        userName = userName.capitalize()
        if userName in contacts:
            del contacts[userName]
            print(f"\n{userName} Deleted Successfully!")
        else:
            print("Contact Not Found!")
