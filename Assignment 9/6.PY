#Write a python script to print first N even natural numbers

i=1
n=int(input("enter a number "))
while i<n:
    if i%2==0:
        print(i,end=' ')
    i+=1