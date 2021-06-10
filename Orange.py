class Orange:
    cost_of_orange = 25

    def __init__(self):
        self.Amount_of_orange_available = 50

    def demand(self):
        print(f"Unit price of orange = ${self.cost_of_orange}\nWe have {self.Amount_of_orange_available} in stock")

        trial = True
        while trial:
            amount_demanded = int(input("Input the amount of orange you want to purchase: "))
            if amount_demanded > self.Amount_of_orange_available:
                print("The amount you requested is above the amount of oranges we have in stock")
                print("Enter amount below the amount of orange in stock")

            elif amount_demanded < self.Amount_of_orange_available:
                trial = False
                return self.purchase(amount_demanded)

            elif amount_demanded < 1:
                print("The amount you requested is not up to 1")
                print("Enter something reasonable")



    def purchase(self, amount):
        print(f"Quantity = {amount}")
        total_cost = amount * self.cost_of_orange
        print(f"Total cost of purchase = ${total_cost}")
        confirm = input("Confirm purchase (y/n): ")
        if confirm == "y":
            return "Thank yo for patronizing us"


test = Orange().demand()
