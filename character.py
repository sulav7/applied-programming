print('''
            Welcome to Sunway Character Check System
                    Maitidevi, Kathmandu

''')

string = input("Enter something: ")
upper = 0
lower = 0
number = 0
special = 0
for i in range(len(string)):
    if 65 <= ord(string[i]) <= 90:
        upper += 1
    elif 97 <= ord(string[i]) <= 122:
        lower += 1
    elif 48 <= ord(string[i]) <= 56:
        number += 1
    else:
        special += 1

print(f"Upper: {upper}")
print(f"Lower: {lower}")
print(f"Digit: {number}")
print(f"Special: {special}")
print("Thank you for the visit")
