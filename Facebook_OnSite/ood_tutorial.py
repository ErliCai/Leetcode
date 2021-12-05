



class Shape():

    def __init__(self, shapename = None):

        self.name = shapename

    def shape():
        return "shape"

    def draw():
        return "Drawing a " + Shape.shape()

    def getname(self):
        return self.name

    def liangchengjirii(self):

        #  implementation

        return True


class Circle(Shape):

    def __init__(self, name=None, diameter = 0):
        super().__init__(shapename=name)
        # self.name = name
        self.diameter = diameter

    def area(self):
        return (self.diameter/2) ** 2 * 3.14

    def shape():
        return "Circle"

class Square(Shape):

    def __init__(self, name=None, length = 0):
        super().__init__(name=name)
        self.length = length

    def area(self):
        return self.length ** 2

    def shape():
        return "Square"


circle1 = Circle(name = "circle1", diameter = 2)
print(circle1.getname())
print(circle1.area())


# # static method
# print(Shape.shape())
# # print(Shape.shape2("shape"))
shape1 = Shape(num = 1, name = "lixue")
# shape2 = Shape("shape2")
# shape3 = Shape()

# print(shape1.getname())
# print(Shape.getname())



# print(shape1.name)
# print(shape2.name)
# print(shape3.name)


class Circle(Shape):

    def __init__(self, name=None, diameter = 0):
        super().__init__(name=name)
        self.diameter = diameter

    def area(self):
        return self.diameter ** 2 * 3.14

    def shape():
        return "Circle"



class Square(Shape):

    def __init__(self, name=None, length = 0):
        super().__init__(name=name)
        self.length = length

    def area(self):
        return self.length ** 2

    def shape():
        return "Square"
