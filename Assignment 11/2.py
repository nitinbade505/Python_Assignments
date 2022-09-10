#Write a python script to calculate sum of squares of first N natural numbers

sum=0
n=int(input('enter a number '))
for e in range(n):
    print(e+1,end=' ')
    sum+=(e+1)**2
print()
print(sum)