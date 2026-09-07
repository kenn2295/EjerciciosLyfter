my_list = []
while True:   
    number = input('Ingrese un numero (o ENTER/stop para salir): ').lower() 
    if number == '' or number == 'stop':
        break
    my_list.append(int(number))
total = sum(my_list)
average = total / len(my_list)
new_list = []
for num in my_list:
    if num > average:
        new_list.append(num)
print(f'Promedio: {average}')
print(f'Nueva Lista: {new_list}')
