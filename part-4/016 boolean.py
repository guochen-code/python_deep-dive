'''
every object in python has an associated truth(boolean) value
  any non-zero number -> True otherwise False(i.e if equal to0)
  an empty collection (len() is 0) -> False otherwise True
  
by default, any custom object also has a truth value
  -> can override this by defining the __bool__ method -> must return True/False !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    -> if __bool__ is not defined
        -> python looks for __len__ 0 -> False, anything else will be True
        -> if neither present, always returns True
'''


class Point:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  
p1=Point(0,0)
p2=Point(1,1)
bool(p1), bool(p2) -> (True,True)

class Point:
  def __init__(self,x,y):
    self.x=x
    self.y=y
    
  def __bool__(self):
    return self.x!=0 or self.y!=0
  
bool(p1), bool(p2) -> (False,True)

# alternatively
bool(p1.x or p1.y) -> false
bool(p2.x or p2.y) -> True

# must return True/False !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Point:
  def __init__(self,x,y):
    self.x=x
    self.y=y
    
  def __bool__(self):
    return self.x or self.y # not working. TypeError: __bool__ should return bool, return int
  
 class Point:
  def __init__(self,x,y):
    self.x=x
    self.y=y
    
  def __bool__(self):
    return bool(self.x or self.y) #  this will work
