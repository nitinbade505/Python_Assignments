#Write a python script to calculate sum of cubes of first N natural numbers

sum=0
n=int(input('enter a number '))
for e in range(n):
    print(e+1,end =' ')
    #sum=sum+(e+1)**3
    sum+=(e+1)**3
print()
print(sum)