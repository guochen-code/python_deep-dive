# class methods

class MyClass:
  def hello():
    print('hello...')
    
  def inst_hello(self):
    print(f'hello from {self}')
    
  @classmethod
  def cls_hello(cls):
    print(f'hello from {cls}')

                      MyClass                     Instance
hello              regular function             method bound to instance -> call will fail (by default, any function defined in a class will be handled as a bound method when called from an instance
inst_hello          regular function              method bound to instance
cls_hello          method bound to class            method bound to class

# static methods
# a function in a class that will never be bound to any obkect when called

class Circle:
  @staticmethod
  def help():
    return 'help available'                                                                       
c = Circile()
Cirucle.help() -> help available
c.help() -> help available   
                                                                                            
in summary
(1) function bound to instance when called from instance - will receive instance as first parameter
(2) function bound to class when called from either the class or the instance - will receive the class(MyClass) as first paramter
(3) static method is never bound to anything - receives no extra argument no matter how it is called
***************************************************************************************************************************************
# application
'''
why use static methods?
cases where it makes sense for a function to live in a class
  but does not need access to either the instance or the class state
  
Timer
  start(self)   -> instance method
  end(self)     -> instance method
  timezone      -> class attribute -> allow us to modify time zone for all instances
  current_time_utc()    -> static method
  current_time(cls)     -> class method(needs class time zone)
'''
                                                                                            
****************************************************************************************************************************************
class TimerError(Exception):
    """A custom exception used for Timer class"""
    # (since """...""" is a statement, we don't need to pass)
    
class Timer:
    tz = timezone.utc  # class variable to store the timezone - default to UTC
    
    def __init__(self):
        # use these instance variables to keep track of start/end times
        self._time_start = None
        self._time_end = None
        
    @staticmethod
    def current_dt_utc():
        """Returns non-naive current UTC"""
        return datetime.now(timezone.utc)
    
    @classmethod
    def set_tz(cls, offset, name):
        cls.tz = timezone(timedelta(hours=offset), name)
        
    @classmethod
    def current_dt(cls):
        return datetime.now(cls.tz)
    
    def start(self):
        # internally we always non-naive UTC
        self._time_start = self.current_dt_utc()
        self._time_end = None
        
    def stop(self):
        if self._time_start is None:
            # cannot stop if timer was not started!
            raise TimerError('Timer must be started before it can be stopped.')
        self._time_end = self.current_dt_utc()
        
    @property
    def start_time(self):
        if self._time_start is None:
            raise TimerError('Timer has not been started.')
        # since tz is a class variable, we can just as easily access it from self
        return self._time_start.astimezone(self.tz)  
        
    @property
    def end_time(self):
        if self._time_end is None:
            raise TimerError('Timer has not been stopped.')
        return self._time_end.astimezone(self.tz)
    
    @property
    def elapsed(self):
        if self._time_start is None:
            raise TimerError('Timer must be started before an elapsed time is available')
            
        if self._time_end is None:
            # timer has not ben stopped, calculate elapsed between start and now
            elapsed_time = self.current_dt_utc() - self._time_start
        else:
            # timer has been stopped, calculate elapsed between start and end
            elapsed_time = self._time_end - self._time_start
            
        return elapsed_time.total_seconds()                                                                                            
                                                                                            
                                                                                            
from time import sleep

t1 = Timer()
t1.start()
sleep(2)
t1.stop()
print(f'Start time: {t1.start_time}')
print(f'End time: {t1.end_time}')
print(f'Elapsed: {t1.elapsed} seconds')
                                                                                            
Timer.set_tz(-7, 'MST')

print(f'Start time: {t1.start_time}')
print(f'End time: {t1.end_time}')
print(f'Elapsed: {t1.elapsed} seconds')                                                                                            
                                                                                            
