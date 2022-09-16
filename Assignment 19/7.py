# Write a python program to sum all the numbers in a list.

def sum():
    a=int(input('enter a number '))
    b=int(input('enter a number '))
    c=a+b
    print(c)
sum()
print()

def sum(a,b):
    print(a+b)
    c=a+b
    print(c)
sum(2,3)
print()

def fun(a):
    print(a)
    print(sorted(a))
fun(input('enter a number '))
