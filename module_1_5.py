immutable_var = (None, True, 'hello', {'key': 'value'})
print('Tuple: ', immutable_var)

try:
    print('Попробуем поменять первый элемент на 1')
    immutable_var[0] = 1
    print('Мы гении Питона! У нас получилось изменить кортеж!')
    print('Tuple: ', immutable_var)
except TypeError:
    print('Ошибка! Кортеж неизменяемый тип данных!\n')

mutable_var = list(immutable_var)
print('List: ', mutable_var)

try:
    print('Попробуем поменять первый элемент на 1')
    mutable_var[0] = 1
    print('У нас получилось изменить список')
    print('List: ', mutable_var)
except TypeError:
    print('Мы такие непутевые, что нам даже не удалось изменить список')
