slots

----- memory savings, enven compared to sharing dictionaries, can be substantial

class Point:
  def __init__(self,x,y):
    self.x=x
    self.y=y
    
class Point:
  __slots__=('x','y')
  def __init__(self,x,y):
    self.x=x
    self.y=y
    
10,000 instances: 1,729KB vs 635KB
  
isn't creating that many instances of an object rare?
  -> depends on your program
  -> example: returning multiple rows from a database and putting each row into an object
  -> use slots in cases where you know you will benefit substantially
  
----- speed
using slots reuslts in generally faster operations (on average)

class PersonDict:
  pass

class PersonSlots:
  __slots__=('name',)

def manipulate_dict():
  p=PersonDict()
  p.name='jhon'
  p.name
  del p.name
  
def manipulate_slots():
  p=PersonSlots()
  p.nmae='jhon'
  p.name
  del p.name

timeit(manipulate_dict)
timeit(manipulate_slots) -> about 30% faster

-------- if better in terms of memory and speed, why not use slots all the time?
if we use slots, we cannot add attributes to our objects that are not defined in slots

class Point:
  __slots__=('x','y')
  def __init__(self,x,y):
    self.x=x
    self.y=y
    
p=Point(0,0)
p.z=100
setattr(p,'z',100) -> AttributeError: 'Point' object has no attribute 'z'
  
-> can cause difficulties in multi-inheritance

*********************************************************************************************************************************************

use slots, we can delete attributes
p=Point(1,2)
del p.X -> ok

and can reset it back
p.X=10 -> ok


class Location:
  __solots__='name,'_longitude','_lattitude'
  
  def __init__(self,nmae,*longitude,latitude):
    self._longitude = longitude
    self._latitude=latitude
    self.name=name
    
  @propery
  def longitude(self):
    return self._longitude
  
  @property
  def latitude(self):
    return self._latitude

del l.longitude -> AttributeError: can't delete attribute # because didnot define deleter method for the longitude !!!!!!!!!!!!!
del l._longitude -> ok

l.__dict__ -> 'Location' object has no attribute '__dict__' # when use slots, we lose dictionary.......
*********************************************************************************************************************************************

the best of both worlds
slots -> faster attribute access, less memory
instance directionary -> can add attributes arbitrarily at run-time

-> can we do both> -> yes!
-> specify __dict__ as a slot

class Person:
  __solots__ = 'name', '__dict__'
  
p.name = 'Alex'
p.age = 18
p.__dict__ -> {'age':18}

