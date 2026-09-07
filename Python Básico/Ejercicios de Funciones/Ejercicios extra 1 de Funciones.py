text = input("Ingrese su texto: ")

character = input("Ingrese el carácter que desea buscar: ")

def total_character(text,character):
    total = 0
    for letter in text:
        if letter == character:
            total +=1
    return total

print(f"Se a encontrado {total_character(text,character)} veces el carácter")