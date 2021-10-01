import pymongo
from Bank_v2 import Customer


class Authentification:

    def __init__(self):
        self.client = self.connection()

    def function(self):

        response = input("Do you have an account with Bank-X? (y/n): ")
        if response.lower() == "y":
            self.login()
        elif response.lower() == "n":
            self.signup()

    @classmethod
    def connection(cls):
        client = pymongo.MongoClient("mongodb://localhost:27017/")

        # client = pymongo.MongoClient(
        #    "mongodb+srv://George:realghost16@cluster1.qvpms.mongodb.net/Bank?retryWrites=true&w=majority")
        db = client["Bank"]
        collection = db["customers"]
        return collection

    def login(self):
        print("\nPlease login")
        account_number = int(input("Account Number: "))
        pin = int(input("Pin: "))
        match = self.client.find_one({"account number": account_number, "pin": pin})
        if match:
            trial = 3
            while trial != 0:
                if account_number == match.get("account number") and pin == match.get("pin"):
                    print("Verified")
                    instance = Customer(match.get("account number"), match.get("pin"), self.client)
                    instance.function()
                    break
                else:
                    print("Incorrect password, account number or pin")
        else:
            response = input("Account doesn't exist.\nConsider creating and account with BANK-X (y/n): ")
            if response.lower() == "y":
                self.signup()

    def signup(self):
        print("\nPlease signup")
        name = input("Name: ")
        account_number = int(input("Account Number: "))
        pin = int(input("Pin: "))
        bvn = int(input("bvn: "))
        # instance = Customer(name, account_number, pin, bvn)
        data = {
            "name": name,
            "account number": account_number,
            "pin": pin,
            "bvn": bvn,
            "account balance": 0,
            "transactions": "",
            "account type": "Dollar"
        }
        connection = self.client
        connection.insert_one(data)
        print("Signed up successfully")
        self.login()


Authentification().function()
