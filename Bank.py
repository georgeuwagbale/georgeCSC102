class Bank:
    def __init__(self, name, account_number, pin):
        self.Name = name
        self.Account_number = account_number
        self.pin = pin
        self.account_balance = 0
        self.transaction = {
            "Debit":[],
            "Credit":[]
        }

    def change_pin(self, new_pin):
        self.pin = new_pin
        return "You have successfully changed your password"

    def deposit(self):
        balance = float(input("How much do you want to deposit: "))
        self.account_balance += balance
        self.transaction.get("Credit").append(balance)
        return f"Account Balance: {self.balance}"

    def withdrawal(self):
        withdrawal = float(input("How much do you want to withdrawal: "))
        request_pin = int(input('Pin: '))
        if request_pin == self.pin:
            self.account_balance -= withdrawal
            self.transaction.get("Debit").append(withdrawal)
            return f"Debit of {withdrawal}; Account Balance: ${self.account_balance}"
        else:
            return "Password is incorrect"


    #def statement_of_account(self):


    def __str__(self):
        return f"Name: {self.Name}; Account Number: {self.Account_number}; Account Balance: ${self.account_balance}"



George = Bank("George", 20120612030, 1234)


