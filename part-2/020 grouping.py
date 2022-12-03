# mimic df.head(n)

import itertools

with open('cars_2014') as f:
  for row in itertools.islice(f,0,20): # display 0-20 top rows
    print(row, end='')
    

# similar to group by

makes = defaultdict(int)

with open('cars_2014.csv') as f:
  next(f)
  for row in f:
    make,_ = row.strip('\n').split(',')
    makes[make]+=1
    
for key, value in makes.items():
  print(f'{key}:{value}')
  
# group

data=(1,2,2,2,3)
list(itertools.groupby(data)) ->
[(1,<itertools._grouper at 0x....>),
 (2,<itertools._grouper at 0x....>),
 (3,<itertools._grouper at 0x....>),]

it = itertools.groupby(data)
for group_key, sub_iter in it:
  print(group_key, list(sub_iter))
-> 
1 [1]
2 [2,2,2]
3 [3]


groups = itertools.groupby(data, key=lambda x: x[0]) # group by the 1st element of each tuple/list
for group_key, sub_iter in groups:
  print(group_key, list(sub_iter))
->
1 [(1,'abc'),(1,'bcd')]
2 [(2,'pyt'), (2,'yth'), (2,'tho')]
3 [(3,'hon')]

with open('cars_2014.csv') as f:
  next(f) # skip headers
  make_groups = itertools.groupby(f,key=lambdax:x.split(',')[0])
  make_counts = ((key,len(models) for key, models in make_groups)
  print(list(make_counts))
-> TypeError: object of type 'itertools._grouper' has no len()
                 
'''
# way-A:
def len_iterable(iterable):
  i = 0 
  for item in iterable:
    i+=1
  return i
# way-B: replace each element with number 1 and sum((1,1,1)) will give the length

with open('cars_2014.csv') as f:
  next(f) # skip headers
  make_groups = itertools.groupby(f,key=lambdax:x.split(',')[0])
  make_counts = ((key, sum(1 for model in models)) for key, models in make_groups)
  print(list(make_counts))
                 
               
                 


