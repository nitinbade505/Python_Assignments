"""Write a python program to create a function that accepts a string and calculate the
number of upper case letters and lower case letters."""

def string(a):
    print(a)
    for e in a:
        if e=='N':
            print('Capital')
        print(e,end=' ')
        print('Small' if e=='i' else 'Capital')
string('Ni')