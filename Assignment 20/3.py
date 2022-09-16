"""Write a python program to create a function that prints the even numbers from a
given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]"""

def even(*t):
    print(list(t))
    for e in list(t):
        print(e)
        print(type(e))
        for l in e:
            if l%2==0:
                print(l,end=' ')
                print('even')
even([1, 2, 3, 4, 5, 6, 7, 8, 9])