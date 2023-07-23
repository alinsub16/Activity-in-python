
import house
import Inputs



def main():
    while True:
        try:
            hu = house.House(12, 12)
            print("====================")
            print("Unmodified Properties")
            hu.displayt()
            print("====================")
            townhouse1 = house.TownHouse(Inputs.inputs("Number of Floor : "), Inputs.inputs("Nuber of Doors: "))

            print("======================")
            print("Modified Properties")
            townhouse1.access()
        except ValueError:
            print("invalid")
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
                print("Please Enter A or B")
            if response == "A" or response == "a":
                main()
            elif response == "B" or response == "b":
                exit()
main()





