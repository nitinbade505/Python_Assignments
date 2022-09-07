#Write a python script to print first N odd natural numbers

n=int(input('enter a number '))
for e in range(2*n):
    if e%2==1:
        print(e,end=' ')
print()