'''
the garbage collector destroys objects that are no longer referenced anywhere
  -> hook into that lifecycle event
      -> use the __del__ method
      
  the __del__ method will get called right before the object is destroyed by the GC
      -> so the GC determines when this method is called
      
  -> __del__ is sometimes called the class finalizer
  (sometimes called the destructor, but not entirely accurate, since GC destroys the object)
  
  
when does __del__ method called?
-> that's the basic issue with the __del__ method
    -> we do not control when it will get called !!!!!!!
    called only when all references to the object are gone
  -> have to be extremely careful with our code
  -> easy to inadvertently create additional references, or circular references
'''

'''
additional issues

if __del__ contains references to global variables, or other objects
    -> those objects may be gone by the time __del__ is called
    
if an exception occurs in the __del__ method
  -> exception is not raised - it is silenced
  -> exception description is sent to stderr
  -> main program will not be aware something went wrong during finalization

-> prefer using context managers to clean up resources

-> perosnally I do not use __del__
'''

please see the notebook



