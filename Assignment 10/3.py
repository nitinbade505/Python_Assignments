 #Write a python script to print first N natural numbers in reverse order

n=int(input('enter a number '))
for e in range(n,0,-1):
    print(e,end=' ')
print()


n=range(int(input('enter a number ')),0,-1)    # range(4, 0, -1)  , n=(4 3 2 1)
for e in n:
    print(e,end=' ')
