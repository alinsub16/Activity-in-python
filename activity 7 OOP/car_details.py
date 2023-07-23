class Car:
    # creating private variables
    __color = None
    __model = None
    __Manufacturer = None

    def __init__(self, color, model, Manufacturer):
        self.__color = color
        self.__model = model
        self.__Manufacturer = Manufacturer

    def __display_details(self):
        print('''*************
Car Details:
Car Color: {}
Car Model: {}
Car Manufacturer: {}
*************'''.format(
            self.__color,
            self.__model,
            self.__Manufacturer
        ))

    def update_color(self, value):
        self.__color = value

    def update_model(self, value):
        self.__model = value

    def update_Manufacturer(self, value):
        self.__Manufacturer = value

    def access_details(self):
        self.__display_details()
