# define a circle class to  create a circle with radius r using constructor define an AREA() method of the class which calculates the area of the circle , define a parameter method of the class which alloys you to calculate the parameter of the circle .

class Circle:
    def  __init__ (self , radius):
        self.radius = radius

    def Area(self):
        return 3.14 * self.radius **2
    
    def parameter(self):
        return 2 * 3.14 * self.radius

c1 = Circle(21)
print(c1.Area())
print(c1.parameter())