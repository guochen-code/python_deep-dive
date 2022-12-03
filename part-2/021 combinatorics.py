cartesian product

itertools.product(*args) -> lazy iterator

l1= [1,2,3]
l2 = ['a','b','c','d']

product(l1,l2) -> (1,'a'),(1,'b'),(1,'c'),(1,'d'), ..., (3,'d')
l3 = [100,200]

product(l1,l2,l3)

**********************************************************************
permutations

itertools.permutations(iterable, r=None)
  -> r is the size of the permutation
  -> r=None means length of each permutation is the length of the iterable
  
elements of the iterable are considered unique based on their positionm not their value
->
if iterable produces repeat values then permutations will have repeat values too

**********************************************************************
combinations

unlike permutationsm the order of elements in a combination is not considered
  -> ok to always sort the elements of a combination

combination of length r, can be picjed from a set
--- without replacement -> once an element has been picked from the set it cannot be picked again
---- with replacement -> once an element has been picked from the set it can be picked again

itertools.combinations(iterable,r) # the size of combination
itertools.combinations_with_replacement(iterable,r)

just like for permutations: the elements of an iterable are unique based on their positionm not their value
  
the different combinations produced by these functions are sorted based on the original ordering in the iterable

