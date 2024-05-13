class House:
    def __init__(self):
        self.numberOfFloors = 10

    def floors(self):
        print('Текущий этаж равен - ', self.numberOfFloors)


house = House()
house.floors()
