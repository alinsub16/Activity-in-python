
RatePerHour = 100
while True:

    try:
        EmployeeName = str(input("Employee Name:"))
        if not EmployeeName.isalpha():
            raise ValueError
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
Tax = GrossSalary * 0.01
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



