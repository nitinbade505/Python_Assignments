#Write a python script to print first N even natural numbers

n=int(input('enter a number '))
for e in range(2*n):
    if e%2==0:
        print(e+2,end=' ')
print()