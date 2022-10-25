# area is a computed property, every radius has its area.....
# if you need to access area 1000 times, you don't want to calculate it 1000 times
# you would like to cache it

class Circle:
  def __init__(self,radius):
    self._radius = radius
    self._area = None
    
  @property
  def radius(self):
    return self._radius
  
  @radius.setter
  def radius(self,value):
    self._area = None # validate cache
    self._radius = value
    
  @property
  def area(self):
    if self._are is None:
      print('calculating area...')
      self._area = pi * (self.radius**2) # not use self._radius: return abs(self._radius) when sb put negative value. use getter can make sure it is positive.
    return self._area # if not None, return cache value
  
# this is example we use getter and setter to do more than validation, 

# lazy attributes/properties

