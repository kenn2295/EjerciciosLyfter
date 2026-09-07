my_list = []
amount = int(input('Cuantos numeros desea agregar a la lista? '))
for n in range(amount):    
    number = int(input('Ingese el numero: '))
    my_list.append(number)
    
def total_numbers(my_list):
    total = 0
    for num in my_list:
        total += num
        
    return total

print(f"El total es: {total_numbers(my_list)}")
    