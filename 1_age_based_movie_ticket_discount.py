#Age-based Movie Ticket Discount:

age = int(input("Enter the age: "))

if age < 5:
    price = 0
elif age >= 5 and age <= 18:
    price = 100
elif age >= 19 and age <= 60:
    price = 200
else:  
    price = 50

print("Your ticket price is: INR", price)
