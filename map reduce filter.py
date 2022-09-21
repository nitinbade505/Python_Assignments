# map reduce filter --> these are functions  --. map object
# 1. map function --> map function returns a map object (iterable) 
# syntax -- map(function,iterable)

l1=[1,2,3,4]
def square(a):
    return a*a
l2=list(map(square,l1))
print(l2)
print(type(l2))
print()

# 2. reduce --> this is function is defined in functools module. You need to import reduce from functools module.
# reduce function return single accumulated value.
# syntax --> reduce(function,iterable)

from functools import reduce
l1=[1,2,3,4]
def multiply(a,b):
    return a*b
r=reduce(multiply,l1)
print(r)
print(type(r))
print()

# 3. Filter --> filter method filters a given iterable with the help of function and test each element in the iterable to be true or not.
# syntax --> filter(function,iterable)
# it filter true output only.

l1=[1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17]
def checkprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
l2=list(filter(checkprime,l1))
print(l2)
print(type(l2))
