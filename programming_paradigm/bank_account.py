class BankAccount:
  def __init__(self,account_balance = 0):
    self.account_balance = account_balance

  def deposit(self,amount):
    self.amount = amount
    self.account_balance += self.amount
    print(f" Deposited: ${self.account_balance}" )
  
  def withdraw(self,amount):
    self.amount = amount
    if self.account_balance == 0:
       print(f"Your Account is: {self.account_balance}")
    elif self.account_balance < self.amount:
      print ("Insufficien funds.")
    elif self.account_balance >= self.amount:
      self.account_balance -= self.amount
      print(f"withdrew:, ${float(self.account_balance)}")
  def display_balance(self):
      print( f"Current Balance: ${float(self.account_balance)}" )

my_account = BankAccount(250)
print(my_account.display_balance())
my_account.deposit(50)
my_account.display_balance()
my_account.withdraw(2000)
my_account.display_balance()












    

  