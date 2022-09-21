# Iterator --> It can seen as a pointer to a container 
# It is point to the object inside container
# it is work only on container elements of object like list, str, dict etc
# iter(iterable) - it is iterator function
# next(iterator) - it is function and return the next item form the iterator

l=[10,20,40,50,80,20,30]
it=iter(l)  # its takes container as argument as input and produce iterable object pointing to first element of object as output
print(type(iter(l)))    # class "list_iterator"
print(next(it))   # It is function and produce output as first element of object of container.
print(next(it))   # It produce next (second) element of object of container
print(next(it))   # it produce next element as output 
print()

l=[1,2,3,4]
it=iter(l)
while True:
    print(next(it),end=' ')    # Error StopIteration

