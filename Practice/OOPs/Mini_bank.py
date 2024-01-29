class Account:
  def __init__(self,name,balance,min_balance):
    self.name=name
    self.balance=balance
    self.min_balance=min_balance
  def deposit(self,amount):
    self.balance=self.balance+amount
  
  def withdraw(self,amount):
    if self.balance-amount>=self.min_balance:
      self.balance=self.balance-amount
    else:
      print('Sorry,Insufficient Funds')
  
  def PrintStatement(self):
    print('Account Balance:',self.balance)
    
class Current_Account(Account):
  def __init__(self,name,balance):
    super().__init__(name,balance,-1000)
  def __str__(self):
    return '{}s Current account with Balance:{}'.format(self.name,self.balance)

class Savings_Account(Account):
  def __init__(self,name,balance):
    super().__init__(name,balance,0)
  def __str__(self):
    return '{}s Avaings account with Balance:{}'.format(self.name,self.balance)
  
print(':::::::Savaings Account transactions::::::::')
s=Savings_Account('Virat',10000)
print(s)
s.deposit(1000)
s.PrintStatement()
s.withdraw(9989)
s.PrintStatement()
print(s)
print()

print(':::::::Current Account transactions::::::::')
c=Current_Account('Virat',10000)
print(c)
c.deposit(100)
c.PrintStatement()
c.withdraw(976)
c.PrintStatement()
print(c)