# Vowel or Consonant Checker

c = input("Enter a Character: ")
v = "a,e,i,o,u"

if c in v:
    print(c, "is a Vowel")
elif c not in v:
    print(c, "is a Consonant")
else:
    print(c, "is not a alphabet")