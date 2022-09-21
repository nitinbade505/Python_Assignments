#Create a generator to produce first n odd natural numbers

def oddnatural(n):
    i=1
    while n:
        yield i
        i+=2
        n-=1
it=oddnatural(5)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print()


def oddnatural(n):
    i=1
    while n:
        yield i
        i+=2
        n-=1
for e in oddnatural(10):
    print(e,end=' ')