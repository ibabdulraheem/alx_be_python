class BankAccount:
  def __init__(self,account_balance):
    self.account_balance = account_balance

  def deposit(self,amount):
    self.amount = amount
    self.account_balance += self.amount
    return (f" Deposited: ${self.account_balance}" )
  
  def withdraw(self,amount):
    self.amount = amount
    if self.account_balance == 0 or self.account_balance < self.amount:
       print("Insufficient funds.")
    elif self.account_balance >= self.amount:
      self.account_balance -= self.amount
      return self.account_balance
  
  def display_balance(self):
    print( "Current Balance: ", {self.account_balance} )













    

  