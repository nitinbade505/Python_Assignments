#Write a python script to print first N odd natural numbers in reverse order

i=1
n=int(input("enter a number "))
while i<=n*2:
    if i%2==1:
        print(n*2-i,end=' ')
    i+=1