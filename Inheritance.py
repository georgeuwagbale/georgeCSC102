class Student:
    def __init__(self, name, age, hight):
        self.name = name
        self.age = age
        self.hight = hight

    def __str__(self):
        return f"{self.name}, {self.age}, {self.hight}"


class PostGrad(Student):
    def __init__(self, name, age, house, hight):
        self.house = house
        super().__init__(name, age, hight)


S = Student("Ike", 13, 60)
P = PostGrad("George", 12, "Co", 15)
print(P.)



