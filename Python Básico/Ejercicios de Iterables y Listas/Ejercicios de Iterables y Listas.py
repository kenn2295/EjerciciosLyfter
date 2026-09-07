#1
first_list = ['Hay', 'en', 'que','iteracion', 'indices','muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']

for i in range(len(first_list)):
    print(first_list[i],second_list[i])
print()
    
#2
my_string = input('Ingrese su frase: ')

for i in range(len(my_string)-1,-1,-1):
    print(my_string[i])
print()

#3
my_list = []

while True:
    numbers = input('Ingrese un numero (o ENTER/stop para salir): ').lower()

    if numbers == "" or numbers == "stop":
        break
    my_list.append(numbers)

if len(my_list) >= 2:
    print(f'Su lista es: {my_list}')
    my_list[0], my_list[-1] = my_list[-1], my_list[0]
    print(f'Su lista intercambiada es: {my_list}')
else:
    print('Innecesario validar, solo hay un número o ninguno')
print()

#4
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in my_list[:]: #esta funcionalidad crea una copia mientras recorro la lista buscando los impares
    if num % 2 != 0: #si el numero es impar entra al if
        my_list.remove(num) #elimina el num impar
print(my_list) #imprime lista actualizada
print()

#5
counter = 1
my_list = []
while counter <= 10:
    numbers = int(input(f'Ingrese el numero {counter}: '))
    my_list.append(numbers)
    counter += 1
counter = 0
greater = my_list[0]
for num in my_list:
    if greater < num:
        greater = num
        counter += 1
print(f'{my_list}. El más alto fue {greater}')