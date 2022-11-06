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
  
