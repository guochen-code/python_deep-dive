Counter is a subclass of dictionary

*****************************************
from collection import Counter

counter = Counter()
for c in sentence:
  counter[c]+=1

c1 = Counter(sentence)
c1 = Counter([1,2,2,2,3,3,4,4,4]) -> Counter({1:1,2:3,3:2,4:3})

# split on words
import re

words = re.split('\W', sentence)
word_count=Counter(words)
word_count.most_common(5) # top 5 words

# interesting:

c1 = Counter('abba')

for c in c1:
  print(c) -> a b # return keys
  
for c in c1.elements():
  print(c) -> a a b b # return all elements
  
******************************************************
# throw out the key as many times as its corresponding value # what is the applicaiton?
c1 = Counter()
for i in range(1,11):
  c1[i] = i
print(list(c1.elements()))

# to reproduce above using normal dictionary
class RepeatIterable:
  def __init__(self,**kwargs):
    self.d = kwargs
    
  def __setitem__(self,key,value):
    self.d[key] = value
    
  def __getitem__(self,key):
    self.d[key] = self.d.get(key,0)
    return self.d[key]
  
  def elements(self):
    for k, frequency in self.d.items():
      for _ in range(frequency):
        yield k
    
r = RepeatIterable(x=10,y=20)

************************************************************ # add/subtract two counters
c1 = Counter(a=1, b=2, c=3)
c2 = Counter(b=1, c=2, d=3)

c1.update(c2)
c1.subtract(c2) # do this again, will have negative values

# also can do this, directly with raw data
c1 = Counter('aabbccddee')
c1.update('abcdef')

# Counter also supports some mathmatical operations
c1+c2 -> return new object
c1-c2

# compare two counters, maximum and minimum 
c1 = Counter(a=5, b=1)
c2 = Counter(a=1,b=10)

c1 & c2 -> Counter({'a':1, 'b':1}) # return minimum
c1 | c2 -> Counter({'a':5,'b':10})

# remove negative counter # application: up to one time, only care about positive
c1 = Counter(a=10, b=-10, c=0)
+c1 -> Counter({'a':10}) # return a new object

-c1 -> Counter({'b':10}) # step-1: add nagetive to all values; step-2: return the positive key and value

************************************************************ application ************************************************************
to find out what is the top selling products
source data: (1) sales (2) refunds

import random
random.seed(0)

# simulate data
widgets = ['battery', 'charger', 'cable', 'case', 'keyboard', 'mouse']
orders = [(random.choice(widgets), random.randint(1,5)) for _ in range(100)]
refunds = [(random.choice(widgets), random.randint(15)) for _ in range(20)]

sold_counter = Counter()
refund_counter = Counter()

# cannot directly pass orders and refunds to the counter
for order in orders:
  sold_counter[order[0]] += order[1]
for refund in refunds:
  refund_counter[refund[0]] += refund[1]
  
net_counter = sold_counter - refund_counter
net_counter.most_common(3)

****************************** a step further
# if want to directly pass to Counter, we need sth like
Counter(['battery''battery','battery','keyboard','keyboard']
# in order to do that
from itertools import repeat
list(repeat('battery',3)) -> ['battery''battery','battery']

list(repeat(*orders[0]) # orders[0] -> ('case',4) so need to unpack
# so we want to chain these together
repeat(*orders[0]) + repeat(*orders[1]) + ........ + repeat()

# chain mutiple iterbales into a single iterable
list(chain.from_iterable(repeat(*order) for order in orders))
couter_orders = Counter(chain.from_iterable(repeat(*order) for order in orders)
refund_orders = Counter(chain.from_iterable(repeat(*refund) for refund in refunds)
net_counter = sold_counter - refund_counter

********************** to do without using Counter
net_sales={}

for order in orders:
  key = order[0]
  cnt = order[1]
  net_sales[key] = net_sales.get(key,0) + cnt
  
for refund in refunds:
  key = refund[0]
  cnt = refund[1]
  net_sales[key] = net_sales.get(key,0) + cnt

net_sales = {k : v for k,v in net_sales.items() if v>0}
sorted_net_sales = sorted(net_sales.items(), key = lambda t:t[1], reverse = True)
sorted_net_sales[:3]
