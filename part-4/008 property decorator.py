# why use property decorator: to simplify the code getter and setter
# why use getter and setter -> private attribute
# why use private attribute? don't want to be modified?
# why not be modified?

class Person:
  def __init__(self,name):
    self._name = name
  
  def name(self):
    print('getter called...')
    return self._name
  
  name=property(name) # it reminds you decorator. func = decorator(func)

# same as above

class Person:
  def __init__(self,name):
    self._name = name
  
  @property
  def name(self):
    print('getter called...')
    return self._name
# what actually happen: 
# creating a property object and then use decorator syntax to redefine the function name
# but the function name to redefine that now as a property

**********************
p = property(get_prop)
p = p.setter(set_prop)
p = p.deleter(del_prop)

def name(self):
  print('getter....')
hex(id(name)) -> '0x7f84f020b158'
name = property(name)
type(name), hex(id(name)), hex(id(name.fget)) ->
(property, '0x7f84e81f06d8', '0x7f84f020b158')

name_temp = name

def name(self,value):
  print('setter...')

type(name),hex(id(name)) ->
(function, '0x7f84f0453c80')

name = name_temp.setter(name)
type(name), hex(id(name)), hex(id(name.fget)), hex(id(name.fset)) ->
(property, '0x7f84e81f2318', '0x7f84f020b158', '0x7f84f0453c80')

# reminds decorator
class Person:
  def __init__(self,name):
    self._name = name
  
  @property
  def name(self):
    '''the person's name'''
    return self._name
  
  @name.setter
  def name(self, value):
    self._name = value 
    
help(Person.name) -> the person's name
# if you set doc string in setter above, it will not work

******* what if only want setter, no getter
******* how to set doc string in setter
(1)
class Person:
  def prop_set(self,value):
    print('setter called...')
  prop = property(fset=prop_set)
  
(2) 
class Person:
  prop=property(doc='write-only property'). # set up doc string here
  
  @prop.setter
   def prop_set(self,value):
    print('setter called...')
