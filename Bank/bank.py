class account():
    def __init__(self, balance):
        self.balance = balance

    def getBalance(self):
        return float(self.balance)

    def deposit(self, balance):
        depo = float(balance)
        bal = self.balance + depo
        self.balance = bal

    def withdraw(self,balance):
        withd = float(balance)
        wd1 = self.balance - withd
        self.balance = wd1

class customer():
    def __init__(self,firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.account = None
    def getFirstName(self):
        return self.firstName
    def getLastName(self):
        return self.lastName
    def getAccount(self):
        return self.account
    def setAccount(self, balance):
        self.account = account(balance)

class bank():
    def __init__(self, bankname):
        self.customers = []
        self.numberofcustomers = 0
        self.bankename = bankname

    def getBankname(self):
        return self.bankename

    def addCustomer(self, firstName, lastName):
        self.customers.append(customer(firstName, lastName))

    def getNumOfCustomers(self):
        self.numberofcustomers = len(self.customers)
        return self.numberofcustomers

    def getCustomer(self, index):
        return self.customers[index]

