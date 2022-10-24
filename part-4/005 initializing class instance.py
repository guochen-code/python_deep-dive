important !!!

by the time __init__ is called
  python has already created the object and a namespace for it (like a __dict__ in most cases)
  then __init__ is called as a method bound to the newly created instance

we actually can specify a custom function to create the object
  __new__
  90% of the time we don;t use and don't override the __new__ method
  
in summary: __init__ is not creating the object, it is only running some code after the instance has been created.
  
__init__ is an instance method, because object is already created before its call

example:
class Person:
  def __init__(self):
    print('fInitializing a new Person object: {self}')

p = Person() -> Initializing a new Person object: <__main__.Person object at 0x7ff590219400>
# the __init__ method was called automatically and it was bound to this object p

class Person:
  def __init__(self,name):
    self.name = name
p = Person('Eric')
p.__dict__ -> {'name': 'Eric'}
# same as below, just make all steps below automatically called and done in one step if we use this special method !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Person:
  def init(self,name):
    self.name = name    
p = Person()
p.__dict__ -> {}
p.init('Eric')
p.__dict__ -> {'name': 'Eric'}

