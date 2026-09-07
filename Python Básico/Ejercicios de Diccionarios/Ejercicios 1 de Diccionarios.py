my_hotel = {
    'name': 'Tamarindo Diria',
    'number_of_stars': 7,
    'rooms': [
        {'number': 1,
        'floor':1,
        'price_per_night': 50
        },
        {'number': 750,
        'floor':2,
        'price_per_night': 100
        },
        {'number': 75,
        'floor':10,
        'price_per_night': 1000
        }
        ]
    }
print(f'DICCIONARIO DEL HOTEL:')
for key, value in my_hotel.items():
    print(f' {key}: {value}')
print(f'\n DICCIONARIO DE HABITACIONES:')
for room in my_hotel['rooms']:
    for key, value in room.items():
        print(f' {key}: {value}')
    print()
