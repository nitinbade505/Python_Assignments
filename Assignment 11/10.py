"""Write a python script to print the octal equivalent of a given decimal number. (do not
use oct() method)"""

c=''
n=int(input('enter a number '))
while n>0:
    c=(print(0) if n%8==0 else print(n))
    n=n//8