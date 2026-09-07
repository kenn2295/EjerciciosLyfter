counter = 1
my_list = []

while counter <= 10:
    numbers = int(input(f'Ingrese el numero {counter}: '))
    my_list.append(numbers)
    counter += 1
    
counter = 0
wanted_number = int(input('Ingrese su numero a buscar: '))

for num in my_list:
    if wanted_number == num:
        counter += 1
print(f'El número {wanted_number} aparece {counter} veces')