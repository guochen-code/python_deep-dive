print('hello') # the standard output is here in jupyter notebook, in the console

# we can use context manager to redirect the standard output to somewhere else

import sys

class OutToFile:
  def __init__(self,fname):
    self._fname = fname
    self._current_stdout = sys.stdout
    
  def __enter__(self):
    self._file=open(self._fname,'w')
    sys.stdout=self._file
    
  def __exit__(self,exc_type,exc_value,exc_tb):
    sys.stdout=self._current_stdout
    self._file.close()
    return False
  
with OutToFile('test.txt'): # if __enter__ not return anything, we don't need as xxxxxx
  print('Line 1')
  print('Line 2')
  
***************************************************************************************************** generator + context manager
import sys
@contextmanager
def out_to_file(fname):
  current_stdout=sys.stdout
  file=open(fname,'w')
  sys.stdout=file
  try:
    yield None
  finally:
    file.close()
    sys.stdout=current_stdout
    
with out_to_file('test.txt'): 
  print('Line 1')
  print('Line 2')
  
***************************************************************************************************** python built-in
# our method above only redirect to file, built-in can be more generic than just sending it to a file
# we can redict it to a file object, not a file
from contextlib import redirect_stdout
with open('test.txt','w') as f:
  with redirect_stdout(f):
    print('look on')

with open('test.txt','r') as f:
  print(f.readlines())


