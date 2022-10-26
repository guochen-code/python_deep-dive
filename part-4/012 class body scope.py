class Account:
  COMP_FREQ=12
  APR=0.02
  APY=(1+APR/COMP_FREQ) ** COMP_FREQ -1 # this work because APR and COMP_FREQ are symbols in the same class body namespace
  
  def __init__(self,balance):
    self.balance=balance
  
  def monthly_interest(self):
    return self.balance * self.APY.     # this works because we used self.APY
  
  @classmethod
  def monthly_interest_2(cls,amount):
    return amount * cls.APY              # this works because we used cls.APY
  
  @staticmethod
  def monthly_interest_3(amount):
    return amount * Account.APY          # this works because we used Account.APY
  
  def monthly_interest_3(self):
    return self.amount * APY             # this will fail if APY is not defined in this function's scope or in any enclsing scope
                                         # beware: this can produce subtle bugs!! if you have APY in the module
# "monthly_interest_3" looks into the module namespace rather than the class namespace
# so cannot find APY
