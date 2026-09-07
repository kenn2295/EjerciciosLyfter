def my_list():
    new_list = []
    amount = int(input("Cuantos elementos desea ingresar? "))
    for n in range(1,amount+1):
        element = input(f"Ingrese el elemento {n}: ")
        new_list.append(element)
    return new_list

def sum_values(my_list):
    print("\nResultado:")
    total = 0
    for n in my_list:
        try:
            n = float(n)
        except ValueError:
            print(f"Elemento inválido: {n}")
        else:
            counter = counter+n
            print(f"{n} sumado correctamente")
    print(f"Total de la suma: {total}")
    
sum_values(my_list())