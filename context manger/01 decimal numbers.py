import decimal

decimal.getcontext() -> Context(prec=28,rounding=Round_HALF_EVEN, .....)

deciaml.getcontext().prec = 14 # can change 

# change decimal numbers application
# without context manager, you need to remember when you change and when to change it back
deciaml.getcontext().prec = 14
old_prec=decimal.getcontext().prec
decimal.getcontext().prec=4 # set a new prec
print(decimal.Decimal(1)/decimal.Decimal(3)) -> 0.3333
decimal.getcontext().prec=old_prec # remember to reset it back
print(decimal.Decimal(1)/decimal.Decimal(3)) -> 0.33333333333333

# above method is error-prone, easy to forget to reset 
class precision: # lowercase, because it actis like a function
  def __init__(self,prec):
    self.prec=prec
    self.current_prec=decimal.getcontext().prec
    
  def __enter__(self):
    decimal.getcontext().prec=self.prec
    
  def __exit__(self,exc_type,exc_value,exc_tb):
    decimal.getcontext().prec=self.current_prec
    return False
  
with precision(3):
  print(decimal.Decimal(1)/decimal.Deciaml(3)) -> 0.333
print(decimal.Decimal(1)/decimal.Deciaml(3)) -> 0.3333333333333333333333333333

# built-in context manager
with decimal_localcontext() as ctx:
  ctx.prec = 3

  










