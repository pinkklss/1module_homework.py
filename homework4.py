my_string = (input())
print(len(my_string))
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(' ', ''))
print(my_string[0])
print(my_string[-1])

immutamle_var = 1, 1.5, 'number'
print(immutamle_var)
immutamle_var[0]=200 #Кортеж не поддерживает изменение в его элементах

mutable_list = ([2, 1.5, 'number'], 0)
print(mutable_list)
mutable_list[0][0] = 3
print(mutable_list)