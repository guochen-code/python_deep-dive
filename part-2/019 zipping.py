the zip function -> lazy iterator

zips based on the shortest iterable

sometimes we want to zip, but based on the logest iterable
    -> need to provide a default value for the holes -> fillvalue

itertools.zip_longest(*args,[fillvalue=None])

************************************
a=zip(l1,l2,l3)
# if iterable
iter(a) is a -> True
# if iterator
'__next__' in dir(a) -> True

**************************************** be aware
infinite iterator

iter1 = infinite
iter2 = infinite

cannot zip longest, because they are infinite
but it works if we give it a finite iterable

list(zip(range(10,iter1,iter2)) # this is ok

list(zip_longest(range(10,iter1,iter2)) # will cause a problem
     
     
