"""Write a python script to check whether a given pair of numbers are co-Prime
numbers or not."""


n=int(input('enter a number '))
for e in range(n):
    if e%2==0:
        print(e+1,end=' ')