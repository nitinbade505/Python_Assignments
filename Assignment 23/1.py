# Use iter and next method to access all the elements of a given set using while loop

l={1,2,3,4,5}
print(type(l))
it=iter(l)
print(next(it),next(it),next(it),next(it),next(it))
print()


l={1,2,3,4,5,6,7,8}
it=iter(l)
i=1
while i<=8:
    print(next(it),end=' ')
    i+=1
