# Generator --> It is function, generate a value with the "yield" keyword 
# if its body contain "yield" keyword its automatically become generator function.
# it is obtain the iterator object means output is iterator object.
# iter() and generator() both obtain iterator object.
# iter() obtain in statically while generator obtain dynamically.

def f():
    yield 5    # yield 5 means generate 5 as iterator object item
    yield 10   # yield 10 means generate 10 as iterator object item
    yield 15
it=f()
print(next(it))
print(next(it))
print(next(it))
print()

# or use for loop as written below for the same

for e in f():
    print(e,end =' ')
print()
print()

def f(n):
    x=2
    while n:
        yield x
        x+=2
        n-=1
for e in f(10):
    print(e,end=' ')
