import math

class Shape:
    def area(self):
        raise NotImplementedError ("classes need to override this method")
    
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()

        self.length= length
        self.width= width

    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        """Initialize the circle with a radius."""
        self.radius = radius
    
    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)