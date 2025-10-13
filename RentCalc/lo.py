'''
Beginner: Rent Calculator

'''

rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of people living in room/flats = "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons

print(f"Each person will pay {output}")