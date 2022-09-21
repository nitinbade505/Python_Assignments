# Create a generator to produce squares of first N natural numbers

def sqr(n):
    i=1
    while n:
        yield i*i
        i+=1
        n-=1
it=sqr(10)
#print(next(it),next(it),next(it),next(it),next(it))

for e in it:
    print(e,end=' ')
