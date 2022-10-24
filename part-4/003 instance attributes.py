class MyClass:
  language = 'python'

my_obj = MyClass()

MyClass.__dict__ -> {'language':'python'}
my_obj.__dict__ -> {}

my_obj.language -> 'python'
# it first looks into instance namespace, not found, it will go to class namespace, found it.

# so it is important to distinguish the class attributes (common attributes to all instances) and instance (specific) attributes.

type(MyClass.__dict__) -> mappingproxy # not mutable
type(my_obj.__dict__) -> dict # mutable

