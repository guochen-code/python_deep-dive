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
    
    
usage example

@contextmanager_dec
def open_file(f_name):
  f=open(f_name)
  try:
    yield f
  finally:
    f.close()
    
open_file=contextmanager_dec(open_file)
  -> open_file is now actually the helper closure
  
calling open_file(f_name)
  -> calls helper(f_name)             [free variable gen_fn=open_file]
    -> creates the generator object
    -> returns GenContextManager instance
  -> with open_file(f_name)
