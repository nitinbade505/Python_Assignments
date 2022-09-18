# Write a recursive python function to print first N even natural numbers
def f(n):
    if n>0:
        f(n-1)
        if n%2==0:
            print(n,end=' ')
f(9)