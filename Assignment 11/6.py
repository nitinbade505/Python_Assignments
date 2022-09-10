#Write a python script to calculate factorial of a given number

fact=1
n=int(input('enter a number '))
for e in range(1,n+1):
    print(e,end=' ')
    fact=fact*e
print()
print(fact,end=' ')    
