my_list = []
amount = int(input("Ingrese el número de Palabras: "))
for n in range(1, amount + 1):
    word = input(f"Ingrese su palabra {n}: ")
    my_list.append(word)
min_letters = int(input("Ingrese el número de letras mínimas en la palabra: "))

def limit_result(my_list, min_letters):
    new_list = []
    for word in my_list:
        if len(word) > min_letters:
            new_list.append(word)
    return new_list

print(f"{limit_result(my_list, min_letters)}")