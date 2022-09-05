#Write a python script to print first N even natural numbers in reverse order

i=0
n=int(input("enter a number "))
while i<n*2:
    if i%2==0:
        print(n*2-i,end=' ')
    i+=1