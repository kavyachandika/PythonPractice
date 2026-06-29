print("---------------------------------------------\n")
print("---------------------------------------------\n")
print("       SIMPLE STUDENT CALCULATOR       ")
print("---------------------------------------------\n")
print("---------------------------------------------\n")
print("Welcome Kavya!\n")
print("Choose an operation\n")
choice = input("""
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. BMI Calculator
6. Average of 3 marks
7. Exit
""")
match choice:
    case "1":
        num1 = float(input("Enter your first number: \n"))
        num2 = float(input("Enter your second number: \n"))
        print("The sum of the given numbers is ", num1+num2)
    case "2":
        num1 = float(input("Enter your first number: \n"))
        num2 = float(input("Enter your second number: \n"))
        print("The subtraction of the given numbers is ", num1-num2)
    case "3":
        num1 = float(input("Enter your first number: \n"))
        num2 = float(input("Enter your second number: \n"))
        print("The product of the given numbers is ", num1*num2)
    case "4":
        num1 = float(input("Enter your first number: \n"))
        num2 = float(input("Enter your second number: \n"))
        if (num2 == 0):
            print("Invalid")
            num2 = float(input("Enter your second number again: \n"))
        print("The quotient(division) of the given numbers is ", num1/num2)
    case "5":
        weight = float(input("Enter your weight in kilograms: \n"))
        height = float(input("Enter your height in meters: \n"))
        bmi = weight/height**2
        print("Your BMI is ", bmi)
    case "6":
        grade1 = float(input("Enter your first marks: \n"))
        grade2 = float(input("Enter your second marks: \n"))
        grade3 = float(input("Enter your third marks: \n"))
        average = (grade1+grade2+grade3)/3
        print("The average is: ", average)
    case "7":
        print("Goodbye! \n")
    case _:
        print("INVALID CHOICE")
