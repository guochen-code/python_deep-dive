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
********************************************************************************************************************
major=0
minor=0
revision=1

def gen_class():
  major=0
  minor=4
  revision=2
  
  class Language:
    major=3
    minor=7
    revision=4
    
    #classmethod
    def version(cls):
      return'{}.{}.{}'.fomrat(major,minor,revision)
    
  return language

cls = gen_class()
cls.version() -> '0.4.2' # if remove 0.4.2 in source code, it will show '0.0.1'

import inspect
inspect.getclosurevars(cls.version) -> ........

********************************************************************************************************************

name = 'Guido'

class MyClass:
  name = 'Raymond'
  list_1 = [name]*3
  list_2 = [name for i in range(3)]
  
  @classmethod
  def hello(cls):
    return'{} says hellp'.format(name)
  
MyClass.hello() -> 'Guido says hello'

MyClass.list_1 -> ['Raymond','Raymond','Raymond']

MyClass.list_2 -> ['Guido','Guido','Guido']   # comprehensives(list/generator/set) are functions under the hood!!!!!!!
