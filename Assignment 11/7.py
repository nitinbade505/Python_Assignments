#Write a python script to count digits in a given number

n=int(input('enter a number '))
count=0
for e in str(n):
    print(e,end=' ')
    count+=1
print()
print(count,end=' ')