# area is a computed property, every radius has its area.....
# if you need to access area 1000 times, you don't want to calculate it 1000 times
# you would like to cache it

class Circle:
  def __init__(self,radius):
    self._radius = radius
    self._area = None
    
  @property
  def radius(self):
    return self._radius
  
  @radius.setter
  def radius(self,value):
    self._area = None # validate cache
    self._radius = value
    
  @property
  def area(self):
    if self._are is None:
      print('calculating area...')
      self._area = pi * (self.radius**2) # not use self._radius: return abs(self._radius) when sb put negative value. use getter can make sure it is positive.
    return self._area # if not None, return cache value
  
# this is example we use getter and setter to do more than validation, 

# lazy attributes/properties
import urllib
from time import perf_counter

class WebPage:
  def __init__(self,url):
    self.url=url
    self._page=None
    self._load_time_secs=None
    self._page_size=None
    
    @property
    def url(self):
      return self._url
    
    @url.setter
    def url(self,value):
      self._url=value
      self._page=None
      
    @property
    def page(self):
      if self._page is None:
        self.download_page()
      return self._page
    
    @property
    def page_size(self):
      if self._page is None:
        self.download_page()
      return self._page_size
    
    @property
    def time_elapsed(self):
      if self._ppage is None:
        self.download_page()
      return self._load_time_secs
    
    def download_page(self):
      self._page_size=None
      self._load_time_secs=None
      start_time=perf_counter()
      with urllib.request.urlopen(self.url) as f:
        self._page=f.read()
      end_time=perf_counter()
      self._page_size=len(self._page)
      self._load_time_secs=end_time-start_time
      
urls=['https://www.google.com','https://www.python.org','https://www.yahoo.com']

for url in urls:
  page = WebPage(url) # lazy, here just create object, not download page
  print(f'{url}\tsize={format(page.page_size,"_")}\telapsed={page.time_elapsed:.2f} secs') # get the data when request
