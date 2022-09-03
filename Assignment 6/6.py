#Write a python script to check whether a given number is a three digit number or not.
x=int(input("enter a number"))
if 99<x<1000:
    print("Three digit number")
else:
    print("Not a three digit number")

print("3 digit" if 99<int(input("enter a number"))<1000 else "not 3 digit")
