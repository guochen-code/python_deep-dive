mapping -> applying a callable to each element of an iterable
        -> map(fn,iterable)
            -> fn must be a callable that requires a single argument
            
            
        
accumulation -> reducing an iterable down to a single value
  -> sum(iterable)
  -> min(iterable)
  -> max(iterable)
  -> reduce(fn,iterable,[initializer]) # 
        -> fn is a function of two arguments
        -> applies fn accumulatively to elements of iterable
        
example:

l = [1,2,3,4]
sum(l) -> 1+2+3+4=10

reduce(lambda x,y: x+y, l) -> 1 # !!!! no caculation here!!!! just take the 1st element as the start value
                           -> 1+2 =3 # 1 is the result of previous step and 2 is next unused element in the iterable
                           -> 3+3=6
                           -> 6+4=10
      
to find the product of all elements
reduce(lambda x,y: x*y, l)

**********************************************************************************************************************************************
itertools.starmap

starmap is very similar to map
  -> it unpacks every sub element of the iterable argument, and passes that to the map function
  -> useful for mapping a multi-argument function on an iterable of iterables
  
l=[[1,2],[3,4]] 

map(lambda item: item[0]*item[1],l) -> 2,12

we can use starmap: starmap(operator.mul,l) -> 2,12
  
we could also just use a generator expression to do the same thing:
(operator.mul(*item) for item in l)

we can of course use iterables that contain more than just two values:
l = [[1,2,3],[10,20,30],[100,200,300]]
starmap(lambda x,y,z: x+y+z,l) -> 6, 60, 600

all three approaches give lazy iterator

**********************************************************************************************************************************************
itertools.accumulate(iterable,fn) -> lazy iterator

very similar to the reduce function

but it retunrs a lazy iterator producing all the itermediate results -> reduce only returns the final result

unlike reduce, it does not accept an initializer

note the argument order is not the same !!!!
reduce(fn,iterable)
accumulate(iterable,fn)

in accumulate, fn is optional -> dfaults to addition

example:
[l = [1,2,3,4]
 
functools.reduce(opearator.mul,l) -> 24

itertools.accumulate(l,operator.mul) -> 1,2,6,24 # give us intermediate results as well
 
 
