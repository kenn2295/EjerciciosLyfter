def insert_text():
    new_text = input("Por favor ingrese su linea de texto: ")
    return new_text

def append_to_existing_file(file_name,new_text):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()

        with open(file_name, 'a', encoding='utf-8') as file:
            if content:
                file.write(f"\n{new_text}")
            else:
                file.write(new_text)

    except FileNotFoundError:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(new_text)


def main():
    file_name = "extra4.txt"
    new_text = insert_text()
    append_to_existing_file(file_name,new_text)
    print("Texto agregado correctamente")


main()