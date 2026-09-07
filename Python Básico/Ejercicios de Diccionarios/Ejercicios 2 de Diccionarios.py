print()
list_a = []
list_b = []

amount = int(input("¿Cuántos datos vas a ingresar?: "))

for i in range(amount):
    key = input("Ingrese la key: ")
    value = input("Ingrese el value: ")

    list_a.append(key)
    list_b.append(value)

final_dic = dict(zip(list_a, list_b))
print('LISTAS')
print(list_a)
print(list_b)
print('DICCIONARIO')
print(final_dic)