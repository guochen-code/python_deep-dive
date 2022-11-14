so far we saw how to create a context manager using a class and a generator function

using a decorator to encapsulate these steps:
  (1) gen = gen_func(args)
  (2) with GenContextManager(gen):
        ...

def gen(args):
  # setup happens herem or inside try
  try:
    yield obj # whatever normally gets returned by __enter__
  finally:
    # perform clean up code here
      
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

***************************************************************************************************************************************
(1) create generator function
def open_file(name,mode='r'):
  print('opening file...')
  f=open(fname,mode)
  try:
    yield f
  finally:
    print('closing file...')
    f.close()
    
(2) create context manager class
class GenContextManager:
  def__init__(self,gen):   # receive generator object. not function because want to create function within the decorator below
    self.gen=gen
  def __enter__(self):
    print('calling next to get the yielded value from generator')
    return next(self.gen)
  def __exit__(self,exc_type,exc_value,exc_tb):
    print('calling next to perform cleanup in generator')
    try:
      next(self.gen)
    exept StopIteration:
      pass
    return False

file_gen=open_file('test.txt','w')
with GenContextManager(file_gen) as f:
  f.writelines('Sir Spamlot')
  
**** create a decorator
def context_manager_dex(gen_fn): # receive generator function not object
  def helper(*args,**kwargs):
    gen=gen_fn(*args,**kwargs)
    ctx=GenContextManager(gen)
    return ctx
  return helper

***********************************
@context_manager_dec
def open_file(name,mode='r'):
  print('opening file...')
  f=open(fname,mode)
  try:
    yield f
  finally:
    print('closing file...')
    f.close()
*********************************** equivalent to writting this way: open_file=context_manager_dec(open_file)
  
# now open_file is our context manager
with open_file('test.txt') as f:
  print(f.readlines())
  
*********************************** python built-in take care of all above !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
from contextlib import contextmanager
@contextmanager
def open_file(name,mode='r'):
  print('opening file...')
  f=open(fname,mode)
  try:
    yield f
  finally:
    print('closing file...')
    f.close()
# this works to create a context manager out of a generator function

******************************************************************************************************************************************************
application-1: timer
# go back to context manager folder - timer.py
