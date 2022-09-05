#Write a python script to print first N even natural numbers in reverse order

i=1
n=int(input("enter a number "))
while i<n:
    if i%2==1:
        print(n-i,end=' ')
    i+=1