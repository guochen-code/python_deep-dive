class MyClass:
  pass

m = MyClass()
type(m), m.__class__ -> (__main__.MyClass, __main__.MyClass)

class MyClass:
  __class__ = str
m= MyClass()
m.__class__, type(m) -> (str,__main__.MyClass)

# so it is safer to use type
# instance is a little bit different
m = MyClass()
isinstance(m,MyClass) -> True
isinstance(m,str) -> True

# in general don;t use the __class__ because that gets to be problematic unless you know exactly what you are doing

