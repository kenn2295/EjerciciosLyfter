def my_list():
    while True:
        new_list = []
        try:
            amount = int(input("Cuantos elementos desea ingresar? "))
        except ValueError:
            print("Ingrese valores numéricos\n")
            continue
        for n in range(1,amount+1):
            element = input(f"Ingrese el elemento {n}: ")
            new_list.append(element)
        return new_list

def convert_to_int(my_list):
    print("\nResultado:")
    for n in my_list:
        original = n
        try:
            n = int(n)
        except ValueError:
            print(f"No se pudo convertir el elemento: '{original}'")
        else:
            print(f"'{original}' convertido a {n}")
    
convert_to_int(my_list())
