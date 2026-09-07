def get_name():
    while True:
        try:
            name = input("Ingrese su nombre: ")
            if name.isdigit():
                raise ValueError("El nombre no puede ser un número")
            return name
        except ValueError as error:
            print(error)

def get_age():
    while True:
        try:
            age = int(input("Ingrese su edad: "))
            return age
        except ValueError:
            print("Número no valido\n")

def main(name,age):
    print(f"Hola {name}, su edad es {age}")
    
main(get_name(),get_age())