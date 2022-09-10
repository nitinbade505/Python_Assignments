#Write a python script to check whether a given number is Prime or not

n=int(input('enter a number '))
for e in range(n):
    if (e+1)//(e+1)==1:
        print(e+1,end=' ')