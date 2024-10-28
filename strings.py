import random

random.seed()
length_example = random.randint(1, 20)

example = ''
for letter in range(length_example):
    example += chr(random.randint(33, 122))
print('This is your string: ', example)

print(example[0])
print(example[-1])
print(example[(length_example // 2):])
print(example[::-1])
print(example[1::2])