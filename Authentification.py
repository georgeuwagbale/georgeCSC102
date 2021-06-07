import pymongo
from Bank import Customer


class Authentification:

    def __init__(self):
        self.client = self.connection()

    def function(self):
        response = input("Do you have an account with Bank-X? (y/n): ")
        if response == "y" or response == "Y":
            self.login()
        elif response == "n" or response == "N":
            self.signup()

    @classmethod
    def connection(cls):
        client = pymongo.MongoClient(
            "mongodb+srv://George:realghost16@cluster1.qvpms.mongodb.net/Bank?retryWrites=true&w=majority")
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
                    instance = Customer(match.get("name"), match.get("account number"), match.get("pin"),
                                        match.get("bvn"), self.client)
                    instance.function()
                    break
                else:
                    print("Incorrect password, account number or pin")
        else:
            response = input("Account doesn't exist. \nConsider creating and account with BANK-X (y/n): ")
            if response == "y" or response == "Y":
                self.signup()

    def signup(self):
        print("\nPlease signup")
        name = input("Name: ")
        account_number = int(input("Account Number: "))
        pin = int(input("Pin: "))
        bvn = int(input("bvn: "))
        instance = Customer(name, account_number, pin, bvn, self.client)
        data = {
            "name": instance.name,
            "account number": instance.account_number,
            "pin": instance.pin,
            "bvn": instance.bvn,
            "account balance": instance.account_balance,
            "transactions": instance.transaction,
            "account type": instance.account_type
        }
        connection = self.client
        connection.insert_one(data)
        print("Signed up successfully")
        self.login()


Authentification().function()
