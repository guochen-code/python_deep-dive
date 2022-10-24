# we saw that we can add to an instance namespace directly at runtime by using setattr or the dot notation
# example:
class MyClass:
  language = 'Python'
  
obj = MyClass()
obj.version = '3.7'
obj.__dict__ -> {'version': '3.7'}

# what happen if we create a new attribute whose value is a function?
obj.say_hello = lambda : 'Hello World!'
# then
obj.say_hello -> function # not a bound method!
obj.say_hello() -> 'Hello World!'
# but say_hello does not have access to the instance namespace
# say_hello function does not receive the object because it is not bound to it, so we don't have access to the object inside the lambda function.(see below application)

********************************************************************* # can we create and bind a method to an instance at runtime? !!!!!!!!!!!!
# just need to define a method that binds the function to the instance

class MyClass:
  language = 'Python'
obj = MyClass()

from types import MethodType  # MethodType(function,object) # function we want to bind, the object to bind to

obj.say_hello = MethodType(lambda self: f'Hello {self.language}!', obj)

# say_hello is now a method bound to obj
# only obj has been affected. if I have another instance of MyClass, it hasn't been affected !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# just modify the namespace for this specific instance
# no other instances have that method !!!!!!!!!!!!!!

********************************************************************* application
class MyClass:
  language = 'Python'
  
obj = MyClass()
obj.say_hello = lambda : f'{self.language} Hello World!'
obj.say_hello() -> NameError: name 'self' is not defined # don't have access to the object inside the lambda function
  
from types import MethodType
obj.say_hello = MethodType(lambda self : f'{self.language} Hello World!', obj)
obj.say_hello() -> 'Python Hello World!'

********************************************************************* extended application
we have different implementations for different instances, but we are still calling them the same way. It is kind of idea of plug in 
# we CAN achieve this using inheritance or maybe using masterclasses and so on. but these things get really complicated sometime.
# this is a nice application of creating your own methods and adding them to instances at runtime, essentially monkey patching your instances with these custom 
# boud methods

from types import MethodType

class Person:
  def __init__(self,name):
    self.name=name
    
  def register_do_work(self,func):
    setattr(self,'_do_work',MethodType(func,self))
    
  def do_work(self):
    do_work_method = getattr(self,'_do_work',None)
    
    if do_work_method:
      return do_work_method()
    else:
      raise AttributeError('You must first register a do_work method.')
      
  
