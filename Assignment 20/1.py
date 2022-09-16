"""Write a python program to create a function that takes a list and returns a new list
with the original list's unique elements."""

def lst(*t):
    print(list(t))
    print(type(list(t)))
lst([10,20,30,40,50,10,20])