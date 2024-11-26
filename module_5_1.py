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

if __name__ == '__main__':
    from random import randint

    NAME = (''.join(chr(randint(97, 122)) for i in range(randint(1,10)))
            .capitalize())
    NUMBERS_OF_FLOORS = randint(1, 15)
    NEW_FLOOR = randint(-10, 20)

    print(f'Name: {NAME} - Numbers_of_floors: {NUMBERS_OF_FLOORS} - '
          f'New_floor: {NEW_FLOOR}')

    house = House(NAME, NUMBERS_OF_FLOORS)
    house.go_to(NEW_FLOOR)