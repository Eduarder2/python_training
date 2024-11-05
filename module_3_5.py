def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    other = str_number[1:]
    other = int(other) if other != '' else 0
    if other:
        return first * get_multiplied_digits(other)
    else:
        return first

print(get_multiplied_digits(int(input())))