"""Write a python script to print all Prime numbers between two given numbers (both
values inclusive)"""

n=int(input('enter a number '))
p=int(input('enter a number '))
r=range(n,p,1)
for e in r:
    if e%2==0:
        print(e,end=' ')