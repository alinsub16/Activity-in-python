import SalaryDeduction
import NetSalary
import GrossSalary


def mainsalary():
    
    while True:

        try:
            EmployeeName = str(input("Employee Name:")).strip()

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
            loan = int(input("loan: "))
            if loan < 0:
                raise ValueError
            break
        except ValueError:
            print(" Invalid Input!!")

    while True:
        try:
            health = int(input("Health Insurance: "))
            if health < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid Input!!")

    Tax = "12%"

    print("""
    ==============PAYSLIP==============
    ========EMPLOYEE INFORMATION=======""")
    print("Employee Name:" + str(EmployeeName))
    print("Rendered Hours:" + str(NumberOfHours))
    print("Rate per Hour: 500")
    print("Gross Salary:" + str(GrossSalary.grossSalary(NumberOfHours)))
    print("=============DEDUCTION=============")
    print("Loan:" + str(loan))
    print("Health:" + str(health))

    deduct = float(SalaryDeduction.salarydeduct(loan, health))
    gross = float(GrossSalary.grossSalary(NumberOfHours))
    ttax = 0.12
    net = NetSalary.Net_salary(gross,deduct)
    taxes = float(net*ttax)
    total_dedution = deduct + taxes
    netSalary = gross - total_dedution

    print(f"Tax:{taxes}")
    print(f"Total Deductions: {total_dedution}")
    print("Net Salary: PHP %.1f" % netSalary)

mainsalary()