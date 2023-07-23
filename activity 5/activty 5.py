import math
import random
import string
import cmath


def login_security():
    while True:
        try:
            login_name = input("ENTER USER NAME: ")
            password = input("ENTER PASSWORD: ")

            if login_name == "alinsub" and password == "0123":
                menu()
                break
            elif login_name != "alinsub" and password == "0123":
                print("The USER NAME is wrong!!")
                login_security()
                break
            elif login_name == "alinsub" and password != "0123":
                print("The PASSWORD is wrong!!")
                login_security()
                break
            elif login_name != "alinsub" and password != "0123":
                print("The USER NAME and PASSWORD is wrong or not filled up!!")
                login_security()
                break
        except ValueError:
            print("Invalid input. ")


def menu():
    print("=====MAIN MENU=====")

    print("A. ROCK-PAPER SCISSOR GAME")
    print("B. AVERAGE HEIGHT CALCULATOR")
    print("C. PASSWORD GENERATOR")
    print("D. RECORD KEEPING APPLICATION")
    print("E. FACTORIAL")
    print("F. ODD/EVEN")
    print("G. QUADRATIC EQUATION SOLVER")
    print("H. SIMPLE  CALCULATOR")
    print("I. SIMPLE SALARY CALCULATOR")
    print("J. NUMBER SYSTEM CONVERSION")
    print()

    while True:
        try:
            choose = input("Choose operation:")
            if choose in ("A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j"):
                break
            print("Choose number from the operation MENU A to B only!!!")
        except ValueError:
            print("")
    if choose == "A" or choose == "a":
        ROCK_PAPER_SCISSOR_GAME()
    elif choose == "B" or choose == "b":
        AVERAGE_HEIGHT_CALCULATOR()
    elif choose == "C" or choose == "c":
        PASSWORD_GENERATOR()
    elif choose == "D" or choose == "d":
        RECORD_KEEPING_APPLICATION()
    elif choose == "E" or choose == "e":
        FACTORIAL()
    elif choose == "F" or choose == "f":
        ODD_EVEN()
    elif choose == "G" or choose == "g":
        QUADRATIC_EQUATION_SOLVER()
    elif choose == "H" or choose == "h":
        SIMPLE_CALCULATOR()
    elif choose == "I" or choose == "i":
        SIMPLE_SALARY_CALCULATOR()
    elif choose == "J" or choose == "j":
        NUMBER_SYSTEM_CONVERSION()
    else:
        exit()


def checkOutput(choice, computer):
    if choice == computer:
        print("It's a tie!")
    elif choice == "Rock":
        if computer == "Paper":
            print("You Lose!")
        elif computer == "Scissor":
            print("You Win!")
    elif choice == "Paper":
        if computer == "Rock":
            print("You Win!")
        elif computer == "Scissor":
            print("You Lose!")
    elif choice == "Scissor":
        if computer == "Paper":
            print("You Win!")
        elif computer == "Rock":
            print("You Lose!")


def ROCK_PAPER_SCISSOR_GAME():
    while True:
        try:
            list = ["Rock", "Paper", "Scissor"]
            user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
            if user >= 3:
                raise ValueError
            if user < 0:
                raise ValueError

            computer = random.choice(list)
            if user == 0:
                choice = "Rock"
                print("You choose: %s" % choice)
                print("Computer chose: %s" % computer)
                checkOutput(choice, computer)
            elif user == 1:
                choice = "Paper"
                print("You choose: %s" % choice)
                print("Computer chose: %s" % computer)
                checkOutput(choice, computer)
            elif user == 2:
                choice = "Scissor"
                print("You choose: %s" % choice)
                print("Computer chose: %s" % computer)
                checkOutput(choice, computer)
        except ValueError:
            print("Invalid Input!!!")
        else:
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
                ROCK_PAPER_SCISSOR_GAME()
            elif response == "B" or response == "b":
                menu()
            else:
                exit()


def AVERAGE_HEIGHT_CALCULATOR():
    while True:
        try:
            height = input("Input a list of student heights: ").split()
            for i in height:
                if int(i) <= 0:
                    raise ValueError
            num = [int(i) for i in height]
            print(num)

            total = sum(num)
            avg = total / len(num)
            print("%d is the total student heights" % total)
            print("%d is the total number of students" % len(num))
            print("%d is the average height" % avg)
        except ValueError:
            print("Invalid Input!!!")
        else:
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
                AVERAGE_HEIGHT_CALCULATOR()
            elif response == "B" or response == "b":
                menu()
            else:
                exit()


