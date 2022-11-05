class Account:
  apr=3.0
  
  def __init__(self,account_number,balance):
    self.account_number=account_number
    self.balance=balance
    self.account_type='Generic Account'
    
  def calc_interest(self):
    return f'Calc interest on {self.account_type} with APR = {self.__class__.apr}'
  
class Savings(Account):
  apr =5.0
  
  def __init__(self,account_number, balance):
    self.account_number=account_number
    self.balance=balance
    self.account_type='Savings Account'
