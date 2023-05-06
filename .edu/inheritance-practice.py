# super() and multiple inheritances
# https://realpython.com/python-super/#multiple-inheritance-alternatives

class Triangle:
    def __init__(self, base, height, **kwargs):
        self.base = base # redundant? since .base already set in RightPyramid but is needed for Triangle initialization
        self.height = height
        super().__init__(**kwargs)
    
    def tri_area(self):
        return (self.base * self.height) / 2

# --

class Rectangle:
    def __init__(self, length, width, **kwargs):
        """
        1. __init__ called by Square
        2. super() below initializes next class: Triangle
        3. Triangle initialization is passed base and height attributes from RightPyramid initialization
        4. Base and height can now be used as args to resolve area_2() function call
        """
        
        self.length = length
        self.width = width
        
        super().__init__(**kwargs)
    
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    
class Square(Rectangle):
    def __init__(self, length, **kwargs):
        super().__init__(length = length, width = length, **kwargs)

# --

class VolumeMixin:
    def volume(self):
        return self.area() * self.length

class Cube(VolumeMixin, Square):
    def __init__(self, length):
        super().__init__(length)
        self.height = length

    def surface_area(self):
        return super().area() * 6

class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height

        kwargs["height"] = slant_height
        kwargs["length"] = base
        super().__init__(base = base, **kwargs)

    def area(self):
        base_area = super().area() # which superclass to call method on proxy object?
        perimeter = super().perimeter() # calls .perimeter() on Rectangle through Square superclass
        return (perimeter * self.slant_height + base_area) / 2

    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area