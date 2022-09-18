# Write a recursive python function to print cubes of first N natural numbers

def f(n):
    if n>0:
        f(n-1)
        print(n*n*n,end=' ')
f(9)