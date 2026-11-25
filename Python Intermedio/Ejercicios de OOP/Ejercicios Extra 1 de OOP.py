def insert_values():
    while True:
        try:
            height = float(input("Ingrese la altura: "))
            width = float(input("Ingrese el ancho: "))
            if width < 0 or height < 0:
                raise ValueError("Existe un valor negativo, los valores deben ser positivos")
            return height, width
        except ValueError as error:
            print(error)
    

class Rectangle:
    
    def __init__(self,height,width):

                self.height = height
                self.width = width
                
    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter

my_value_1 = insert_values()
rectangle_1 = Rectangle(*my_value_1)
print(f"El Área del rectángulo 1 es: {rectangle_1.get_area()}")
print(f"El Perímetro del rectángulo 1 es: {rectangle_1.get_perimeter()}")


my_value_2 = insert_values()
rectangle_2 = Rectangle(*my_value_2)
print(f"El Área del rectángulo 2 es: {rectangle_2.get_area()}")
print(f"El Perímetro del rectángulo 2 es: {rectangle_2.get_perimeter()}")