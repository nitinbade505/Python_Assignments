#Write a python script to calculate sum of first N even natural numbers
sum=0
n=2*int(input('enter a number '))
for e in range(n):
    if e%2==1:
        print(e+1,end =' ')
        #sum=sum+e+1
        sum+=e+1
print()
print(sum)
