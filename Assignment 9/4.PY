#Write a python script to print first N odd natural numbers

i=1
n=int(input("enter a number "))
while i<=n*2:
    if i%2==1:
        print(i,end=' ')
    i+=1
