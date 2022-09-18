# Write a recursive python function to print first N natural numbers


def f(n):
    if n>0:
        f(n-1)
        print(n,end=' ')
f(9)