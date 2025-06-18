class BankAccount:
  def __init__(self,account_balance):
    self.account_balance = account_balance

  def deposit(self,amount):
    self.account_balance += amount
    print(f"Deposited: ${amount} ")
  def withdraw(self,amount):
    if self.account_balance == 0:
       print(f"Your Account is zero")
    elif self.account_balance < amount:
      print ("Insufficient funds.")
    elif self.account_balance >= amount:
      self.account_balance -= amount
      print(f"withdrew: ${amount}")
  def display_balance(self):
      print( f"Current Balance: ${self.account_balance} ")
