class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        return 3.14 * (self.radius ** 2)

my_circle = Circle(5)
my_second_circle = Circle(10)
print("the area of the circle is: ", my_circle.get_area())
print("the area of the second circle is: ", my_second_circle.get_area())