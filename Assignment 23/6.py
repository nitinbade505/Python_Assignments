# Create a generator to produce first n prime numbers
def prime(n):
    i=1
    while n:
        yield i
        i+=1
        n-=1
it=prime(10)
#print(next(it),next(it),next(it),next(it),next(it))

for e in it:
    print(e,end=' ')