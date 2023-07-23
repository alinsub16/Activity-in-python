def calc():
    print("Simple Calculator")
    print()
    print("Operations: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print()

    while True:
        try:
            operation = int(input("Please enter the number you want to perform: "))
            if operation > 4 or operation < 1:
                raise ValueError
        except ValueError:
            print("Invalid Input")
        else:
            while True:
                try:
                    a = int(input("Enter num1: "))
                    while True:
                        try:
                            b = int(input("Enter num2: "))
                            if operation == 1:
                                res = a + b
                                sum = "The sum of {} and {} is {}"
                                sum2 = sum.format(a,b,res)
                                print(sum2)
                                break
                            elif operation == 2:
                                res = a - b
                                dif = "The difference of {} and {} is {}"
                                dif2 = dif.format(a, b, res)
                                print(dif2)
                                break
                            elif operation == 3:
                                res = a * b
                                product = "The product of {} and {} is {}"
                                product2 = product.format(a, b, res)
                                print(product2)
                                break
                            elif operation == 4:
                                res = a / b
                                q = "The quotient of {} and {} is {}"
                                q2 = q.format(a, b, res)
                                print(q2)
                                break
                            else:
                                print()
                        except (ValueError, ZeroDivisionError):
                            print("Invalid Input")
                except (ValueError, ZeroDivisionError):
                    print("Invalid Input")

                while True:
                    again = input("Do you want to run again?(y/n)\n")
                    if again in ("y", "Y", "n", "N"):
                        break
                    print("Invalid input")
                if again == "Y":
                    calc()
                    continue
                if again == "y":
                    calc()
                    continue
                else:
                    print("Thank You")
                    print("EXIT")
                    exit()
                break
            break
calc()

