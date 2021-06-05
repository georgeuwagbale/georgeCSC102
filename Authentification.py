import pymongo

class Authentification:

    def __init__(self):
        self.client = self.connection()

    @classmethod
    def connection(cls):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client.get_database("Bank")
        collection = db.get_collection("customers")
        return collection

    def login(self):
        name = input("Name: ")
        account_number = int(input("Account Number: "))
        pin = int(input("Pin: "))
        match = self.client.find_one({"name": name, "account number": account_number, "pin": pin})
        if match:
            trial = 3
            while trial != 0:

                if name == match.get("name") and account_number == match.get("account number") and pin == match.get("pin"):
                    from Bank import Customer
                    instance = Customer(match.get("name"), match.get("account number"), match.get("pin"), match.get("bvn"))
                    break
                else:
                    print("Incorrect password, account number or pin")

test = Authentification().login()
test