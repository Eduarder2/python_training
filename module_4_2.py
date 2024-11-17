def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

try:
    inner_function()
except NameError:
    vars_ = [var for var in list(globals().keys())
             if not var.startswith('__')]
    print('Глобальные переменные ...', *vars_, '\ninner_function среди нет.')