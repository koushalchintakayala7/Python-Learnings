# Electricity Bill Calculator

units = int(input("Enter the unit consumed: "))

if units <= 50:
    print("Total Bill Amount: INR", 3 * units)
elif units <= 150:
    print("Total Bill Amount: INR", 5 * units)
else:
    print("Total Bill Amount: INR", 8 * units)