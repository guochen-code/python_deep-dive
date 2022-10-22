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

if you only need to insert and pop, deque will be much faster.
but if you also want to look up for one element to check if it is in the collection, ordered dict will be faster 
because in deque or list it needs to iterate through the whole deque or list

