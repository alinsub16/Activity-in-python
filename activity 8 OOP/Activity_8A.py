
import student

def main():
    print("Activity 8A")
    while True:
        try:
            Name = str(input("Enter name of Student: "))
            if Name.isspace() or not Name:
                raise ValueError
            if not Name.isalpha():
                raise ValueError
        except ValueError:
            print("Invalid!!")
        else:
            while True:
                try:
                    math = int(input("Enter math grade: "))
                    if math < 0 or math > 100:
                        raise ValueError
                except ValueError:
                    print("Invalid!!!")
                else:
                    while True:
                        try:
                            science = int(input("Enter science grade: "))
                            if science < 0 or science > 100:
                                raise ValueError
                        except ValueError:
                            print("Invalid")
                        else:
                            while True:
                                try:
                                    english = int(input("Enter english grade: "))
                                    if english < 0 or english > 100:
                                        raise ValueError
                                    student1 = student.student(Name, math, science, english)
                                    student1.acces()
                                except ValueError:
                                    print("Invalid!!!")
                                else:
                                    while True:
                                        print()
                                        print("A. Try Again?")
                                        print("B. To Exit")

                                        print()
                                        response = input("Please Select: ")
                                        if response in ("A", "a", "B", "b"):
                                            break
                                        print()
                                        print("Please Enter A or B ")
                                    if response == "A" or response == "a":
                                        main()
                                    elif response == "B" or response == "b":
                                        exit()


main()