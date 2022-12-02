---- itertools.count -> lazy iterator
the count function is an infinite iterator

similar to range -> start, step
different from range -> no stop -> infinite
                     -> start and step can be any numeric type float
  
  
count(10,2) -> 10, 12, 14 .....
count(10.5,0.1) -> 10.5, 10.6, 10.7 .....
takewhile(lambda x: x < 10.8, count(10.5,0.1)) -> 10.5, 10.6, 10.7

---- itertools.cycle -> lazy iterator
the cycle function allows us to loop over a finite iterable indefinitely

cycle(['a','b','c']). -> a,b,c,a,b,c.....
important
if the argument of cycle is itself an iterator -> iterator becomes exhausted
cycle will still produce an infinite sequence !!!!

---- itertools.repeat
the repeat function simply yields the same value indefinitely
repeat('spam') -> spam,spam,spam......

optionally, we can specify a count to make the iterator finite
repeat('spam',3)

caveat!!!!!
the items yielded by repeat are the same object -> they each reference the same object in memory !!!!
string does not matter, it is immutable
but be careful about mutable objects

************************************************************************************************************************************************************
g=count(10)
list(islice(g,5)) -> [10,11,12,13,14] # count can be used for integer, float, decimal, real number etc....
# need islice because of infinite loop

************************************************************************************************************************************************************
from collections import namedtuple

Card = namedtuple('Card', 'rank suit')

def card_deck():
    ranks = tuple(str(num) for num in range(2, 11)) + tuple('JQKA')
    suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
    for suit in suits:
        for rank in ranks:
            yield Card(rank, suit)

            
hands = [list() for _ in range(4)] !!!! cannot do hands = []*4 because they are refering to the same memory address

index = 0
for card in card_deck():
    index = index % 4
    hands[index].append(card)
    index += 1

----------------------------------------------------------------------------------------------------------------------------    
You notice how we had to use the mod operator and an index to cycle through the hands.

So, we can use the cycle function instead:
  
hands = [list() for _ in range(4)]

index_cycle = cycle([0, 1, 2, 3])
for card in card_deck():
    hands[next(index_cycle)].append(card)
    
----------------------------------------------------------------------------------------------------------------------------   
But we really can simplify this even further - why are we cycling through the indices? 
Why not simply cycle through the hand themselves, and append the card to the hands?

hands = [list() for _ in range(4)]

hands_cycle = cycle(hands)
for card in card_deck():
    next(hands_cycle).append(card)
