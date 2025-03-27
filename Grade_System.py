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





"""
3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error.
If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

"""