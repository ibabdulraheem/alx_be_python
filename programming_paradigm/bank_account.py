class BankAccount:
  def __init__(self,account_balance):
    self.account_balance = account_balance

  def deposit(self,amount):
    self.amount = amount
    self.account_balance += self.amount
    print(f"Deposited: ${self.amount} ")
  
  def withdraw(self,amount):
    self.amount = amount
    if self.account_balance == 0:
       print(f"Your Account is zero")
    elif self.account_balance < self.amount:
      print ("Insufficient funds.")
    elif self.account_balance >= self.amount:
      self.account_balance -= self.amount
      print(f"withdrew: ${amount}")
  def display_balance(self):
      print( f"Current Balance: ${self.account_balance} ")
account = BankAccount(1000)
account.display_balance()
account.deposit(1500)
account.display_balance()
account.withdraw(1200)
account.display_balance()

