class Employee:

    __employee_name = None
    __email = None
    __mobile_number = None

    def __init__(self, name, email, mobile):
        self.__employee_name = name
        self.__email = email
        self.__mobile_number = mobile

    # private function
    def __display_details(self):
        print('''
-----------------Employee Information----------------
Name: {}
Email: {}
Mobile Number: {}
-----------------------------------------------------'''.format(
            self.__employee_name,
            self.__email,
            self.__mobile_number
        ))

    # creating public functions
    def access_details(self):
        self.__display_details()

    def update_name(self, value):
        self.__employee_name = value

    def update_email(self, value):
        self.__email = value

    def update_mobile(self, value):
        self.__mobile_number = value