class MyClass:
  def say_hello():
      print('hello world!')
      
my_obj = MyClass()
      
MyClass.say_hello() -> 'hello world!'
my_obj.say_hello() -> TypeError: say_hello() takes 0 positional arguments but 1 was given
  
# what happened?
# method is an actual object type in python, like a function, it is callable
# but unlike a function it is bound to some object, and that object is passed to the method as its first parameter

# methods are onjects that combine:
  -- instance (of some class)
  -- function
# like any object it has attributes:
__self__ -> the instance the method is bound to
__func__ -> the original function (defined in the class)

obj.method(args) -> method.__func__(method.__self__, args) 

*****
class MyClass:
  language = 'python'
  
  def say_hello(obj, name):
    return f'hello {name}! I am {obj.language}.'
  
python = MyClass()
python.say_hello('John') -> MyClass.say_hello(python, 'john') # equivalent

