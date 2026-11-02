class Circle:
    radius = 0
    
    def get_area(self):
        area = 3.14 * (self.radius **2)
        return area
    
my_circle = Circle()
my_circle.radius = 5

print("Area of the circle:", my_circle.get_area())

