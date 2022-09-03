"""Write a python script to check whether a given quadratic equation has two real &
distinct roots, real & equal roots or imaginary roots"""

print("enter value of a,b,c of a qaudratic equ")
a,b,c=int(input()),int(input()),int(input())
d=b**2-4*a*c
if d>0:
    print("distict root")   # a,b,c = 2,5,2
elif d==0:
    print("real and equal") # a,b,c = 2,4,2
else:
    print("imaginary root") # a,b,c = 1,2,2