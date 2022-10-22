# you can do reverse iteration while you can't do it with normal dictionary

for k in reversed(d):
  print(k)
  
# ordered dict is a subclass of dictionary. everything you can do with dictionary you can do with ordered dict.

d.popitem() -> remove last item
d.popitem(last=False) -> remove first item

d.move_to_end('<key you want to move>')
d.move_to_end('<key you want to move>',last=False) -> move to beginning

ordered_d1==ordered_d2 # only if the key and values are the same and the keys are in the same order
ordered_d1==d2 # when compare with normal dict, the order does not matter any more

****************************************

# compare efficiency with deque

it depends on your problem

if you only need to insert and pop, deque will be much faster. you don't need to frequently check the membership.....
but if you also want to look up for one element to check if it is in the collection, ordered dict will be faster 
because in deque or list it needs to iterate through the whole deque or list

****************************************
summary:
  (1) reversed iteration
  (2) popitem first or last
  (3) move to end or beginning
  (4) equality: key and order
    
**************************************** how to reproduce these properties to normal dictionary
(1) we can create a list, we know a list cane be reversed
(2) you can also create a list to do so. but different way: first_key = next(iter(d.keys()))
  normal dictionary also has popitem, can use this to find the last_key
  normal dictionary also can popitem according to key
  def popitem(d, last=True):
    if last:
      return d.popitem()
    else:
      first_key = next(iter(d.keys()))
      return first_key, d.pop(first_key)
(3) move to end is easy, because it is kind of default
    move to beginning is chanllenging
    3.1 pop the target key and insert the target key which will be at the end of the dict
    3.2 pop the 1st key of the dict and insert, keep doing this, until you have the target key at the beginning
    or you can create a new dictionary (NOT what we want here) while the above technique just to mutate the dictionary
    def move_to_end(d, key, *, last=True):
      d[key] = d.pop(key)
      
      if not last:
        for key in list(d.keys())[:-1]:
          d[key] = d.pop(key)
(4) d1.keys() == d2.keys() # keys view acts like set. when you compare set, it is no order
    list(d1.keys()) == list(d2.keys()) # list equality, the order does matter
  so one way:
    d1 == d2 and list(d1.keys()) == list(d2.keys()) # but some overhead here because you need to create a new list
  if not want to create a new list, just iterate through the keys:
    def dict_equal_sensitive(d1,d2):
      if d1 == d2:
        for k1, k2 in zip(d1.keys(), d2.keys()):
          if k1 != k2:
            return False
        return True
      else:
        return False
********************************** improvement

def dict_equal_sensitive(d1,d2):
      if d1 == d2:
        for k1, k2 in zip(d1, d2):   # change here!!!!!
          if k1 != k2:
            return False
        return True
      else:
        return False

      
def dict_equal_sensitive(d1,d2):
      if d1 == d2:
        return all(k1 == k2 for k1, k2 in zip(d1,d2))    # change here!!!
      else:
        return False      
      
      
map(lambda x: x**2, [1,2,3]) -> <map at 0x103696748> # map is a generator
list(map(lambda x: x**2, [1,2,3])) -> [1,4,9]

map(lambda el: el[0] == el[1], zip(d1,d2))
any(map(lambda el: el[0] == el[1], zip(d1,d2)))

def dict_equal_sensitive(d1,d2):
      if d1 == d2:
        return any(map(lambda el: el[0] == el[1], zip(d1,d2)))   # change here!!!
      else:
        return False  
******************************
next question: is ordered dict slower than normal dictioanry?
  yes, overhead to track the order
  retrieve keys are the same
  pop, move, equality and so on normal dict is slower, except for poping the last item.

  
