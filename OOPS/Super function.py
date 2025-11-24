# super() - Function used in a child class to call methods from a parent class (superclass).
#            Allows you to extend the functionality of the inherited methods

class Shapes:
    def __init__(self,color,filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"it is {self.color} and it is {"filled" if self.filled else "not filled"}")


class Circle(Shapes):
    def __init__(self,color,filled, radius):
        #self.color = color
        #self.is_filled = is_filled
        super().__init__(color,filled)
        self.radius = radius

    def describe(self):
            print(f"The area of the circle is {3.14 * self.radius ** 2}cm^2")


class Square(Shapes):
    def __init__(self,color,filled,length):
        #self.color = color
        #self.is_filled = is_filled
        super().__init__(color,filled)
        self.length = length
    def describe(self):
        print(f"Area of square is {self.length*self.length}cm^2")
        super().describe()

class Triangle(Shapes):
    def __init__(self,color,filled,width,height):
        #self.color = color
        #self.is_filled = is_filled
        super().__init__(color,filled)
        self.width = width
        self.height = height
    def describe(self):
        print(f"Area of triangle is {1/2*self.width*self.height}cm^2")
        super().describe()

circle = Circle("red",True,5)
square = Square("blue",True,5)
triangle = Triangle("green",False,5,10)

circle.describe()
square.describe()
triangle.describe()

# print(circle.color)
# print(circle.filled)
# print(circle.radius)
# print("")
# print(square.color)
# print(square.filled)
# print(square.length)
# print("")
# print(triangle.color)
# print(triangle.filled)
# print(triangle.width)
# print(triangle.height)

