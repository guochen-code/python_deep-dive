chaining iterables

what happens if we want to chain from iterables contained inside another, single, iterable?
for example:

l = [iter1, iter2, iter3]
chain(l) -> l
what we really want is to chain iter1, iter2 and iter3

we can try this using unpacking: chain(*l)
  
BUT.............................................!!!!!!!!!!!!!!!!!!!!
unpacking is eager not lazy
if l was a lazy iterator, we essentially iterate through l (not the sub iterators), just to unpack! 

what if you want a lazy outcome, because we may not use all the elements...only need first few elements.....
solution:

itertools.chain.from_iterable(it) -> lazy iterator

it is equivalent to this code:
def chain_lazy(it):
  for sub_it in it:
    yield from sub_it
        
**********************************************************************************************************************************************************

teeing iterators

itertools.tee(iterable,n)

sometimes we need to iterate through the same iterator multiple times, or even in parallel (iterator is getting exausted, cannot be reused)

we could create the iterator multiple times manually

iters=[]
for _ in range(10):
  iters.append(create_iterator())
  
or we can use tee in itertools -> return independent iterators in a tuple !!!! key word here is independent !!!!

tee(iterables,10) -> (iter1, iter2,....,iter10) #### independent ---- all different objects !!!!!!!!!!!!

ONE IMPORTANT THING TO NOTE
the element of the returned tuple are lazy iterators
  -> always!
  -> even if the original argument was not
  
l = [1,2,3,4]
tee(l,3) -> (iter1, iter2, iter3) # all lazy iterators, not list!!!!!!!!!
**********************************************************************************************************************************************************

