def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def prime_numbers(my_list):
    result = []

    for num in my_list:
        if is_prime(num):
            result.append(num)

    return result


my_list = []
amount = int(input('Cuantos numeros desea ingresar? '))

for n in range(amount):
    num = int(input('Ingrese su numero: '))
    my_list.append(num)

print(prime_numbers(my_list))