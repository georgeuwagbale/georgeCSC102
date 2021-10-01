class Customer:
    # Init method
    def __init__(self, account_number, pin, database_connection):
        self.client = database_connection
        self.account_number = account_number
        self.pin = pin
        self.name = self.client.find_one({"account number": self.account_number, "pin": self.pin}).get("name")
        self.bvn = self.client.find_one({"account number": self.account_number, "pin": self.pin}).get("bvn")
        self.account_type = self.client.find_one({"account number": self.account_number,
                                                  "pin": self.pin}).get("account type")
        self.account_balance = self.client.find_one({"account number": self.account_number,
                                                     "pin": self.pin}).get("account balance")
        self.transaction = {
            "Debit": [],
            "Credit": []
        }

    # Method for changing user pin
    def change_pin(self):
        print("\n\t---CHANGE OF PIN---")

        if self.pin:
            trial = 3
            while trial != 0:
                old_pin = int(input("Input old pin: "))
                if old_pin == self.pin:
                    new_pin = int(input("Input new pin: "))
                    self.pin = self.client.update_one({"name": self.name, "account number": self.account_number},
                                                      {"$set": {"pin": new_pin}})
                    print("You have successfully changed your password")
                    break
                else:
                    print("Incorrect password, try again")
                trial -= 1
        self.perform_another_transaction()

    # Method for deposit
    def deposit(self):
        print("\n\t---DEPOSIT---")
        balance = float(input("\nHow much do you want to deposit: "))
        # retrieved_balance = self.client.find_one({"account number": self.account_number, "bvn": self.bvn})
        # self.account_balance = retrieved_balance.get("account balance")
        # self.client.find_one({"account number": self.account_number, "bvn": self.bvn}).get("account balance")
        self.account_balance += balance
        self.client.find_one_and_update({"account number": self.account_number, "bvn": self.bvn},
                                        {"$set": {"account balance": self.account_balance}})
        self.transaction.get("Credit").append(balance)
        self.alert(message="credit", transaction_amount=balance)
        self.perform_another_transaction()

    # Method for withdrawal
    def withdrawal(self):
        print("\n\t---WITHDRAWAL---")
        trial = 3
        while trial != 0:
            request_pin = int(input('Pin: '))
            if request_pin == self.pin:
                withdrawal = float(input("Pin correct.\nHow much do you want to withdrawal: "))

                # self.account_balance = self.client.find_one(
                #    {"account number": self.account_number, "bvn": self.bvn}).get("account balance")

                if self.account_balance >= withdrawal:
                    self.account_balance -= withdrawal
                    self.client.find_one_and_update({"account number": self.account_number, "bvn": self.bvn},
                                                    {"$set": {"account balance": self.account_balance}})
                    self.transaction.get("Debit").append(withdrawal)
                    self.alert(message="debit", transaction_amount=withdrawal)
                    break

                else:
                    print("Insufficient fund")
                    break
            else:
                print("Pin is incorrect, try again.")
            trial -= 1
        self.perform_another_transaction()

    # Method for transfer
    def transfer(self):
        print("\n\t---TRANSFER---")
        amount = float(input("Amount: "))
        int(input("Recipient's Account number: "))
        input("Recipient's bank: ")
        pin = int(input("Input your pin to verify: "))
        trial = 3
        while trial != 0:
            if pin == self.pin:
                self.account_balance -= amount
                self.client.find_one_and_update({"account number": self.account_number, "bvn": self.bvn},
                                                {"$set": {"account balance": self.account_balance}})
                print("Transaction successful")
                self.alert("debit", amount)
            else:
                print("Incorrect pin, try again")
            trial -= 1
        self.perform_another_transaction()

    # This method displays and the available transactions of BANK-X
    def function(self):
        print("\t\t\tWELCOME TO BANK-X \n")
        print(
            "Enter '1' to Deposit \n Enter '2' to Withdrawal \n Enter '3' to Change of Pin \n Enter '4' to get a "
            "statement of account")
        print("Enter '5' to view your profile")
        try:
            response = int(input("What transaction do you want to perform: "))

            if response == 1:
                return self.deposit()
            elif response == 2:
                return self.withdrawal()
            elif response == 3:
                return self.change_pin()
            elif response == 4:
                return self.statement_of_account()
            elif response == 5:
                return self.profile()
            elif response == 6:
                return self.transfer()
            else:
                print("Input out of range")
        except ValueError:
            print("Invalid input")

    # Method for statement of account
    def statement_of_account(self):
        pass

    # Method for alert
    def alert(self, message, transaction_amount):
        revised_account_number = str(self.account_number)
        coded_account_number = revised_account_number[0:3] + "****" + revised_account_number[8:]
        if message == "debit":
            print(
                f"\n\tDebit \nAmount: ${transaction_amount} \nAccount: {coded_account_number} "
                f"\nBalance: ${self.account_balance}")
        elif message == "credit":
            print(
                f"\n\tCredit \nAmount: ${transaction_amount} \nAccount: {coded_account_number} "
                f"\nBalance: ${self.account_balance}")

    # Method for retrieving profile details of the user
    def profile(self):
        print("\n\tProfile")
        print(f"\nName: {self.name} Account Number: {self.account_number}")
        print(f"Account Balance: ${self.account_balance} Account Type: {self.account_type}")
        self.perform_another_transaction()

    # __str__ method
    def __str__(self):
        return f"Name: {self.name}; Account Number: {self.account_number}; Account Balance: ${self.account_balance}"

    # This methods asks the user is he/she wants to perform another transaction
    def perform_another_transaction(self):
        response = input("\nDo you want to perform another transaction (y/n): ")
        if response == "y" or response == "Y":
            self.function()
        elif response.lower() == "n":
            print("Thank you for banking with us.")

    # BVN Generator.
    @classmethod
    def bvn_generator(cls):
        from random import randrange
        bvn = randrange(1000, 1000000)
        return bvn

# George = Customer("Moses", 20120612060, 1034,)
# George.function()
