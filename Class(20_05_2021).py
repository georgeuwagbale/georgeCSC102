# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


class Coffee:
    coffeeCupCounter = 0
    def __init__(self, themilk, thesugar, thecoffeemate):
        self.milk = themilk
        self.sugar = thesugar
        self.coffeemate = thecoffeemate
        Coffee.coffeeCupCounter +=1

    def output_coffee(self):
        return f"You now have your coffee with {self.milk} milk, {self.sugar} sugar, {self.coffeemate} coffeemate"


mycoffee = Coffee(1, 2, 3).output_coffee()
print(mycoffee)
myMuchSugarCoffee = Coffee(2, 10, 1)
#print(myMuchSugarCoffee)
print(myMuchSugarCoffee.sugar)
print(f"W have made {myMuchSugarCoffee.coffeeCupCounter} coffee cups so far")