def PASSWORD_GENERATOR():
    while True:
        try:
            passlength = int(input("Enter password length: "))
            if passlength < 0:
                raise ValueError
        except ValueError:
            print("Invalid input!!!")
        else:

            while True:
                try:
                    alphapass = int(input("Enter alphabet count in password: "))
                    if alphapass < 0:
                        raise ValueError
                except ValueError:
                    print("Invalid input!!!")
                else:
                    while True:
                        try:
                            specialpass = int(input("Enter special characters count in password: "))
                            if specialpass < 0:
                                raise ValueError
                            if alphapass + specialpass <= passlength:
                                letter = []
                                for i in range(0, alphapass):
                                    letter.append(random.choice(string.ascii_letters))
                                special = []
                                for i in range(0, specialpass):
                                    special.append(random.choice(string.punctuation))
                                digit = []
                                digit.append(random.choice(string.digits))
                                password_requirements = letter + special
                                pass0 = alphapass + specialpass
                                passl = passlength - pass0
                                passw = []
                                for i in range(0, passl):
                                    passw.append(random.choice(string.digits))
                                for char in password_requirements:
                                    passw.append(char)
                                random.shuffle(passw)
                                passd = "".join(passw)
                                print(passd)

                            elif alphapass + specialpass > passlength:
                                print("Characters total count is greater than the password length")
                        except ValueError:
                            print("Invalid input!!!")
                        else:
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
                                PASSWORD_GENERATOR()
                            elif response == "B" or response == "b":
                                menu()
                            else:
                                exit()


def RECORD_KEEPING_APPLICATION():
    dict1 = {}
    print("A. Add Data")
    print("B. Delete Data")
    print("C. End")
    user = str(input("Please Select: "))
    while True:
        if user.upper() == "A":
            userKey = input("Enter Key: ")
            if userKey in dict1:
                print("Key Already Exist")
            else:
                userValue = input("Enter Value: ")
                dict1[userKey] = userValue
                print(dict1)
        elif user.upper() == "B":
            if dict1:
                delKey = input("Enter Key: ")
                if delKey in dict1:
                    dict1.pop(delKey)
                    print(dict1)
                else:
                    print("Key Does Not Exist")
            else:
                print("No Records Available")
        elif user.upper() == "C":
            print()
            print()
            print("THANK YOU")
            print()
            print()
            menu()

        print("A. Add Data")
        print("B. Delete Data")
        print("C. End")
        user = str(input("Please Select: "))


def FACTORIAL():
    global factorial
    while True:
        try:
            num = int(input("Enter a number: "))
            if num < 0:
                raise ValueError
            if num == 0:
                print("The factorial of 0 is 1")
            else:
                for i in range(1, num):
                    factorial = math.factorial(num)
                print("The factorial of %s is %s" % (num, factorial))
        except ValueError:
            print("Invalid Input!!!")
        else:
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
                FACTORIAL()
            elif response == "B" or response == "b":
                menu()
            else:
                exit()


def ODD_EVEN():
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
        ODD_EVEN()
    elif response == "B" or response == "b":
        menu()
    else:
        exit()


def QUADRATIC_EQUATION_SOLVER():
    while True:
        try:
            a = int(input("Enter a: "))
            if a == 0 and a < 1:
                raise ZeroDivisionError
        except ZeroDivisionError:
            print("a is != zero")
        except ValueError:
            print("Invalid Input!!!")
        else:
            while True:
                try:
                    b = int(input("Enter b: "))
                except ValueError:
                    print("Invalid input!!!")
                else:
                    while True:
                        try:
                            c = int(input("Enter c: "))
                            d = (b ** 2) - (4 * a * c)
                            sol1 = (-b - cmath.sqrt(d)) / (2 * a)
                            sol2 = (-b + cmath.sqrt(d)) / (2 * a)
                            print(f"the solution are{sol1} and {sol2}")
                        except ValueError:
                            print("Invalid Input!!!")
                        else:
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
                                QUADRATIC_EQUATION_SOLVER()
                            elif response == "B" or response == "b":
                                menu()
                            else:
                                exit()



