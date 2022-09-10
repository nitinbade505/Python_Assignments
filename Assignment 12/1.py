# Write a python script to reverse a number.
n=int(input('enter a number '))
r=range(n,0,-1)
for e in r:
    print(e,end=' ')
print()

#or

for e in range(n,0,-1):
    print(e,end=' ')

#or

r=range(12345)
for e in r:
    print(e,end=' ') 

