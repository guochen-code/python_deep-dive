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

------------------------------------------------------------------------------------------------------------------------------------------------------------

def matrix(n):
  for i in range(1,n+1):
    for j in range(1,n+1):
      yield (i,j,i*j)
      
def matrix(n):
  for i,j in itertools.product(range(1,n+1),range(1+n+1)):
    yield (i,j,i*j)
    
def matrix(n):
  return ((i,j,i*j) for i,j in itertools.product(range(1,n+1),range(1,n+1)))

# what if we have more than 2 demensions, we can use tee

def matrix(n):
  return ((i,j,i*j) for i,j in itertools.product(*itertools.tee(range(1,n+1),2))) # must unpack; # generators from tee, they are independent!!!


********************************************************************** application
generate grid points for a plot

def grid(min_val,max_val,step,*,number_dimensions=2):
  axis = itertools.takewhile(lambda x:x<= max_val, itertools.count(min_val,step)) # range only for integers while count can be used for floats
  axes=itertools.tee(axis,number_dimensions)
  return itertools.product(*axes)

rolling two dices - summation = 8 
sample_space = list(itertools.product(range(1,7),range(1,7)))
outcomes = list(filter(lambda x:x[0] + x[1] ==8, sample_space))
len(outcomes)/len(sample-space) -> 0.138888888888889
# use fraction
from fractions import Fraction
odds = Fraction(len(outcomes),len(sample_space))
odds -> Fraction(5,36)

********************************************************************** application
permutation

combination
list(itertools.combination([1,2,3,4],2)) -> [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
list(itertools.combination([4,2,3,1],2)) -> [(4,2),(4,3),(4,1),(2,3),(2,1),(3,1)]

list(itertools.combination_with_replacement([1,2,3,4],2))


# what is the chance have 4 Ace
# odds of succesively picking four aces from a shuffled deck is:
# this is brutal force approach (run all posibilities, costly) - although can use statistics: 
deck = (Card(rank,suit) for suit, rank in itertools.product(SUITS,RANKS))
sample_space = itertools.comninations(deck,4)
total=0
acceptable=0
for outcome in sample_space:
  total+=1
  for card in outcome:
    if card.rank != 'A':
      break
  else: #nobreak:    # if we break the else call will not be executed !!!!!!
    acceptable+=1

# simplify code above
# demonstrate why we use namedtuple to describe the cards
deck = (Card(rank,suit) for suit, rank in itertools.product(SUITS,RANKS))
sample_space = itertools.comninations(deck,4)
total=0
acceptable=0
for outcome in sample_space:
  total+=1
  if all(map(lambda x: x.rank == 'A', outcome)): # this is the use of namedtuple !!!!
    acceptable+=1
