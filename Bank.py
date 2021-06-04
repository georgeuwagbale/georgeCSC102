class Bank:
    def __init__(self, name, account_number, pin):
        self.name = name
        self.account_number = account_number
        self.pin = pin
        self.account_type = "dollar"
        self.account_balance = 500000
        self.transaction = {
            "Debit": [],
            "Credit": []
        }

    def change_pin(self):
        old_pin = int(input("Input old pin: "))
        if old_pin == self.pin:
            new_pin = int(input("Input new pin: "))
            self.pin = new_pin
            print( "You have successfully changed your password")

    def deposit(self):
        balance = float(input("How much do you want to deposit: "))
        self.account_balance += balance
        self.transaction.get("Credit").append(balance)
        #return f"Account Balance: {self.account_balance}"
        self.alert(message="credit", transaction_amount=balance)

    def withdrawal(self):
        trial = 3
        while trial != 0:
            request_pin = int(input('Pin: '))
            if request_pin == self.pin:
                withdrawal = float(input("Pin correct.\nHow much do you want to withdrawal: "))
                self.account_balance -= withdrawal
                self.transaction.get("Debit").append(withdrawal)
                #return f"Debit of {withdrawal}; Account Balance: ${self.account_balance}"
                self.alert(message="debit", transaction_amount=withdrawal)
                break
            else:
                print("Pin is incorrect, try again.")
            trial -=1

    def transfer(self):
        amount = float(input("Amount: "))
        account = int(input("Recipient's Account number: "))
        bank = input("Recipient's bank: ")
        pin = int(input("Input your pin to verify: "))
        trial = 3
        while trial != 0 :
            if pin == self.pin:
                print("Transaction successful")
                self.alert("debit", amount)
            else:
                print("Incorrect pin, try again")
            trial -=1



    def statement_of_account(self):
        for transactions in self.transaction.keys():
            print(self.transaction.get(transactions))

    def function(self):
        print("\t\t\tWELCOME TO BANK-X \n")
        print("Enter '1' to Deposit \n Enter '2' to Withdrawal \n Enter '3' to Change of Pin \n Enter '4' to get a statement of account")
        print("Enter '5' to view your profile")
        try:
            response = int(input("What transaction do you want to perform: "))

            if response == 1:
                return self.deposit()
            elif response == 2:
                return self.withdrawal()
            elif  response == 3:
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

    def alert(self, message, transaction_amount):
        revised_account_number = str(self.account_number)
        coded_account_number = revised_account_number[0:3] + "****" + revised_account_number[8:]
        if message == "debit":
            print(f"Debit\n Amount: {transaction_amount} \n Account: {coded_account_number} \n Balance: ${self.account_balance}")
        elif message == "credit":
            print(f"Credit\n Amount: {transaction_amount} \n Account: {coded_account_number} \n Balance: ${self.account_balance}")

    def profile(self):
        print(f"\nName: {self.name} Account Number: {self.account_number}")
        print(f"Account Balance: ${self.account_balance} Account Type: {self.account_type}")

    def __str__(self):
        return f"Name: {self.name}; Account Number: {self.account_number}; Account Balance: ${self.account_balance}"


George = Bank("George", 20120612030, 1234)
George.function()



