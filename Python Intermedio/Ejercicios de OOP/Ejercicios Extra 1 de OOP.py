class Rectangle:
    
    def __init__(self):
        while True:
            try:
                height = float(input("Ingrese la altura: "))
                width = float(input("Ingrese el ancho: "))
                if width < 0 or height < 0:
                    raise ValueError("Existe un valor negativo, los valores deben ser positivos")
                self.height = height
                self.width = width
                break
            except ValueError as error:
                print(error) 
    
    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter

rectangle_1 = Rectangle()
print(f"El Área del rectángulo 1 es: {rectangle_1.get_area()}")
print(f"El Perímetro del rectángulo 1 es: {rectangle_1.get_perimeter()}")

rectangle_2 = Rectangle()
print(f"El Área del rectángulo 2 es: {rectangle_2.get_area()}")
print(f"El Perímetro del rectángulo 2 es: {rectangle_2.get_perimeter()}")