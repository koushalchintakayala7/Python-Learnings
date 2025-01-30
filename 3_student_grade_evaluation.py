# Student Grade Evaluation

english = int(input("Enter marks for English: "))
telugu = int(input("Enter marks for Telugu: "))
hindi = int(input("Enter marks for Hindi: "))

total = english + telugu + hindi

if total > 90:
    grade = "A+"
elif total >= 75 and total <= 90:
    grade = "A"
elif total >= 50 and total <= 74:
    grade = "B"
else:
    grade = "Fail"

print("Total Marks:", total)
print("Grade:", grade)






# english = int(input("Enter the marks of English: "))
# telugu = int(input("Enter the marks of Telugu: "))
# hindi = int(input("Enter the marks of Hindi: "))

# total = english + telugu + hindi

# if (total > 90):
#     print("A+")
# elif (total >= 75 and total <= 90):
#     print("A")
# elif (total >= 50 and total < 75):
#     print("B")
# else:
#     print("Fail")