def SIMPLE_CALCULATOR():
    print("\t\t\t\t\t===SIMPLE CALCULATOR===")
    while True:
        try:
            print("\t\t\t\t\t=======MENU==========")
            print()
            print("1. Multiplication \t2. Division \t 3. Addition \t4. Subtraction ")
            print()

            while True:
                choose = int(input("Choose operation:"))
                if choose in (1, 2, 3, 4):
                    break
                print("\nChoose number from the operation MENU 1 to 4 only!!!\n")
            if choose == 1:
                while True:
                    try:
                        num_1 = int(input("First number: "))
                        break
                    except ValueError:
                        print("Invalid Input!!!")
                while True:
                    try:
                        num_2 = int(input("Second number: "))
                        break
                    except ValueError:
                        print("Invalid Input!!!")
                product = int(num_1) * int(num_2)
                prod = "The product of {} and {} is {}"
                prod2 = prod.format(num_1, num_2, product)
                print(prod2)
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
                    SIMPLE_CALCULATOR()
                elif response == "B" or response == "b":
                    menu()
                else:
                    exit()
            if choose == 2:
                while True:
                    try:
                        num_1 = int(input("First number: "))
                        break
                    except ValueError:
                        print("Invalid Input!!!")

                while True:
                    try:
                        num_2 = int(input("Second number: "))
                        if num_2 == 0:
                            raise ZeroDivisionError
                        break
                    except ValueError:
                        print("Invalid Input")
                    except ZeroDivisionError:
                        print("Invalid Input!!!\t THE DIVISOR CANNOT BE EQUAL TO ZERO")
                quot = int(num_1) / int(num_2)
                q = "The quotient of {} and {} is {}"
                q2 = q.format(num_1, num_2, quot)
                print(q2)
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
                    SIMPLE_CALCULATOR()
                elif response == "B" or response == "b":
                    menu()
                else:
                    exit()
            if choose == 3:
                while True:
                    try:
                        num_1 = int(input("First number: "))
                        break
                    except ValueError:
                        print("Invalid Input!!!")

                while True:
                    try:
                        num_2 = int(input("Second number: "))
                        break
                    except ValueError:
                        print("Invalid Input!!!")
                sum = int(num_1) + int(num_2)
                sum1 = "The sum of {} and {} is {}"
                sum2 = sum1.format(num_1, num_2, sum)
                print(sum2)
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
                    SIMPLE_CALCULATOR()
                elif response == "B" or response == "b":
                    menu()
                else:
                    exit()
            if choose == 4:
                while True:
                    try:
                        num_1 = int(input("First number: "))
                        break
                    except ValueError:
                        print("Invalid Input!!!")
                while True:
                    try:
                        num_2 = int(input("Second number: "))
                        break
                    except ValueError:
                        print("Invalid Input!!!")
                difference = int(num_1) - int(num_2)
                dif = "The difference of {} and {} is {}"
                dif1 = dif.format(num_1, num_2, difference)
                print(dif1)
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
                    SIMPLE_CALCULATOR()
                elif response == "B" or response == "b":
                    menu()
                else:
                    exit()

        except ValueError:
            print("Invalid")


def SIMPLE_SALARY_CALCULATOR():
    RatePerHour = 100
    while True:

        try:
            EmployeeName = str(input("Employee Name:")).split()

            break
        except ValueError:
            print("Use String Only!!")
    while True:
        try:
            NumberOfHours = int(input("Enter number of Hours:"))
            if NumberOfHours < 0:
                raise ValueError

            break
        except ValueError:
            print("Invalid Input!!")

    while True:
        try:
            SssContribution = int(input("SSS Contribution:"))
            if SssContribution < 0:
                raise ValueError
            break
        except ValueError:
            print(" Invalid Input!!")

    while True:
        try:
            PhilHealth = int(input("Phil Health:"))
            if PhilHealth < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid Input!!")

    while True:
        try:
            HousingLoan = int(input("Housing Loan:"))
            if HousingLoan < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid Input!!")

    GrossSalary = NumberOfHours * RatePerHour
    Tax = GrossSalary * 0.1
    TotalDeduction = SssContribution + PhilHealth + HousingLoan + Tax
    NetSalary = GrossSalary - TotalDeduction
    print("""
    ==============PAYSLIP==============
    ========EMPLOYEE INFORMATION=======""")
    print("Employee Name:" + str(EmployeeName))
    print("Rendered Hours:" + str(NumberOfHours))
    print("Rate per Hour:" + str(RatePerHour))
    print("Gross Salary:" + str(GrossSalary))
    print("=============DEDUCTION=============")
    print("SSS:" + str(SssContribution))
    print("PhilHealth:" + str(PhilHealth))
    print("Other Loans:" + str(HousingLoan))
    print("Tax: %.1f" % Tax)
    print("Total Deductions: %.1f" % TotalDeduction)
    print("Net Salary: PHP %.1f" % NetSalary)
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
        SIMPLE_SALARY_CALCULATOR()
    elif response == "B" or response == "b":
        menu()
    else:
        exit()


