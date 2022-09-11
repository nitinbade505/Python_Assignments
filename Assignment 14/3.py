# Write a Python script to create a list of first N even natural numbers

n=int(input('enter a number '))
for e in range(n):
    if e%2==1:
        print(e+1,end=' ')
