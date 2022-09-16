# Write a python program to access a function inside a function

def f():
    print('a')
    print('b')
    def add(a,b):
        print(a+b)
    add(2,3)
f()