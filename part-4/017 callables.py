'''
any object can be made to emulate a callable by implementing a __call__ method

class Person:
  def __call__(self,name):
    return f'Hello {name}'

p = Person()
p('Eric') -> p.__call__('Eric')  -> Eric

-> useful for creating function-like objects that need to maintain state
-> useful for creating decorator classes

'''

