# Create a generator to produce first n even natural numbers

def even(n):
    i=2
    while n:
        yield i
        i+=2
        n-=1
it=even(5)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print()


def even(n):
    i=2
    while n:
        yield i
        i+=2
        n-=1
for e in even(5):
    print(e,end=' ')