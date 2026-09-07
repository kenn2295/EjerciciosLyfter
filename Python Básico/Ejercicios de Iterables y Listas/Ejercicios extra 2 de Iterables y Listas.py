my_list = []
counter = 1

while counter <= 5:
    numbers = int(input(f'Ingrese el numero {counter}: '))
    counter += 1
    my_list.append(numbers)

all_positive = True

for num in my_list:
    if num <= 0:  
        all_positive = False
if all_positive:
    print('Todos son positivos')
                
else:   
    print('Hay al menos un número negativo o cero')