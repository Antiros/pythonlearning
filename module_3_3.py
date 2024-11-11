def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(2)
print_params(4, 'book')
print_params(43, 'AD', False)
print_params(b = 25)              # ругается на число, так как должна быть строка
print_params(c = [1, 2, 3])       # ругается на список, так как должно быть булевое выражение


value_list = [True, 3, 'Arch']
value_dic = {'a': 7, 'b': 'ERROR', 'c': False}
print_params(*value_list)
print_params(**value_dic)


value_list_2 = [1, None]
print_params(*value_list_2, 42)