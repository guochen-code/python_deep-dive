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

