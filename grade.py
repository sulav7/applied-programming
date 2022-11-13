print(''' Sunway Int'l College
           Maitidevi, Kathmandu
**********************************************
           ''')
studentName = input(" Enter name of the student ")
studentAddress = input(" Enter address of the student ")
studentFaculty = input(" Enter faculty of the student ")
studentProgram = input(" Enter the program of the student ")
studentIntake = input(" Enter the intake of the student ")

appliedProgramming, MobileProgramming, Entreprenurship, Communication, DataStructure = input(
    " Enter the marks for applied programming, mobileProgramming,Entreprneurship,Communication,DataStructure ").split(",")

sum = int(appliedProgramming)+int(MobileProgramming) + \
    int(Entreprenurship)+int(Communication)+int(DataStructure)

percentage = sum / 5
if(percentage >= 90):
    Grade = "A+"
elif(percentage > 80 and percentage < 90):
    Grade = "A"
elif(percentage > 70 and percentage <= 80):
    Grade = "B+"
elif(percentage > 60 and percentage <= 70):
    Grade = "B-"
elif(percentage > 50 and percentage <= 60):
    Grade = "B"
elif(percentage > 40 and percentage <= 50):
    Grade = "C+"
elif(percentage > 30 and percentage <= 40):
    Grade = "D"
else:
    Grade = "F"

print(''' Sunway Int'l College
           Maitidevi, Kathmandu
**********************************************
           ''')
print(f"Name : {studentName} ")
print(f"Address : {studentAddress} ")
print(f"faculty : {studentFaculty} ")
print(f"program : {studentProgram} ")
print(f"intake : {studentIntake}")


print(f"percentage : {percentage}")
print(f"Grade: {Grade}")
