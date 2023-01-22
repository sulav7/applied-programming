from datetime import date
custName = []
custAddress = []
custPhone = []
custEmail = []

total = []
netTotal = []
discount = []

heading = '''Sunway College BhatBhateni Maitidevi,Kathmandu 
Phone: 01-415463'''
heading2 = "\nCustomer Billing Software\n"
heading3 = date.today()
heading4 = "-------------------------------------------------\n"


def initialDisplay(heading, heading2, heading3, heading4):
    print("")
    print(heading3)
    print(heading)
    print(heading2)
    print(heading4)


def userInformation():

    n = int(input("Enter no of the customers "))
    for i in range(n):
        custName.append(input(f"Enter name of the customer {i+1} "))
        custAddress.append(input(f"Enter address of the customer {i+1} "))
        custPhone.append(int(input(f"Enter phone no of customer {i+1} ")))
        custEmail.append(input(f"Enter email of the customer {i+1} "))
        itemNo = int(input(f"Enter no of items of customer {i+1} "))
        for j in range(itemNo):
            totalPrice = 0
            itemPrice = int(input(f"Enter price of the item {j+1} "))
            itemQuantity = int(input(f"Enter quantity of item {j+1} "))
            totalPrice = totalPrice+itemPrice * itemQuantity
            total.append(totalPrice)
            calculation(total)
        print("")


def calculation(total):
    for i in range(len(total)):
        totalPrice = total[i]
        discount = 0
        if totalPrice <= 5000:
            discount = totalPrice * 0.05
        elif totalPrice <= 8000:
            discount = totalPrice * 0.08
        elif totalPrice <= 10000:
            discount = totalPrice * 0.10
        elif totalPrice > 10000:
            discount = totalPrice * 0.15
        netAmount = totalPrice - discount
        netTotal.append(netAmount)
        return netAmount, discount


def displayInformation(custName, custPhone, custAddress, custEmail, netAmount):
    for i in range(len(custName)):

        initialDisplay(heading, heading2, heading3, heading4)
        initialDisplay(heading, heading2, heading3, heading4)
        print(heading)
        print(f"Customer Name : {custName[i]}")
        print(f"Customer Address : {custAddress[i]}")
        print(f"Customer Phone : {custPhone[i]}")
        print(f"Customer Email : {custEmail[i]}")
        print(f"Customer netAmount : {netAmount[i]}")
        print(heading3)


initialDisplay(heading, heading2, heading3, heading4)

userInformation()
displayInformation(custName, custPhone, custAddress,
                   custEmail, netAmount=netTotal)
