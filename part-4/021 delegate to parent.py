# problem
class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
    
class Student(Pserson):
  def __init__(self,name,age,major):
    self.major=major
    self.name=name # repeat
    self.age=age # repeat, there has to be a better way!
    
# solution: delegating to parent
# delegation works its way up the inheritance (parent-grandparent-great grandparent)  until it finds what it needs

class Student:
  def __init__(self,name,age,major):
    super.().__init__(name,age)
    self.major=major # encouraged to do this way, if reverse these two lines, parent may override child if have sth in common
    

    
 
