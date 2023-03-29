from abc import ABC, abstractmethod
# from abc import ABCMeta, abstractmethod

class Shape(ABC):
    @abstractmethod  # we cant make obj of abstract class
    def printarea(self):  # it say we must add printarea funct in all class it inherited
        return 0

class Rect(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 9

    def printarea(self):
        return self.length * self.breadth

rect1 = Rect()
print(rect1.printarea())