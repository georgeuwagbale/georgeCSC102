class XBank:
    loggedinCounter = 0

    def __init__(self, theatmpin, theaccountbalance, thename):
        self.atmpin = theatmpin
        self.accountbalance = theaccountbalance
        self.name = thename
        XBank.loggedinCounter = XBank.loggedinCounter + 1

    def CollectMoney(self, amounttowithdraw):
        if (amounttowithdraw > self.accountbalance):
            print("Sorry we are not able to process at this time")
        else:
            print("Collect your cash....Thanks for banking with Xbank")

    def ChangePin(self, newPin):
        self.atmpin = newPin
        print("Your Pin has been changed...Thanks for banking with Xbank")

    def __str__(self):
        return f"Account Name: {self.name}  Account Balance: {self.balance}"

    @classmethod
    def NoOfCustomersLoggedin(cls):
        print("we have a total of" + str(cls.loggedinCounter) + " that have logged in")


f = open("Database.txt", 'r')

#print(f.readlines())
password = []
accountB = []
name = []
breaker = []
for x in f:
    breaker = x.split(' ')
    password.append(breaker[0])
    accountB.append(breaker[1])
    name.append(breaker[2])
    break

print("enter your pin........")

pasw = input()

if (pasw == password[0]):
    customer = XBank(password[0], accountB[0], name[0])
else:
    print("sorry your password does not match")
