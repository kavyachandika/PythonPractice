Firstname = input("Enter your first name\n")
Lastname = input("Enter your last name\n")
item1 = input("Enter the name of your first item\n")
price1 = float(input("Enter the price of your first item\n"))
item2 = input("Enter the name of your second item\n")
price2 = float(input("Enter the price of your second item\n"))
item3 = input("Enter the name of your third item\n")
price3 = float(input("Enter the price of your third item\n"))
total = price1+price2+price3
tax_rate = 0.0825
tax_amount = total * tax_rate
total_price = total + tax_amount
print("Welcome", Firstname, " ", Lastname)
print(item1, " $", price1)
print(item2, " $", price2)
print(item3, " $", price3)
print("subtotal = ", total)
print("tax = ", tax_amount)
print("total = ", total_price)
print("Thank you!")
