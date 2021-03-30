class BankAccount:
  def __init__(self):
    self.balance = 0

  def deposit(self, amount):
    if(0 > amount):
      return False
    self.balance += amount
    return f'Your balance is {self.balance}'

  def withdraw(self, amount):
    if(0 > amount):
      return False
    self.balance -= amount
    return f'Your balance is {self.balance}'

  def accumulate_interest(self):
    self.balance += (self.balance * .02)
    return f'Your balance is {self.balance}'

class ChildrensAccount(BankAccount):
  def accumulate_interest(self):
    self.balance += 10


class OverdraftAccount(BankAccount):
  def __init__(self):
    super().__init__()
    self.overdraft_penalty = 40
  def withdraw(self, amount):
    if(amount > self.balance):
      self.balance -= self.overdraft_penalty
      return False
  def accumulate_interest(self):
    if(0 > self.balance):
      return False

try:
  basic_account = BankAccount()
  basic_account.deposit(600)
  print("Basic account has ${}".format(basic_account.balance))
  basic_account.withdraw(17)
  print("Basic account has ${}".format(basic_account.balance))
  basic_account.accumulate_interest()
  print("Basic account has ${}".format(basic_account.balance))
  print()
except Exception as e:
  print(e)

try:
  childs_account = ChildrensAccount()
  childs_account.deposit(34)
  print("Child's account has ${}".format(childs_account.balance))
  childs_account.withdraw(17)
  print("Child's account has ${}".format(childs_account.balance))
  childs_account.accumulate_interest()
  print("Child's account has ${}".format(childs_account.balance))
  print()
except Exception as e:
  print(e)
  

try:
  overdraft_account = OverdraftAccount()
  overdraft_account.deposit(12)
  print("Overdraft account has ${}".format(overdraft_account.balance))
  overdraft_account.withdraw(17)
  print("Overdraft account has ${}".format(overdraft_account.balance))
  overdraft_account.accumulate_interest()
  print("Overdraft account has ${}".format(overdraft_account.balance))
except Exception as e:
  print(e)
