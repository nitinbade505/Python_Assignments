# Write a recursive python function to print first N multiples of a given number

e=int(input ('enter a number '))
def f(n):
    if n>0:
        f(n-1)
        print(n*e,end=' ')
f(10)