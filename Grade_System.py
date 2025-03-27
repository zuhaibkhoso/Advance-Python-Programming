while True:

    # Start Program
    user_input = input("Press Enter to Continue / Type '-q' to Quit!\n")

    if user_input == "-q":
        break
    else:
        pass

    # Getting Marks Input from the User
    obt_marks = int(input("Enter Obtained Marks: "))
    total_marks = int(input("Enter Total Marks: "))

    result = obt_marks / total_marks * 100
    result = round(result, 2)

    # Percentage && Grading System
    if result < 30:
        print(f"Percentage: {result}\nGrade: F\n")

    elif result <= 40:
        print(f"\nPercentage: {result}\nGrade: D\n")

    elif result <= 60:
        print(f"\nPercentage: {result}\nGrade: C\n")

    elif result <= 80:
        print(f"\nPercentage: {result}\nGrade: B\n")

    elif result <= 100:
        print(f"\nPercentage: {result}\nGrade: A\n")

    else:
        print("Done!")