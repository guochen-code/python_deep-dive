class MyClass:
  def __init__(self,language):
    self._language = language
  
  def get_language(self):
    return self._language
  
  def set_language(self,value):
    self._language = value
    
  language = property(fget=get_language, fset=set_language)
  
m = MyClass('Python')              m.__dict__ -> {'_language': 'Python'}
m.language='Java'                  m.__dict__ -> {'_language': 'Java'}
  
# language is not in m.__dict__
# remember how python looks for attributes:
  searches instance namespace first
  but also looks in class namespace
    finds language which is property object that has get and set accessors
