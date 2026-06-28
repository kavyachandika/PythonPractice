choice = input("""
1. Kilograms to Pounds
2. Pounds to Kilograms

Choose: """)

match choice:

    case "1":

        kg = float(input("Enter kilograms: "))

        pounds = kg * 2.20462

        print("Pounds:", pounds)

    case "2":

        pounds = float(input("Enter pounds: "))

        kg = pounds / 2.20462

        print("Kilograms:", kg)

    case _:

        print("Invalid choice")
