def average(x):
    global grade

    if x >= 75:
        grade = "Passed"
    else:
        grade = " Failed"

Name = "Christopher ALinsub"
Math = 75.5
Science = 75.4
English = 75.3

print("Name: " + Name)
print("Math grade " + str(Math))
print("Science grade " + str(Science))
print("English grade " + str(English))


finalAverage = (Math + Science + English)/3

average(finalAverage)
print("Average is; " + str(finalAverage))
print("your grade has; "+grade)

