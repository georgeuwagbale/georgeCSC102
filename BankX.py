
class XBank:
    loggedinCounter = 0
    def __init__(self,theATMpin,theAccountbalabce,theName):
        self.theATMpin = theATMpin
        self.theAccountbalabce = theAccountbalabce
        self.theName = theName
        XBank.loggedinCounter +=1

 #   def CollectMoney(self,amountto):
