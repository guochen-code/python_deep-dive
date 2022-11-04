'''
very useful for anythin that needs to provide Enter/Exit Start/Stop Set/Reset

-> open / close file
-> start db transaction / commit or abort transaction
-> set decimal precision to 3 / reset back to orignal precision
'''

# general code
class Resource:
  def __init__(self,name):
    self.name=name
    self.state=None
    
class ResourceManager:
  def __init__(self,name):
    self.name=name
    self.resource=None
    
  def __enter__(self):
    print('entering context')
    self.resource=Resource(self.name)
    self.resource.state='created'
    return self.resource
  
  def __exit__(self,exc_type,exc_value,exc_tb):
    print('existing context')
    self.resource.state='destroyed'
    if exc_type:
      print('error occurred')
    return False # will raise error, not supress error
  
with ResourceManger('spam') as res:  # this line does two things, see below alternative
  print(f'{res.name}={res.state}')
print(f'{res.name}={res.state}')

# alternatively
res_manaer = ResourceManager('spam')
with res_manager as res:
    print(f'{res.name}={res.state}')
print(f'{res.name}={res.state}')

**************************************************************************************************
# application - open file
class File:
  def __init__(self,name,mode):
    self.name=name
    self.mode=mode
  
  def __enter__(self):
    print('opening file...')
    self.file=open(self.name,self.mode)
    return self.file   # you can return self here, with File('test.txt','r') as file_ctx, then not file anymore. so with statement gives whatever return in enter!!!
  
  def __exit__(self,exc_type,exc_value,exc_tb):
    print('closing file...')
    self.file.close()
    return False
  
with File('test.txt','w') as f:
  f.write('This is a late parrot!')

with File('test.txt','r') as f:
  print(f.readlines())
  

  
