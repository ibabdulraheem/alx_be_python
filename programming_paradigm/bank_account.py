class BankAccount:
  def __init__(self,account_balance):
    self.account_balance = account_balance


  def deposit(self,amount):
    self.amount = float(amount)
    self.account_balance += self.amount
    return(f"Deposited: ${amount} ")
  def withdraw(self,amount):
    self.amount = float(amount)
    if self.amount < self.account_balance:
      self.account_balance-= self.amount
      return(f"Withdrew: ${self.amount}")
    elif self.amount > self.account_balance or self.account_balance ==0:
      ("Insufficient funds.")
    else:
      return("Invalid command.")
  def display_balance(self):
     print ( f"Current Balance: ${self.account_balance:.2f}" )



  #   if self.account_balance > self.amount:
  #     self.account_balance -= self.amount
  #     return(f"withdrew: ${self.amount}")
  #   elif self.account_balance == 0 or self.account_balance < self.amount:
  #     self.account_balance -= self.amount
  #     return("Insufficient funds.")
  #   else:
  #     return("Invalid transaction!")
  # def display_balance(self):
  #     return(f"Current Balance: ${self.account_balance} ")

