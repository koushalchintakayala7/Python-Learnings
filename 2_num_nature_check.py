# Number Nature Checker

num = int(input("Enter a number: "))

if num > 0 and num % 2 == 0:
    print("The number is Positive and Even")
elif num > 0 and num % 2 != 0:
    print("The number is Positive and Odd")
elif num < 0 and num % 3 == 0:
    print("The number is Negative and Divisible by 3")
elif num == 0:
    print("The number is Zero")
