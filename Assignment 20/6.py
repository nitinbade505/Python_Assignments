"""Write a python program to create a function and print a list where the values are
square of numbers between 1 and 30."""

def sqr(*t):
    print(t)
    for e in t:
        print(e**2,end=' ')
sqr(1,2,3,4,5,6,7,8,9)