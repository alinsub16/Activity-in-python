import car_details


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

def main():
    looper = True
    while looper is True:
        print('**********************')
        print('Car Original Data')
        # instantiate the object
        car1 = car_details.Car('Blue', "Toyota Yaris", 'Toyota')
        car2 = car_details.Car('Black', "Tucson", 'Hyundai')
        car3 = car_details.Car('Gray', 'Volkswagen Atlas', 'Volkswagen')

        # print unmodified details
        print('Unmodified Details from Car 1 to Car 3')
        car1.access_details()
        car2.access_details()
        car3.access_details()

        print('***********************')
        print('Car Modified Data 1')
        car_color = input('Please enter modified color of car 1: ')
        car_model = input('Please enter the model of the car: ')
        car_manufacturer = input('Please enter the manufacturer of the car: ')

        # modify variables
        car1.update_color(car_color)
        car1.update_model(car_model)
        car1.update_Manufacturer(car_manufacturer)

        print('***********************')
        print('Car Modified Data 2')
        car_color = input('Please enter modified color of car 2: ')
        car_model = input('Please enter the model of the car: ')
        car_manufacturer = input('Please enter the manufacturer of the car: ' )

        # modify variables
        car2.update_color(car_color)
        car2.update_model(car_model)
        car2.update_Manufacturer(car_manufacturer)

        print('***********************')
        print('Car Modified Data 3')
        car_color = input('Please enter modified color of car 3: ')
        car_model = input('Please enter the model of the car: ')
        car_manufacturer = input('Please enter the manufacturer of the car: ')

        # modify variables
        car3.update_color(car_color)
        car3.update_model(car_model)
        car3.update_Manufacturer(car_manufacturer)

        # print modified details
        print ( 'Modified Details from Car 1 to Car 3' )
        car1.access_details ()
        car2.access_details ()
        car3.access_details ()


        try_again()


    # car2.update_color(ch.letter_checker('Enter chuchu'))
    # car2.update_model('Kia Rio')
    # car2.update_Manufacturer('Kia')
    #
    # car3.update_color('Yellow')
    # car3.update_model('Ford Mustang')
    # car3.update_Manufacturer('Ford')

    # printing modified variables
    # print('\nModified Attributes')
    # car1.access_details()
    # car2.access_details()
    # car3.access_details()


if __name__ == '__main__':
    main()
