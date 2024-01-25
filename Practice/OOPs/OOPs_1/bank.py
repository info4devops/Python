# write a program to demonstrate basi bank functionality using class, variable & methods

import sys
class Customer:
    Bank_name = 'ABC Bank'

    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance

    def deposite(self,amount):
        self.balance = self.balance +amount
        print('Balance after deposite:', self.balance)

    def withdraw(self,amount):
        if amount > self.balance:
            print('Insufficient fund, Unable to process your request')
            sys.exit()
        self.balance = self.balance - amount
        print('Balance after withdraw:', self.balance)


print('Welcome to', Customer.Bank_name)
name = input('Enter your name:')
c = Customer(name)

while True:
    print('d-Deposit\nw-Withdraw\ne-Exit')
    option = input('Choose your option: ')
    if option == 'd' or option == 'D':
        amount = float(input('Enter amount: '))
        c.deposite(amount)
    elif option == 'w' or option == 'W':
        amount = float(input('Enter amount: '))
        c.withdraw(amount)
    elif option.lower() == 'e':
        print('Thanks for Banking with us')
        sys.exit()
    else:
        print('Invalid Option, Please choose valid option')
