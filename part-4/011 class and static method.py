# class methods

class MyClass:
  def hello():
    print('hello...')
    
  def inst_hello(self):
    print(f'hello from {self}')
    
  @classmethod
  def cls_hello(cls):
    print(f'hello from {cls}')

                      MyClass                     Instance
hello              regular function             method bound to instance -> call will fail (by default, any function defined in a class will be handled as a bound method when called from an instance
inst_hello          regular function              method bound to instance
cls_hello          method bound to class            method bound to class

# static methods
# a function in a class that will never be bound to any obkect when called

class Circle:
  @staticmethod
  def help():
    return 'help available'                                                                       
c = Circile()
Cirucle.help() -> help available
c.help() -> help available   
                                                                                            
in summary
(1) function bound to instance when called from instance - will receive instance as first parameter
(2) function bound to class when called from either the class or the instance - will receive the class(MyClass) as first paramter
(3) static method is never bound to anything - receives no extra argument no matter how it is called
***************************************************************************************************************************************
# application
'''
why use static methods?
cases where it makes sense for a function to live in a class
  but does not need access to either the instance or the class state
  
Timer
  start(self)   -> instance method
  end(self)     -> instance method
  timezone      -> class attribute -> allow us to modify time zone for all instances
  current_time_utc()    -> static method
  current_time(cls)     -> class method(needs class time zone)
'''
                                                                                            
                                                                                            
                                                                                            
                                                                                            
                                                                                            
