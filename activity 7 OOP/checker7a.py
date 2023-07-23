
def letter_checker(prompt):
    while True:
        try:
            check = input(prompt)
            if check.isspace() or not check:
                print('Text is empty')
            elif all(character.isalpha() or character.isspace() for character in check):
                return check
            else:
                raise NoNumberError
        except NoNumberError:
            print('No special characters and numbers allowed!\n')


def try_again():
    while True:
        choice = input('\nWould you like to try again? [Y/N]\n===>')
        choice = choice.upper()

        if choice == 'Y':
            print("")
            return True
        elif choice == 'N':
            return False
        else:
            print('Please select valid option!')
