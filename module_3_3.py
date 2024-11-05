# Пункт 1
def print_params(a=1, b='string', c=True):
    print(f'{a}, {b}, {c}')

try:
    print_params(10, 2, 3, 4)
except TypeError:
    print('Функция принимает не более 3 аргументов, а мы ввели 4')

print_params(10, 2, 3)
print_params(10, 2)
print_params(10)
print_params()

print_params(b = 25)
print_params(c = [1, 2, 3])
print('-' * 20)

# Пункт 2
values_list = [None, 17, 'coast']
values_dict = dict(a=5, b=False, c={1, 2})

print_params(*values_list)
print_params(**values_dict)
print('-' * 20)

# Пункт 3
values_list_2 = [[11, 2], (11, 2)]
print_params(*values_list_2, 42)