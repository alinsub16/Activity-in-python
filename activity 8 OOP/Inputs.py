

def inputs(type):
    while True:
        try:
            no = int(input(type))
            if no > 0:
                break
            else:
                raise ValueError
        except ValueError:
            print('Invalid input')
    return no