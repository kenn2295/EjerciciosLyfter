employees  = []

amount = int(input('¿Cuantos empleados desea ingresar? '))

print()
for n in range(amount):
    
    name = input('Ingrese el nombre: ').capitalize()
    email = input('Ingrese el correo: ').lower()
    department = input('Ingrese el departamento (TI, Ventas o RRHH): ').upper()
    
    employee = {
        'name': name,
        'email': email,
        'department': department
    }
    
    employees.append(employee)
    
result = {}

print()
for employee in employees:
    
    if employee['department'] not in result:
        result[employee['department']] = []
        
    result[employee['department']].append(employee)
        
for key, value in result.items():
    print(f'\nDEPARTAMENTO DE {key}')
    for employee in value:
        print(f'- {employee['name']} ({employee['email']})')