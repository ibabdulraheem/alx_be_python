class BankAccount:
  def __init__(self,account_balance):
    self.account_balance = account_balance


  def deposit(self,amount):
    self.amount = amount
    self.account_balance += self.amount
    return(f"Deposited: ${amount} ")
  def withdraw(self,amount):
    self.amount = amount
    if self.account_balance == 0:
       return(f"Your Account is zero")
    elif self.account_balance < self.amount:
      return("Insufficient funds.")
    else:
      return(f"withdrew: ${self.amount}")
  def display_balance(self):
      return(f"Current Balance: ${self.account_balance} ")

