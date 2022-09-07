#Write a python script to print first N even natural numbers in reverse order

n=int(input('enter a number '))
for e in range(2*n,0,-1):
    if e%2==0:
        print(e,end=' ')
print()