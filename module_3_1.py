import random
random.seed()

calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.lower(), string.upper())

def is_contains(string, list_to_search):
    count_calls()
    return string in list_to_search

for i in range(random.randint(1, 10)):
    string = ''.join([chr(random.randint(65, 122))
                      for j in range(random.randint(1, 20))])
    string_info(string)

for i in range(random.randint(1, 10)):
    string = chr(random.randint(65, 122))
    list_to_search = [chr(random.randint(65, 122))
                      for j in range(random.randint(1, 20))]
    is_contains(string, list_to_search)