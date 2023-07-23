class House:

    def __init__(self, floor, door):
        self.noOfFloor = floor
        self.noOFDoor = door

    def floorSize(self):
        size = "Floor Size: 20 x 10"
        return size

    def swicthon(self):
        switch = "Switch On"
        self.lightOpen()
        self.ovenOpen()
        print("Finish")

    def lightOpen(self):
        print("light Open")

    def ovenOpen(self):
        print("Oven Open")

    def displayt(self):
        print(self.floorSize())
        print("Number of Floors:",self.noOfFloor)
        print("No of Door:",self.noOFDoor)
        print(self.swicthon())


class TownHouse(House):
    pass

    def updatefloor(self, value):
        self.noOfFloor = value

    def updatedoor(self, value):
        self.noOFDoor = value

    def access(self):
        self.displayt()


