from abc import ABC, abstractmethod


class Bird(ABC):
    @staticmethod
    def defecate():
        return "Pooh"

    def move(self):
        pass


class Fowl(Bird):
    def move(self):
        return "Fly, walk and run"


class Turkey(Bird):
    def move(self):
        return "Fly, walk and run"


class Guineafowl(Bird):
    def move(self):
        return "Fly, walk and run"


class Ostrich(Bird):
    def move(self):
        return "run & walk"