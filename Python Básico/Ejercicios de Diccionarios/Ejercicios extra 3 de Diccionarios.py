products = []

amount = int(input('cantidad de productos vendidos: '))

print()
for n in range(amount):
    
    name = input('Nombre del producto: ').capitalize()
    category = input('Categoria del producto: ').capitalize()
    price = float(input('Precio: '))
    
    sale = {
        'name': name,
        'category': category,
        'price': price
    }
    
    products.append(sale)

result = {}

print('\nVENTAS POR CATEGORIA')
for product in products:
    if product['category'] not in result:
        result[product['category']] = 0
    result[product['category']] += product['price']
    
for key, value in result.items():
    print(f'{key}: {value}')
    
#abajo muestro el ejercicio 3 sencillo como se pide realizar
"""
products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

print('\nVENTAS POR CATEGORIA')
for product in products:
    if product['category'] not in result:
        result[product['category']] = 0
    result[product['category']] += product['price']
    
for key, value in result.items():
    print(f'{key}: {value}')
"""
