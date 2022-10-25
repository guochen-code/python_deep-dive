# deleting property means deleting property from instance not from class
# it does not remove the property from the class !!!!!!!!!!!!!!!!!!!!!!!!!!!

c=Circle()
c.color='red'
c.color -> red

del c.color
c.color -> AttributeError
or
delattr(c,'color')
@prop_name.deleter

**********************************
class unitCircle:
  def __init__(self,color):
    self._color=color
    
  @property
  def color(self):
    return self._color
  
  @color.setter
  def color(self,value):
    self._color=value
    
  @color.deleter
  def color(self):
    del self._color
