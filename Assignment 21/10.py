# Write a recursive python function to print a number in reverse order.


def f(n):
    if n>0:
        print(n,end=' ')
        f(n-1)
f(20)
