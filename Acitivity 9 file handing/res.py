
import excpetion


class restaurant:

    def __init__(self, choice):
        self.choice = choice

        # VIEW RESERVATIONS
        if choice.upper() == "A":
            self.view_reservation()
        elif choice.upper() == "B":
            self.make_reservation()
        elif choice.upper() == "C":
            self.delete()
        elif choice.upper() == "D":
            self.generate_report()
        elif choice.upper() == "E":
            import sys
            sys.exit("Thank you & Come again!")

        else:
            print("INVALID!, PLEASE TRY AGAIN!")

    def view_reservation(self):
        count = 0
        print("============================================= VIEW RESERVATION =============================================\n")
        FILE = open("Reservation.text")
        lines = FILE.readlines()
        FILE.close()
        for line in lines:
            count += 1

        if count == 0:
            print("\nNo Reservation!")
        else:
            FILE = open("Reservation.text", "r")
            print(FILE.read())
            FILE.close()
            print("============================================================================================================\n")

    def make_reservation(self):
        with open("Reservation.text", "r") as FILE:
            for last_line in FILE:
                pass
        if last_line[0] == "#":
            num = 1
        else:
            num = int(last_line[0]) + 1
        print("\n============================================== INPUT RESERVATION ==========================================")
        name = excpetion.inputs2("Enter Name: ")
        date = excpetion.inputs3("Enter Date: ")
        time = excpetion.inputs3("Enter Time: ")
        adult = excpetion.inputs("No. of adult: ")
        children = excpetion.inputs("No. of Children: ")
        FILE = open("Reservation.text", "a")
        FILE.write(f"{num: <1}\t\t\t{name: ^15}\t\t\t   {date: ^10}\t\t\t{time: ^10}\t\t\t{adult: ^10}\t\t\t\t\t{children: ^10}\n")
        FILE.close()

    def delete(self):
        reservation_num = excpetion.inputs("Enter Reservation Number: ")
        file1 = open("Reservation.text", "r")
        lines = file1.readlines()
        file1.close()
        file2 = open("Reservation.text", "w")

        for line in lines:
            if not line.startswith(reservation_num):
                file2.write(line)
        file2.close()

    def generate_report(self):
        adults, children, total_adults, total_children, total = 0, 0, 0, 0, 0
        FILE = open('Reservation.text', "r")

        report: str = ""
        i = 0

        for line in FILE:
            i += 1
            if i > 1:
                stripped_line = line.strip()
                line_list = stripped_line.split("\t\t\t")
                adults += int(line_list[4])
                children += int(line_list[5])
                subtotal = (int(line_list[4]) * 500) + (int(line_list[5]) * 300)
                total += subtotal
                line_list.append(str(subtotal))
                report += f"{line_list[0]}\t\t\t{line_list[1]}\t\t{line_list[2]}\t\t{line_list[3]}\t\t{line_list[4]}\t\t{line_list[5]}\t\t\t\t\t{line_list[6]}\t\t\t\n "
        FILE.close()

        print()
        print()
        print("                                                        GENERATE REPORT")
        print("#\t\t\t\tName\t\t\t\tDate\t\t\t Time\t\t\t\tAdults\t\t\t\tChildren(s)\t\t\t\tSubtotal\n")
        print(report, "\n")
        print("Total # of adults: ", adults)
        print("Total # of children: ", children)
        print("Subtotal: PHP ", total)
        print("-----------------------------------------------------------------------------\n")

while True:

    print("\n=====================================")
    print("=== RESTAURANT RESERVATION SYSTEM ===")
    print("=====================================\n")
    print("MENU:\n")
    print("A. VIEW ALL RESERVATION")
    print("B. MAKE RESERVATION")
    print("C. DELETE RESERVATION")
    print("D. GENERATE REPORT")
    print("E. EXIT")

    Selection_menu = input("SELECT: ")
    restaurant(Selection_menu)