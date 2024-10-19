# Словарь
# 1
my_dict = {'Роман' : 1999,
           'Иван' : 2003,
           'Олег' : 1973,
           'Елена' : 1978,
           'Александр' : 2012
           }
# 2
print(my_dict['Олег'])
# 3
print(my_dict.get('Егор'))
# 4
my_dict.update({'Анастасия': 1952, 'Кристина': 2015})
# 5
name = my_dict.pop('Роман')
print(name)
print(my_dict)

# Множества
# 1
my_set = {'ANT', 1, 2, 3, True, 'ANT', 1, 2, 3, False}
print(my_set)
# 2
my_set.add('False')
my_set.add((5, 9.4, 'str'))
# 3
my_set.discard(False)
print(my_set)