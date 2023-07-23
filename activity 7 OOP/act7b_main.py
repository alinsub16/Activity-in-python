import employee_data

def main():
    while True:
        try:
            employee1_name = str(input('Please enter employee 1 name: '))
            if employee1_name.isspace() or not employee1_name:
                raise ValueError
            if not employee1_name.isalpha():
                raise ValueError
            employee1_email = input('Please enter your email: ')
            if employee1_email.isspace() or not employee1_email:
                raise ValueError
            employee1_cp = input('Please input mobile number: ')
            if employee1_cp.isspace() or not employee1_cp:
                raise ValueError
            if not employee1_cp.isdigit():
                raise ValueError
            employee1 = employee_data.Employee(employee1_name, employee1_email, employee1_cp)
        except ValueError:
            print("Invalid!!!")
        else:
            while True:
                try:
                    employee2_name = str(input('Please enter employee 2 name: '))
                    if employee2_name.isspace() or not employee2_name:
                        raise ValueError
                    if not employee2_name.isalpha():
                        raise ValueError
                    employee2_email = input('Please enter your email address: ')
                    if employee2_email.isspace() or not employee2_email:
                        raise ValueError
                    employee2_cp = input('Please enter your mobile number: ')
                    if employee2_cp.isspace() or not employee2_cp:
                        raise ValueError
                    if not employee2_cp.isdigit():
                        raise ValueError
                    employee2 = employee_data.Employee(employee2_name, employee2_email, employee2_cp)

                    # printing the two employee
                    # printing data for employee 1
                    print('\nEmployee 1 Details')
                    employee1.access_details()
                    # printing data for employee 2
                    print('\nEmployee 2 details')
                    employee2.access_details()

                except ValueError:
                    print("Invalid!!!")
                else:
                    while True:
                        print()
                        print("A. Try Again?")
                        print("B. To Exit")
                        print()
                        response = input("Please Select: ")
                        if response in ("A", "a", "B", "b",):
                            break
                        print()
                        print("Please Enter A or B  ")
                    if response == "A" or response == "a":
                        main()
                    elif response == "B" or response == "b":
                        exit()

main()