# import calendar
# yy = 2022
# mm = 11
# print(calendar.month(yy, mm))
# print(dir(calendar))

import random
name = input("Enter your name ")

randomNum = random.randint(0, 1)
score = 0
chance = 3

while chance > 0:
    userGuessNumber = int(input("Enter your guessed number "))
    if(randomNum == userGuessNumber):
        print(name + " wins ")
        break
    else:
        print("computer wins")
    chance -= 1
