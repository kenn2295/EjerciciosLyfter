#1
#1.1
print()
item_price = int(input('Ingrese el precio del producto: '))
if item_price < 100:
        discount = item_price * 0.02
        final_price = item_price - discount
        message = (f'El producto con el descuento vale: {final_price}')
else:
    discount = item_price * 0.10 
    final_price = item_price - discount
    message = (f'El producto con el descuento vale: {final_price}')
print(message)

#1.2
print()
time_seconds = int(input('Ingrese el tiempo en segundos: '))
time_missing = 600 - time_seconds

if time_seconds < 600:
    print(f'faltarían {time_missing} segundos para llegar a 10 minutos')
elif time_seconds > 600:
    print('Mayor')
else:
    print('Igual')
    
#1.3
print()
your_number = int(input('Ingrese su numero: '))
counter = 1
sum = 0
while counter <= your_number:
    sum += counter
    counter += 1
print(f'El resultado es {sum}')

#2
#2.1
print()
import random
secret_number = random.randint(1,10)
guess = int(input('Adivine un numero del 1 al 10: '))
while guess != secret_number:
    guess = int(input('Incorrecto, intente de nuevo: '))
else:
    print(f'Adivinaste era el {secret_number}')
    
#2.2
print()
num1 = int(input(f'Ingrese el numero 1: '))
num2 = int(input(f'Ingrese el numero 2: '))
num3 = int(input(f'Ingrese el numero 3: '))
sum = num1 + num2 + num3
if num1 == 30 or num2 == 30 or num3 == 30 or sum == 30:
    print('Correcto')
else:
    print('Incorrecto')

#3
print()
celsius = int(input('Ingrese temperatura en Celsius: '))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15
print(f'Fahrenheit: {fahrenheit}')
print(f'Kelvin: {kelvin}')

#4
print()
num = int(input('Ingrese un número: '))
for i in range (1,13):
    print(f'{num} x {i} = {num * i}' ) 