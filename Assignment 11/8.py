#Write a python script to calculate sum of digits of a given number


sum=0
n=int(input('enter a number '))
for e in str(n):
    print(e,end=' ')
    sum=sum+int(e)
print()
print(sum)