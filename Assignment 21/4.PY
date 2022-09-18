# Write a recursive python function to print first N odd natural numbers in reverse order

def f(n):
    if n>0:
        if n%2==1:
            print(n,end=' ')
        f(n-1)
f(9)