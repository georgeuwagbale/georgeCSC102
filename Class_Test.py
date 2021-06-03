
class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    @classmethod
    def speak(cls):
        return "Woof"

    def __str__(self):
        return f"Name: {self.name} Breed: {self.breed}"

dog = Dog("Bruno","Local")
dog1 = Dog.speak()
print(dog.speak())
print(dog1)
