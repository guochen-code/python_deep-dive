what is the caveat of inheritance of class?
typical of the built-in types. when you inherit from the built-in types, there is no gurantee that the built-in types 
when it does other functions and the built-in type will actually use these methods.
**************************************************************************************
# application:
# a dict that only allows certain types of keys (strings keys only -> JSON)
# a dict that only allows keys from some finite set of pre-defined keys
# a dict that only allows numerical values

# why use ????????????????????????
collections.UserDict
# python written in C, if use normal dict class, caveat when in inheritance, even if you override parent methods, prgoram still goes to C
# while, UserDict is written in python, so it is good in inheritance. it is not a dict, but is a mapping type
# example:
'abc'.__len__() # has this method
len('abc') # run this, does not guarantee that it use above method, it goes to C code which is faster to find length
# so when you inherit from built-in types, it does not gurantee the built-in types will use these special python methods.
# that's why user dict is created!!!!!!!!
d['a'] -> 10
d.get(a) -> 10.5 # get method doesnot use our new getitem defined in child class
d1={}
d1.update(d) 
d1 -> {'a':10.5} # it did not use our getitem to get the values, same as above

type(d) -> __main__.IntDict
d.update({'c':100.5})
d['c'] -> 100 # ok
d.update({'d':'python'} -> no error!!!!!!! not what we expect!!!!
d['d'] -> ValueError: invalid literal for int() with base 10: 'python'
         
class IntDict(dict):
  def __setitem__(self,key,value):
    if not isinstance(value,Real):
      raise ValueError('Value must be a real number.')
    super().__setitem__(key,value) # delegate back to the parent class
    
  def __getitem__(self,key):
    return int(super().__getitem__(key)) # delegate back to the parent class
******************************************************************************************************************************************
# just use UserDict here, everything other than that is the same..........
class IntDict(UserDict):
  def __setitem__(self,key,value):
    if not isinstance(value,Real):
      raise ValueError('Value must be a real number.')
    super().__setitem__(key,value) # delegate back to the parent class
    
  def __getitem__(self,key):
    return int(super().__getitem__(key)) # delegate back to the parent class
  
******************************************************************************************************************************************
# application, limit keys and values
class LimitedDict(UserDict):
  def __init__(self,keyset,min_value,max_value,*args,**kwargs):
    self._keyset=keyset
    self._min_value=min_value
    self._max_value=max_value
    super.()__init__(*args,**kwargs)
  
  def__setitem__(self,key,value):
    if key no in self._keyset:
      raise KeyError('Invalid key name.')
    if not isintance(value,int):
      raise ValueError('Value must be an integer type')
    if value<self._min_value or value > self._max_value:
      raise ValueError(f'Value must be between {self._min_value} and {self._max_value})
    super().__setitem__(key,value)
 
d = LimitedDict({'red','gree','blue'},0,255,red=10,green=10,blue=10)

d = LimitedDict({'red','gree','blue'},0,255,yellow=10) -> error
# actually super() also use this new setitem method, so this new setitem method override parent class and child class
# that's how inheritance works                       
                       
