class InsufficientMobileNumber(Exception):
    """Raised when mobile number count is below 11"""
    pass


class ExcessMobileNumber(Exception):
    """Raised when mobile number count exceeds 11"""
    pass


class NoNumberError(Exception):
    """Raised when user inputs number in a string"""
    pass


# def int_check(prompt):
#     while True:
#         try:
#             check = int(input(prompt))
#             if check.len() > 11:
#                 raise InsufficientMobileNumber
#             elif check > 11:
#                 raise ExcessMobileNumber
#             else:
#                 return check
#
#         except ValueError:
#             print('Please enter numbers only!')
#
#         except InsufficientMobileNumber:
#             print('Grade too low! Please input between 50 - 100')
#
#         except ExcessMobileNumber:
#             print('Input exceeds the grading criteria. Please input between 50 - 100')

def num_checker(prompt):
    while True:
        try:
            check = input(prompt)
            if int(check):
                return check
        except ValueError:
            print("Please enter a number!")


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
