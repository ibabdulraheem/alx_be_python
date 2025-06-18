class BankAccount:
  def __init__(self,account_balance):
    self.account_balance = account_balance


  def deposit(self,amount):
    self.amount = amount
    self.account_balance += self.amount
    return(f"Deposited: ${amount} ")
  def withdraw(self,amount):
    self.amount = amount
    if self.account_balance == 0 or self.account_balance < self.amount:
       return("Insufficient funds.")
    elif self.account_balance > self.amount:
      self.account_balance -= self.amount
      return(f"withdrew: ${self.amount}")
    else:
      return("Invalid Transaction!")
  def display_balance(self):
      return(f"Current Balance: ${self.account_balance} ")

