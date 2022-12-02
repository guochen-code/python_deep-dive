# filter function
filter(predicate, iterable) # use predicate on iterable. if true, it will retain the corresponding iterable item.

# predicate is just a fancy way to say it is a function of signle argument that returns True or False

filter returns a lazy iterator : (1) one at a time; (2) can get exausted
we can achieve the same result using generator expressions:
(item for item in iterable if pred(item))

application:
filter(lambda x:x<4, [1,10,2,10,3,10]) -> 1,2,3

filter(None,[0,'','hello',100,False]) # goin to look at truth value of each of the elements -> 'hello',100

---- itertools.filterfalse
# instread of retaining elements where the predicate evalutes to True, it retains where the predicate evaluates to False
filterfalse(lambda x: x<4, [1,10,2,10,3,10]) -> 10, 10, 10

---- itertools.compress
No, this is not a compressor in the sense of a zip archive!
it is basically a way of filtering one iterable, using the truthiness of items in another iterable

data = ['a','b','c','d','e'] # retain the element if associated value is True
selectors = [True, False, 1, 0] 
compress(data,selectors) -> a,c # 'e' is associated with None which is also False
it is also a lazy iterator, no pre-calculate, yiled one at a time

---- itertools.takewhile
takewhile(pred,iterable)

takewhile(lambdax:x<5, [1,3,5,2,1]) -> 1,3 # when get to 5, it is False, iteration stopped. # will get get [2,1] even they are also True

---- itertools.dropwhile
dropwhile(pred,iterable)

dropwhile(lambdax:x<5,[1,3,5,2,1]) -> 5,2,1
************************************************************************************************************************************************
