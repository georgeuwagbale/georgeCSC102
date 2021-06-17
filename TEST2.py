#GEORGE IKE UWAGBALE

class Online:
    def __init__(self, numberOfitemsbought, totalcost):
        self.numberOfitemsbought = numberOfitemsbought
        self.totalcost = totalcost

    def calculator(self):
        if self.numberOfitemsbought < 10 and self.totalcost > 100000:
            total_cost = self.totalcost * (90/100)
            return f"Total cost for {self.numberOfitemsbought} items is N{self.totalcost}, with a discount of 10%, you would pay N{total_cost} "

        elif self.numberOfitemsbought > 10 and self.totalcost > 100000:
            total_cost = self.totalcost * (90/100)
            return f"Total cost for {self.numberOfitemsbought} items is N{self.totalcost}, with a discount of 10%, you would pay N{total_cost} . You have a gift"

        else:
            return f"Total cost for {self.numberOfitemsbought} items is N{self.totalcost}"


demand = int(input("Quantity of items purchased: "))
total_Cost = float(input("Total cost of items purchased: "))

instance = Online(demand, total_Cost).calculator()
print(instance)

