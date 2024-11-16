from new_math_4_1.fake_math import divide as fake_divide
from new_math_4_1.true_math import divide as true_divide

print('10 / 0')
print(f'take_math module - {fake_divide(10, 0)}\n'
      f'true_math module - {true_divide(10, 0)}')