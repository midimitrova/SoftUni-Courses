from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, r):
        self.__r = r

    def calculate_area(self):
        return pi * self.__r ** 2

    def calculate_perimeter(self):
        return pi * 2 * self.__r


class Rectangle(Shape):

    def __init__(self, height, weight):
        self.__height = height
        self.__weight = weight

    def calculate_area(self):
        return self.__height * self.__weight

    def calculate_perimeter(self):
        return 2 * (self.__weight + self.__height)


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())


rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())

