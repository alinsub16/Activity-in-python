

def login_security():
    while True:
        try:
            login_name = input("ENTER USER NAME: ")
            password = input("ENTER PASSWORD: ")
            
            if login_name == "admin" and password == "12345":
                menu()
                break
            elif login_name != "admin" and password == "12345":
                print("The USER NAME is wrong!!")
                login_security()
                break
            elif login_name == "admin" and password != "12345":
                print("The PASSWORD is wrong!!")
                login_security()
                break
            elif login_name != "admin" and password != "12345":
                print("The USER NAME and PASSWORD is wrong or not filled up!!")
                login_security()
                break
        except ValueError:
            print()


def menu():

    print()
    print("A. ODD/EVEN NUMBER CHECKER")
    print("B. ROLLER COASTER")
    print("C. BODY MASS INDEX (BMI) CALCULATOR")
    print("D. MULTIPLICATION TABLE")
    print("E. EXIT")
    print()
    while True:
        try:
            choose = input("Choose operation:")
            if choose in ("A","a","B","b","C","c","D","d","E","e"):
                break
            print("Choose number from the operation MENU A to B only!!!")
        except ValueError:
            print("")
    if choose == "A" or choose =="a":
        cheker()
    elif choose == "B" or choose =="b":
        roller()
    elif choose == "C" or choose =="c":
        bmicalc()
    elif choose == "D" or choose =="d":
        multiplication()
    else:
        exit()

def cheker():
    while True:
        try:
            print()
            print("ODD/EVEN NUMBER CHECKER")
            print()
            user = int(input("Enter a number: "))
            if user % 2 == 0:
                print(f"The number {user} is Even")
                break
            else:
                print(f"The number {user} is Odd")
                break
        except ValueError:
            print("Invalid Input")
    while True:
        print()
        print("A. Try Again?")
        print("B. Return to Main Menu?")
        print("X. Exit?")
        print()
        response = input("Please Select: ")
        if response in ("A", "a", "B", "b", "X", "x"):
            break
        print()
        print("Please Enter A or B and X for exit ")
    if response == "A" or response == "a":
        cheker()
    elif response == "B" or response == "b":
        menu()
    else:
        exit()




price1 = 0
price2 = 100
price3 = 150
price4 = 250

def totalBill(price):
    while True:
        try:
            quantity = float(input("Quantity: "))
            if quantity < 0:
                raise ValueError
        except ValueError:
            print("Invalid Input")
        else:
            tot = price * quantity
            print()
            print("=====TOTAL BILL=====")
            print("Quantity: %d" % quantity)
            print("Ticket Price: %d" % price)
            print("Total: %d" % tot)
            print()
            break


def roller():
    while True:
        try:
            print()
            print("ROLLER COASTER")
            print()
            user = float(input("Enter Your Height(cm): "))
            if user > 5 and user < 120:
                print("Sorry, you have to grow taller before you can ride")
                print()
                roller()
                break
            while True:
                try:
                    if user < 6:
                        raise ValueError
                except ValueError:
                    print("Invalid Input")
                    break
                while True:
                    try:
                        age = float(input("Enter your Age: "))
                        if age < 0:
                            raise ValueError
                        while True:
                            if age in range(0, 4):
                                print("FREE (Ticket Price)")
                                totalBill(price1)
                                break
                            elif age in range(4, 11):
                                print("100 Php (Ticket Price)")
                                totalBill(price2)
                                break
                            elif age in range(11, 18):
                                print("150 Php (Ticket Price)")
                                totalBill(price3)
                                break
                            elif age >= 18:
                                print("250 Php (Ticket Price)")
                                totalBill(price4)
                                break
                        while True:
                            print()
                            print("A. Try Again?")
                            print("B. Return to Main Menu?")
                            print("X. Exit?")
                            print()
                            response = input("Please Select: ")
                            if response in ("A", "a", "B", "b", "X", "x"):
                                break
                            print()
                            print("Please Enter A or B and X for exit ")
                        if response == "A" or response == "a":
                            roller()
                        elif response == "B" or response == "b":
                            menu()
                        else:
                            exit()

                    except ValueError:
                        print("Invalid Input")
        except ValueError:
            print("Invalid Input")


def bmicalc():
    while True:
        try:
            print()
            print("BODY MASS INDEX (BMI) CALCULATOR")
            print()
            while True:
                try:
                    height = float(input("Enter your Height(cm): "))
                    if height < 1:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid Input!")
            while True:
                try:
                    weight = float(input("Enter your Weight(kg): "))
                    if weight < 1:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid Input!")
            bmi = weight / (height / 100) ** 2
            print("Your BMI is %f" % bmi)
            if bmi <= 18.5:
                print("UNDERWEIGHT")
                break
            elif bmi >= 18.5 and bmi < 25:
                print("NORMAL WEIGHT")
                break
            elif bmi >= 25 and bmi < 30:
                print("SLIGHTLY OVERWEIGHT")
                break
            elif bmi >= 30 and bmi < 35:
                print("SLIGHTLY OVERWEIGHT")
                break
            elif bmi >= 35:
                print("CLINICALLY OBESE")
                break
        except ValueError:
            print("cba")
    while True:
        print()
        print("A. Try Again?")
        print("B. Return to Main Menu?")
        print("X. Exit?")
        print()
        response = input("Please Select: ")
        if response in ("A", "a", "B", "b", "X", "x"):
            break
        print()
        print("Please Enter A or B and X for exit")
    if response == "A" or response == "a":
        bmicalc()
    elif response == "B" or response == "b":
        menu()
    else:
        exit()



def multiplication():
    while True:
        try:
            print()
            print("MULTIPLICATION TABLE")
            print()
            num = int(input("Input a number: "))
            if num < 0:
                raise ValueError
            for i in range(11):
                tot = num * i
                print(f"{num} x {i} = {tot}")
        except ValueError:
            print("Invalid Input")
        while True:
            print()
            print("A. Try Again?")
            print("B. Return to Main Menu?")
            print("X. Exit?")
            print()
            response = input("Please Select: ")
            if response in ("A", "a", "B", "b", "X", "x"):
                break
            print()
            print("Please Enter A or B and X for exit ")
        if response == "A" or response == "a":
            multiplication()
        elif response == "B" or response == "b":
            menu()
        else:
            exit()
login_security()
