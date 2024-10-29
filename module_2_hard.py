import random

random.seed()
first_number = random.randint(3, 20)

def get_slice_of_second_number(number):
    slice_of_second_number = list()
    for i in range(1, number // 2 + (number % 2)):
        # Последнее слагаемое добавлено, что бы в ответе не было пар типа n n,
        # как для числа 8 = 4 + 4
        slice_of_second_number += [i, number - i]
    return slice_of_second_number


def get_second_number(first_number):
    second_number = list()
    divisors = [first_number]
    for i in range(2, int(first_number ** 0.5) + 1):
        if not first_number % i:
            divisors += list({i, first_number // i})
    divisors.sort()
    for divisor in divisors:
        second_number += get_slice_of_second_number(divisor)
    return ''.join([str(i) for i in second_number])

print(f'Число на первой дощечке {first_number}, поэтому число на второй - '
      f'{get_second_number(first_number)}.')