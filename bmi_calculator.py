weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
BMI = weight/(height*height)
print("Your BMI is: ", BMI)
if BMI < 18.5:
    print("You are underweight")
elif BMI >= 18.5 and BMI <= 24.9:
    print("You are normal weight")
elif BMI >= 25.0 and BMI <= 29.9:
    print("You are overweight")
elif BMI > 29.9:
    print("You are obese ")
else:
    print("Invalid")
