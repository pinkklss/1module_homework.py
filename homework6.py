my_dict = {'Evgeniy': 2004, 'Konstantin': 2001, 'Vladislav': 2003}
print(my_dict)
print(my_dict['Evgeniy'])
my_dict['Matvey'] = 2002
print(my_dict['Matvey'])
my_dict.update({'Danila': 2002,
                'Egor': 2001})
a = my_dict.pop('Vladislav')
print(a)
print(my_dict)
