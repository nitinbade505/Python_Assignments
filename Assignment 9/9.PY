#Write a python script to print cubes of first N natural numbers

i=1
n=int(input("enter a number "))
while i<=n:
    print(i*i*i, end =' ')                  # i**3 you also use this
    i+=1