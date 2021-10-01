from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    length = 3
    breadth = 5

    def calculate_area(self):
        return self.length * self.breadth


class Circle(Shape):
    radius = 4

    def calculate_area(self):
        return 3.14 * self.radius * self.radius


rec = Rectangle()
cir = Circle()
print("Area of a rectangle:", rec.calculate_area())
print("Area od a circle:", cir.calculate_area())


class Animal:

    def move(self):
        return "Moving"


class Dog(Animal):
    name = "Dog"

    def move(self):
        print(self.name)
        return "running"


d1 = Dog()
print(Dog.move(d1))
#print(Dog.name)