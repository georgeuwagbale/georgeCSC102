# Authentification 1.0
import pymongo
from Bank import Customer


class Authentification:

    def __init__(self):
        self.client = self.connection()

    def function(self):

        response = input("Do you have an account with Bank-X? (y/n): ")
        if response.lower == "yes" or response.lower() == "y":
            self.login()
        elif response.lower() == "n" or response.lower() == "no":
            self.signup()
        elif response.lower() == "sudo":
            self.sudo_access()

    @staticmethod
    def connection():
        # client = pymongo.MongoClient("mongodb://localhost:27017/")
        client = pymongo.MongoClient(
            "mongodb+srv://George:realghost16@cluster1.qvpms.mongodb.net/Bank?retryWrites=true&w=majority")
        db = client["Bank"]
        collection = db["customers"]
        return collection

    def login(self):
        print("\nPlease login")
        account_number = int(input("Account Number: "))
        pin = int(input("Pin: "))
        profile = self.collection.find_one({"account number": account_number, "pin": pin})
        if profile:
            trial = 3
            while trial != 0:
                if account_number == profile.get("account number") and pin == profile.get("pin"):
                    print("Verified")
                    instance = Customer(profile, self.collection)
                    instance.function()
                    break
                else:
                    print("Incorrect password, account number or pin")
        else:
            response = input("Account doesn't exist. \nConsider creating and account with BANK-X (y/n): ")
            if response == "y" or response == "Y" or response == "yes" or response == "Yes" or response == "YES":
                self.signup()

    def signup(self):
        print("\nPlease signup")
        name = input("Name: ")
        account_number = int(input("Account Number: "))
        pin = int(input("Pin: "))
        if_bvn = input("Do have a bvn: ")
        bvn = 0
        if if_bvn.lower() == "yes" or if_bvn.lower() == "y":
            bvn += int(input("bvn: "))
        elif if_bvn.lower() == "no" or if_bvn.lower() == "n":
            bvn += Customer.bvn_generator()

        data = {
            "name": name,
            "account number": account_number,
            "pin": pin,
            "bvn": bvn,
            "account balance": 0,
            "account type": "Dollar"
        }
        connection = self.collection
        connection.insert_one(data)
        print("Signed up successfully")
        self.login()

    def sudo_access(self):
        password = input("Input password: ")
        if password == "ghost":
            data = self.collection.find({},{"_id":0,"name":1,"account number":1,"pin":1})
            for a in data:
                print(a)


Authentification().function()
