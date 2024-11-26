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

if __name__ == '__main__':
    from random import randint

    NAME = (''.join(chr(randint(97, 122)) for i in range(randint(1,10)))
            .capitalize())
    NUMBERS_OF_FLOORS = randint(1, 15)

    house = House(NAME, NUMBERS_OF_FLOORS)
    print(house)
    print(len(house))
