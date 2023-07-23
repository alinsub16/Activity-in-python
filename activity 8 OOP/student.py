class student:
    __name = None
    __math = None
    __science = None
    __english = None

    def __init__(self, name, math, science, english):
        self.__name = name
        self.__math = math
        self.__science = science
        self.__english = english

    def Calculation(self):
        total = self.__math+self.__science+self.__english
        average = total/3
        return average

    def identify(variable_1):
        if variable_1.Calculation() < 75:
            return "failed"
        else:
            return "pass"

    def print(self):
        print("_____________________________")
        print("|Name         |", self.__name)
        print("|Math Grade   |", self.__math)
        print("|Science Grade|", self.__science)
        print("|English Grade|", self.__english)
        print("______________________________")
        print("Average       |", self.Calculation(), self.identify())
        print("______________________________")

    def acces(self):
        self.print()
