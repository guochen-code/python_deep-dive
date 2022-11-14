# timer for the with block
from time import perf_counter, sleep

class Timer:
  def __init__(self):
    self.elapsed = 0
    
  def __enter__(self):
    self.start = perf_counter()
    return self # why? after the context manager has exited, need to go back to the object and read the values
    
  def __exit__(self,exc_type,exc_value,exc_tb):
    self.stop=perf_counter()
    self.elapsed  = self.stop - self.start
    return False
  
with Timer() as timer:
  sleep(1)
print(timer.elaspsed)

*********************************************************************************** generator + context manager
from time import perf_counter, sleep
@contextmanager
def timer():
  stats=dict()
  start=perf_counter()
  stats['start']=start
  try:
    yield stats
  finally:
    end=perf_counter()
    stats['end']=end
    stats['elasped']=end-start

with timer() as stats:
  sleep(2)
print(stats)
