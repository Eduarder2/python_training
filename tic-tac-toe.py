'''
1) объявить правила
1.1) создать таблицу
1.2) показать таблицу
1.3) проверка корректности хода
2) замена таблицы
3) проверка на победу
4) передача хода
5) объявление победителя
'''

def get_rules():
    print('Рады приветствовать, участников увлекательной игры'
          ' "Крестики-нолики".\nПравила игры следующие - двое участников'
          ' по очереди заполняют пустое поле 3х3 крестиком или ноликом.\n'
          'Тот, кто ходит первым, ставит крестик, вторым - нолик.\n'
          'Игра заканчивается либо если кто-то смог на поле поставить свои '
          'символы три подряд\nпо вертикали, по диагонали или по горизонтали'
          ' (тогда он объявляется победителем)\nлибо когда участники не могут'
          ' сделать ход, а победитель не определился.\nХорошей игры!')

def create_table():
    table = list()
    for i in range(3):
        table.append(['*', '*', '*'])
    return table

def get_turn(turn):
    if turn % 2:
        print('Крестики - ваш ход!')
    else:
        print('Нолики - ваш ход!')

def get_sign():
    row = int(input('Выберете строку для вашего знака: ')) - 1
    column = int(input('Выберете столбец для вашего знака: ')) - 1
    return row, column

def change_table(turn, table):
    sign = get_sign()
    if is_corrected(table, *sign):
        table[sign[0]][sign[1]] = 'X' if turn % 2 else 'O'
        return table, sign
    else:
        print('Это поле уже занято, выберете свободное!')
        return change_table(turn, table)


def get_table(table):
    for i in range(3):
        print(table[i])

def is_corrected(table, row, column):
    return True if table[row][column] == '*' else False

def is_won(turn, table, row, column):
    if turn == 10:
        return True
    elif turn == 1:
        return False
    elif (table[row-2][column] == table[row-1][column]
          and table[row-1][column] == table[row][column]):
        return True
    elif (table[row][column-2] == table[row][column-1]
          and table[row][column-1] == table[row][column]):
        return True
    elif table[1][1] != '*':
        if table[0][0] == table[1][1] and table[1][1] == table[2][2]:
            return True
        elif table[0][2] == table[1][1] and table[1][1] == table[2][0]:
            return True

def game_over(turn):
    if turn == 10:
        print('Ничья')
    elif turn % 2:
        print('Победа ноликов')
    else:
        print('Победа крестиков')

turn = 1
table = create_table()
sign = (0, 0)

while not is_won(turn, table, *sign):
    get_table(table)
    get_turn(turn)
    table, sign = change_table(turn, table)
    turn += 1

get_table(table)
game_over(turn)
