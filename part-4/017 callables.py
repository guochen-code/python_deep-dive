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

from functools import partial
type(partial) ---> type

def my_func(a,b,c):
    return a,b,c
  
type(my_func) ---> function

partial_func=partial(my_func,10,20)
type(partial_func) ---> functools.partial
partial_func(30) ---> (10,20,30)

class Partial:
  def __init__(self,func,*args):
      self._func=func
      self._args=args
      
  def __call__(self,*args):
      return self._func(*self._args,*args)
    
partial_func=Partial(my_func,10,20)
type(partial_func) ---> __main__.Partial
partial_func(30) ---> (10,20,30)
type(Partial) ---> type

***********************************************************************************************************************************************************
# keep track number of requests, but the requested data not in dictionary/cache

from collections import defaultdict

def default_value():
  return 'N/A'

d=defaultdict(default_value)
d['a'] ---> 'N/A'

mis_counter=0

def default_value():
  global miss_counter
  miss_counter+=1
  return 'N/A'

d=defaultdict(default_value)

# it is working, but.....
# 2 problems:
(1) rely on global variable
(2) keep tracking different cache instances - miss_counter_1, miss_counter_2....... not good

------------------------------------------------------------------------------------------------------------------------------
def default_value(counter):
  counter+=1     # will create a local variable, not work # defaultdict cannot take any argument
  return 'N/A'
------------------------------------------------------------------------------------------------------------------------------
# try different approach

class DefaultValue:
  def __init__(self):
    self.counter=0
    
  def __iadd__(self,other):
    if isintance(other,int):
      self.counter+=other
      return self
    raise ValueError('Can only increment with an integer value.')
    
default_value_1=DefaultValue()
default_value_1.counter ---> 0
default_value_1+=1
default_value_1.counter=1

class DefaultValue:
  def __init__(self):
    self.counter=0
    
  def __iadd__(self,other):
    if isintance(other,int):
      self.counter+=other
      return self
    raise ValueError('Can only increment with an integer value.')
    
  def __call__(self):
    self.counter+=1
    return 'N/A'
  
def_1=DefaultValue()
def_2=DefaultValue()

cache_1=defaultdict(def_1) # (1) callable (2) has own counter
cache_2=defaultdict(def_2)

cache_1['a'], cache_1['b']
def_1.counter-->2
      
**********************************************  modified version 
class DefaultValue:
  def __init__(self,default_value):
    self.default_value=default_value
    self.counter=0
    
  def __call__(self):
    self.counter+=1
    return self.default_value 
**********************************************  make instances of our class callable, it is very useful, also useful to create decorator classes
although often use closure to create a decorator

for simplicity, only for function in module level, not instance level

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! how many times the function gets called and average of the execution time


from time import perf_counter
from functools import wraps

def profiler(fn):
    counter = 0
    total_elapsed = 0
    avg_time = 0
    
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal counter
        nonlocal total_elapsed
        nonlocal avg_time
        counter += 1
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        total_elapsed += (end - start)
        avg_time = total_elapsed / counter
        return result
    
    # we need to give a way to our users to look at the
    # counter and avg_time values - spoiler: this won't work!
    inner.counter = counter
    inner.avg_time = avg_time
    return inner
  
from time import sleep
import random

random.seed(0)

@profiler
def func1():
    sleep(random.random())
    
func1(), func1() ---> (None,None)
func1.counter
---> 0

Hmm, that's weird - counter still shows zero. This is because we have to understand what we did in the decorator 
- we made inner.counter the value of counter at the time the decorator function was called - this is not the counter value that we keep updating!!



  

