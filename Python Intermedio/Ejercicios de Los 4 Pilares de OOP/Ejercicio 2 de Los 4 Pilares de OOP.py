from abc import ABC, abstractmethod
import math

class Shape(ABC):
    
    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    @abstractmethod    
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter
    def calculate_area(self):
        area = math.pi * self.radius **2
        return area

class Square(Shape):
    def __init__(self,side):
        self.side = side
    def calculate_perimeter(self):
        perimeter = 4 * self.side
        return perimeter
    def calculate_area(self):
        area = self.side **2
        return area

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def calculate_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter
    def calculate_area(self):
        area = self.width * self.height
        return area
    
circle = Circle(80)
print(f"El perímetro del circulo es: {circle.calculate_perimeter():.2f}")
print(f"El area del circulo es: {circle.calculate_area():.2f}")

square = Square(40)
print(f"El perímetro del cuadrado es: {square.calculate_perimeter():.2f}")
print(f"El area del cuadrado es: {square.calculate_area():.2f}")

rectangle = Rectangle(10,15)
print(f"El perímetro del rectángulo es: {rectangle.calculate_perimeter():.2f}")
print(f"El area del rectángulo es: {rectangle.calculate_area():.2f}")
