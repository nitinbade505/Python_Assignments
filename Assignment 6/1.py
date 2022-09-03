#Write a python script to check whether a given number is positive or non-positive

x=int(input("enter a number "))
if x>0:
    print('positive')
if x<=0:
    print("non positive")


if x>0:
    print("positive")
else:
    print("Non positive")

print("non positive" if int(input("enter a number "))<=0 else "positive")