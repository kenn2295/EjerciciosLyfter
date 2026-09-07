my_list = []
counter = 1

while counter <= 5:
    words = input(f'Ingrese la palabra {counter}: ')
    counter += 1
    my_list.append(words)

new_list = []
for long_word in my_list:
    if len(long_word) > 4:
        new_list.append(long_word)
if new_list:
    print(new_list)
else:  
    print('No tiene palabras de mas de 4 letras')