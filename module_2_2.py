first = input('Your first number: ')
second = input('Your second number: ')
third = input('Your third number: ')

if first == second and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)
'''
# Скорее всего, не так эффективно и по памяти, и по времени

first = int(first)
second = int(second)
third = int(third)
if not (first - second) ** 2 + (second - third) ** 2:
    print(3)
elif not (first - second) * (second - third) * (first - third):
    print(2)
else:
    print(0)
'''