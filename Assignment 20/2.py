"""Write a python program to create a function that takes a number as a parameter and
checks if the number is prime or not."""

def para(*t):
    for e in t:
        print(e,end=' ')
        if e//e==1 and e%2==1:
            print('prime',end=' ')
para(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)