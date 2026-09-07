my_dictionary = {}

amount = int(input('Cuantos datos va a ingresar?: '))
for i in range(amount):
    key = input('key: ')
    value = input('value: ')
    
    my_dictionary[key] = value

print('\nDICCIONARIO:')
for key, value in my_dictionary.items():
    
    print(key, value)

deleted_keys = input('\nIngrese las Keys que desea eliminar: ').split(',')

for key in deleted_keys:
    key = key.strip()
    if key in my_dictionary:
        deleted_item = my_dictionary.pop(key)
        print(f'Deleted item: {deleted_item}')
    else:
        print(f'\nLa key "{key}" no existe')
print('\nDICCIONARIO ACTUALIZADO:')
print(my_dictionary)
#sino tambien para ordearlo mejor con key, value
#for key, value in my_dictionary.items():
#    print(key, value)