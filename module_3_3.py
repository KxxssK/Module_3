def print_pfrfms(a = 1, b = 'Строка', c = True):
    print(a, b, c)

print_pfrfms()
print_pfrfms(b = 24)
print_pfrfms(c = [1, 2, 3])


value_list = [3, 'Строка_2', False]
values_dict = { 'a': 54, 'b': [156, 56, 98], 'c': 'String'}
print(*value_list)
print_pfrfms(**values_dict)

value_list_2 = ['Text', 34.3434]
print_pfrfms(*value_list_2, 42)






