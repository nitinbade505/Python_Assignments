'''Write a python script to print binary equivalent of a given decimal number. (do not
use bin() method)'''

n=int(input("enter a number : "))
while(n>0):
    a=(print(0) if n%2==0 else print(1))
    n=n//2


