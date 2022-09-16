# Write a python program to create a function to check whether a given number is even or odd.

def evenodd(a,b,c,d):
    for e in (a,b,c,d):
        if e%2==0:
            print('Even')
        else:
            print('Odd')
evenodd(1,2,3,4)
print()

def evenodd(a,b,c,d):
    for e in (a,b,c,d):
        print('even' if e%2==0 else 'Odd')
evenodd(1,2,3,4)