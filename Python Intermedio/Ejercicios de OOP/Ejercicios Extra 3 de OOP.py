class Product:
    
    def __init__(self,name, price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.my_inventory = []
    
    def show_products(self):
        for products in self.my_inventory:
            print(f"name:{products.name}")
            print(f"Price: {products.price}")
            print(f"Stock: {products.quantity}")
            print()

    def get_product(self):
        while True:
            name = input("Ingrese el nombre del producto: ")
            while True:
                try:
                    price = float(input("Ingrese el precio: "))
                    break
                except ValueError:
                    print("\nIngrese un valor numérico***")
            while True:     
                try:
                    quantity = int(input("Ingrese la cantidad en stock: "))
                    break
                except ValueError:     
                    print("\nIngrese un valor numérico***")
            product = Product(name,price,quantity)
            self.my_inventory.append(product)
            option = input("Desea agregar otro producto? y/n: ")
            if option.lower() != "y":
                break
    
    def get_total_inventory(self):
        total_inventory = 0
        for products in self.my_inventory:
            total_inventory += products.price * products.quantity
        return total_inventory

inventory = Inventory()

while True:            
    print("\nINVENTARIO")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Calcular valor total del inventario")
    print("4. Salir")
    try:
        my_selection = int(input("Seleccione una opción: "))
        if my_selection == 1:
            print("\nADD NEW PRODUCT:")
            inventory.get_product()
        elif my_selection == 2:
            print("\nSTOCK: ")
            inventory.show_products()
        elif my_selection == 3:
            print("\nTOTAL:")
            print(f"El total del inventario es de: {inventory.get_total_inventory()}")
        elif my_selection == 4:
            break
        else: 
            print("\nOpción inválida. Intente nuevamente.\n")
    except ValueError:
        print("Ingrese una opción valida")


