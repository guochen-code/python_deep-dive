'''
in python, everything is object
object is a class
dict(object) -> default dunder methods: __eq__, __hash__ etc.......

as soon as you implement __eq__, python takes away the default __hash__. Because __hash__ use identity, so was __eq__.
Now p1==p is True, but p1 is not p2, so p1==p2, not same hash, not possible.
so need to implement own __hash__
'''

class Person:
  def __init__(self,name):
    self._name=name
    
  @property
  def name(self):
    return self._name
  
  def __eq__(self,other):
    return isinstance(other,Person) and self,name == other.name
  
  def __hash__(self):
    return hash(self.name)
  
  def __repr__(self):
    return f'Person(name='{self.name}')'
  
