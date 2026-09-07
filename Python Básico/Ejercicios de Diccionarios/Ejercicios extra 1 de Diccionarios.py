sales = []

amount = int(input('Cuantas ventas deseas registrar? '))

for n in range(amount):
    
    date = input('Ingrese la fecha: ')
    customer_email = input('Ingrese el correo del usuario: ')
    
    items = []
    amount_items = int(input('Cuantos productos tiene la venta? '))
    
    for m in range(amount_items):
        
        name = input('Ingrese el nombre del producto: ')
        upc = input('Ingrese el UPC del producto: ')
        unit_price = float(input('Ingrese el precio del producto: '))
        
        product = {
            'name': name,
            'upc': upc,
            'unit_price': unit_price
        }
        items.append(product)
        
    sale = {
    'date': date,
    'customer_email': customer_email,
    'items': items
    }
    sales.append(sale)
print(sales)

result = {}
for sale in sales:
    for item in sale['items']:

        if item['upc'] not in result:
            result[item['upc']] = 0
        result[item['upc']] += item['unit_price']
        
print("\nresult =")
for key, value in result.items():
    print(f'{key}: {value}')

