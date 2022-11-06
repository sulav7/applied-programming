firstNumber = int(input("Enter first number "))
secondNumber = int(input(" Enter second number"))
thirdNumber = int(input(" Enter third number"))

if firstNumber > secondNumber and firstNumber > thirdNumber:
    print(f"firstNumber is greater = {firstNumber}")
elif secondNumber > firstNumber and secondNumber > thirdNumber:
    print("secondNumber is greater")
else:
    print("third number is greater")
