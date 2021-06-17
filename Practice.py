class Mother:

    def __init__(self, name, number_of_children, age):
        self.name = name
        self.number_of_children = number_of_children
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Number of Children: {self.number_of_children}, Age: {self.age}"


class Child(Mother):

    def __init__(self, name, number_of_children, age, school):
        super().__init__(name, number_of_children, age)
        self.school = school

    def __str__(self):
        return f"Name: {self.name}, Number of Children: {self.number_of_children}, Age:{self.age}, School:{self.school}"


p1 = Mother("Chika", 5, 38)
print(p1)
print(p1.name)
p2 = Child("George", 0, 19, "PAU")
print(p2)
print(p2.name)
