class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for current_floor in range(1, new_floor + 1):
                print(current_floor)
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, '
                f'количество этажей: {self.number_of_floors}')

    def __eq__(self, other):
        try:
            return self.number_of_floors == other.number_of_floors
        except AttributeError:
            pass

    def __lt__(self, other):
        try:
            return self.number_of_floors < other.number_of_floors
        except AttributeError:
            pass

    def __le__(self, other):
        try:
            return self.number_of_floors <= other.number_of_floors
        except AttributeError:
            pass

    def __gt__(self, other):
        try:
            return self.number_of_floors > other.number_of_floors
        except AttributeError:
            pass

    def __ge__(self, other):
        try:
            return self.number_of_floors >= other.number_of_floors
        except AttributeError:
            pass

    def __ne__(self, other):
        try:
            return self.number_of_floors != other.number_of_floors
        except AttributeError:
            pass

    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
            return self
        else:
            print('Невозможно изменить число этажей на указанную величину')
            return self

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self + other

if __name__ == '__main__':
    from random import randint

    NAME = (''.join(chr(randint(97, 122)) for i in range(randint(1,10)))
            .capitalize())
    NUMBERS_OF_FLOORS = randint(1, 15)
    house1 = House(NAME, NUMBERS_OF_FLOORS)
    print(house1)
    print(len(house1))

    NAME = (''.join(chr(randint(97, 122)) for i in range(randint(1, 10)))
            .capitalize())
    NUMBERS_OF_FLOORS = randint(1, 15)
    house2 = House(NAME, NUMBERS_OF_FLOORS)
    print(house2)
    print(len(house2))

    house1 = house1 + 5
    print(house1)
    house1 += 5
    print(house1)
    house2 = 10 + house2
    print(house2)

    print(house1 == house2)
    print(house1 > house2)
    print(house1 >= house2)
    print(house1 < house2)
    print(house1 <= house2)
    print(house1 != house2)