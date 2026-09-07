my_list = []
counter = 1

while counter <= 5:
    number = int(input(f'Ingrese el numero {counter}: '))
    counter += 1
    my_list.append(number)

counter = 0
smallest = my_list[0]

for num in my_list:
    if smallest > num:
        smallest = num
print(f'El menor valor es {smallest}')

