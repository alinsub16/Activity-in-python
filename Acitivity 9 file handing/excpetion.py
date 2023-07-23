
def inputs(type):
    while True:
        try:
            no = input(type)
            if int(no) >= 0:
                break
            else:
                raise ValueError
        except ValueError:
            print('Invalid input')
    return no


def inputs2(type):
    while True:
        try:
            words = str(input(type))
            if words.isalpha():
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid input!!!!")
    return words

def inputs3(type):
    while True:
        try:
            words = str(input(type))
            if str(words):
                break
            elif int(words) >= 0:
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid input!!!!")
    return words
def inputs4(type):
    while True:
        try:
            words = int(input(type))
            if words > 0:
                break

            f = open("Reservation.text", "r")
            f.read()

        except ValueError:
            print("Invalid input!!!!")
    return words