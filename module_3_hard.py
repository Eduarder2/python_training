"""
Будем решать задачу в предположении, что в качестве входных данных
используется объект одного из следующих типов данных - int, float, str,
list, dict, set, frozenset, tuple, bool - а также их вложения друг в
друга любой глубины. Конечным элементом такого погружения может быть объект
одного из следующих типов данных - int, float, bool (1 или 0), str.
"""

'''
0. заводим счетчик "длины"
1. получаем объект
2. определяем его тип
3. 3.1.1 если объект - коллекция, то переходим на следующий уровень погружения
   3.1.2 запоминаем "адрес" это коллекции и переходим к п.2
   3.2. иначе берем его длину (str) или числовое значение (int, bool, float)
4. добавляем значение "длины" к счетчик и переходим к п.2
'''

def main():
    data_structure = [1, 2, True, '3', None, {'key':10, (1,2):'kk'}]

    def sum_object(object_, count=0):
        object_type = type(object_)
        if object_type in (list, set, frozenset, tuple):
            for instance in object_:
                count += sum_object(instance)
            return count
        elif object_type is dict:
            return sum_object(list(object_.items()))
        elif object_type in (float, int, bool):
            return object_
        elif object_type is str:
            return len(object_)
        else:
            print(f'Incorrect input {object_}-{object_type} is defined as 0')
            return 0

    print(sum_object(data_structure))

if __name__ == '__main__':
    main()