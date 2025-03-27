sign = "+", "-", "*", "/"

while True:
    
    print("\nWhat Do You Want To Perform?\n\nAddition: Press '+'\nSubtraction: Press '-'\nMultiplication: Press '*'\nDivision: Press '/'\nPress '-q' to Quit")

    user_input = input("Operation: ")

    # to do addition
    if user_input == "+":
        num1 = float(input("Enter 1st Number: "))
        num2 = float(input("Enter 2nd Number: "))
        print(f"\n{num1} + {num2} = {num1 + num2}")

    # to do subtraction
    elif user_input == "-":
        num1 = float(input("Enter 1st Number: "))
        num2 = float(input("Enter 2nd Number: "))
        print(f"\n{num1} - {num2} = {num1 - num2}")

    # to do multiplication
    elif user_input == "*":
        num1 = float(input("Enter 1st Number: "))
        num2 = float(input("Enter 2nd Number: "))
        print(f"\n{num1} x {num2} = {num1 * num2}")

    # to do division
    elif user_input == "/":
        num1 = float(input("Enter 1st Number: "))
        num2 = float(input("Enter 2nd Number: "))
        print(f"\n{num1} / {num2} = {num1 / num2}")

    # invalid input && quit system
    elif user_input != sign and user_input == "-q":
        print("\nQuit!")
        break
    else:
        print("\nInvalid Input!")

