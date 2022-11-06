digit = int(input("Enter three number digit"))
a = digit % 10

print(a)
if(a % 7 == 0):
    print("it is divisible by 7")
else:
    print("it is not divisible by 7")
