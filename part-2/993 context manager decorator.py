so far we saw how to create a context manager using a class and a generator function

using a decorator to encapsulate these steps:
  (1) gen = gen_func(args)
  (2) with GenContextManager(gen):
        ...
      
def contextmanager_dec(gen_fn):
  def helper(*args,**kwargs):
    gen = gen_fn(*args,**kwargs)
    return GenContextManager(gen)
  return helper

class GenContextManager:
  def__init__(gen_obj):
    self.gen=gen_obj
  def __enter__(self):
    return next(self.gen)
  def __exit__(self,...):
    next(self.gen)
    
    
