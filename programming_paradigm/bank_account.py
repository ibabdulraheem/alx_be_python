class BankAccount:
  def __init__(self,account_balance,amount):
    self.account_balance = account_balance
    self.amount = amount

  def deposit(self,amount):
    self.amount = amount
    self.account_balance += self.amount
    return(f"Deposited: ${amount} ")
  def withdraw(self,amount):
    self.amout = amount
    if self.account_balance == 0:
       return(f"Your Account is zero")
    elif self.account_balance < self.amount:
      return("Insufficient funds.")
    elif self.account_balance >= self.amount:
      self.account_balance -= self.amount
      return(f"withdrew: ${self.amount}")
  def display_balance(self):
      return(f"Current Balance: ${self.account_balance} ")
account = BankAccount(100,50)