def NUMBER_SYSTEM_CONVERSION():
    print("\t\tMENU")

    print("1. Binary to other number conversion")
    print("2. Octal to other number conversion")
    print("3. decimal other number conversion")
    print("4. hex to other number conversion")
    print("0. to back main menu")
    print()
    print()
    while True:
        try:
            choose = int(input("Please choose 1 to 4 and 0 t0 back to main menu."))
            if choose < 0:
                raise ValueError
            if choose >= 5:
                raise ValueError
            if choose == 1:
                binary_to_other()
            elif choose == 2:
                octal_to_other()
            elif choose == 3:
                decimal_to_other()
            elif choose == 4:
                hex_to_other()
            elif choose == 0:
                menu()

        except ValueError:
            print("Please choose 1 to 4 and 0 t0 back to main menu.")


def binary_to_other():
    while True:
        try:
            binary = input("Enter number in binary format: ")
            decimal = int(binary, 2)
            print(binary, "in Decimal =", decimal)
            print(binary, "in Hexadecimal =", hex(decimal))
            print(binary, "in octal =", oct(decimal))
        except ValueError:
            print("Invalid Input!!!")
        else:
            while True:
                print()
                print("A. Try Again?")
                print("B. Menu?")
                print("X. Exit?")
                print()
                response = input("Please Select: ")
                if response in ("A", "a", "B", "b", "X", "x"):
                    break
                print()
                print("Please Enter A or B and X for exit ")
            if response == "A" or response == "a":
                binary_to_other()
            elif response == "B" or response == "b":
                NUMBER_SYSTEM_CONVERSION()
            else:
                exit()


def octal_to_other():
    while True:
        try:
            octal = input("Enter number in Octal format: ")
            decimal = int(octal, 8)
            print(octal, "in Decimal =", decimal)
            print(octal, "in Hexadecimal =", hex(decimal))
            print(octal, "in Binary =", bin(decimal))
        except ValueError:
            print("Invalid input!!!")
        else:
            while True:
                print()
                print("A. Try Again?")
                print("B. Menu?")
                print("X. Exit?")
                print()
                response = input("Please Select: ")
                if response in ("A", "a", "B", "b", "X", "x"):
                    break
                print()
                print("Please Enter A or B and X for exit ")
            if response == "A" or response == "a":
                octal_to_other()
            elif response == "B" or response == "b":
                NUMBER_SYSTEM_CONVERSION()
            else:
                exit()


def decimal_to_other():
    while True:
        try:
            decimal = int(input("Enter in number decimal format: "))
            print(bin(decimal), "in binary.", oct(decimal))
            print(oct(decimal), "in octal.", hex(decimal))
            print(hex(decimal), "in hexadecimal.",  bin(decimal))
        except ValueError:
            print("Invalid Input!!!")
        else:
            while True:
                print()
                print("A. Try Again?")
                print("B. Menu?")
                print("X. Exit?")
                print()
                response = input("Please Select: ")
                if response in ("A", "a", "B", "b", "X", "x"):
                    break
                print()
                print("Please Enter A or B and X for exit ")
            if response == "A" or response == "a":
                octal_to_other()
            elif response == "B" or response == "b":
                NUMBER_SYSTEM_CONVERSION()
            else:
                exit()


def hex_to_other():
    while True:
        try:
            hex = input("Enter number in hexa-decimal Format: ")
            decimal = int(hex, 16)
            print(hex, "in Decimal =", decimal)
            print(hex, "in octal =", oct(decimal))
            print(hex, "in Binary =", bin(decimal))
        except ValueError:
            print("Invalid Input!!!")
        else:
            while True:
                print()
                print("A. Try Again?")
                print("B. Menu?")
                print("X. Exit?")
                print()
                response = input("Please Select: ")
                if response in ("A", "a", "B", "b", "X", "x"):
                    break
                print()
                print("Please Enter A or B and X for exit ")
            if response == "A" or response == "a":
                octal_to_other()
            elif response == "B" or response == "b":
                NUMBER_SYSTEM_CONVERSION()
            else:
                exit()
login_security()