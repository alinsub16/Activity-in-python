def average(x):
    global grade

    if x >= 75:
        grade = "Passed"
    else:
        grade = " Failed"

Name = str(input("Enter Name: "))
Math = float(input("Enter your math grade: "))
Science = float(input("Enter your Science grade: "))
English = float(input("Enter your English grade: "))

print("Name: " + Name)
print("Math grade " + str(Math))
print("Science grade " + str(Science))
print("English grade " + str(English))


finalAverage = (Math + Science + English)/3

average(finalAverage)
print("Average is; " + str(finalAverage))
print("your grade has; "+grade)
