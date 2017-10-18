from bank import *

bank1 = bank("Samsung")
print ("welcome to " + str(bank1.getBankname()))
while True:
    print ("[1]Create an account\n[2]See total Customers\n[3]see customer detail")
    selection = int(input())
    if selection==1:
        fn=input("First name = ")
        ln=input("Last name = ")
        bank1.addCustomer(fn, ln)
        bank1.getCustomer(bank1.getNumOfCustomers()-1).setAccount(1000)
    elif selection==2:
        print (bank1.getNumOfCustomers())

    elif selection==3:
        for i in range(bank1.getNumOfCustomers()):
            print (str(i+1) + " " + bank1.getCustomer(i).getFirstName())
        inp = int(input('Which customer do you want to see their detail: \n'))
        print('First Name: ' + bank1.getCustomer(inp-1).getFirstName())
        print('Last Name: ' + bank1.getCustomer(inp - 1).getLastName())
        print('Balance: ' + str(bank1.getCustomer(inp - 1).getAccount().getBalance()))
        print("Do you want to deposit/withdraw?")
        depowd= int(input("[1]Deposit\n[2]Withdraw\n"))
        if depowd==1:
            depo = float(input("How much do you want to deposit?\n"))
            bank1.getCustomer(inp - 1).getAccount().deposit(depo)
            print ("Balance Updated!")
        elif depowd==2:
            wd = float(input("How much do you want to withdraw?\n"))
            bank1.getCustomer(inp - 1).getAccount().withdraw(wd)
            print ("Cash withdrawn")