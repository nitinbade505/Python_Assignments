# Recursion --> Function calling itself is called recursion.


def f(n):
    if n==1:
        return 1
    s=n+f(n-1)         # Here we called function itself.
    return s
r=f(3)
print(r)
print()

def add(n):
    if n==1:
        return 1
    return n+add(n-1)
r=add(2)
print(r)
print()

def printN(n):
    if n>0:
        printN(n-1)
        print(n,end=' ')
printN(5)
