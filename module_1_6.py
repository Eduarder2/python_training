my_dict = dict(Pushkin=1799, Gogol=1809, Dostoevsky=1821)
print(my_dict)
print(my_dict.get('Pushkin'), my_dict.get('Chekhov'))
my_dict['Tolstoy'] = 1828
my_dict.update({'Turgenev': 1818})
print('Gogol: ', my_dict.pop('Gogol'))
print(my_dict, '\n')

my_set = {1, -2j, 3, 3, 3, 1 + 2j, 0, -2j}
print(my_set)
my_set.update({-1, -4})
my_set.discard(1)
print(my_set)