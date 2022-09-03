#Write a python script to check whether a given number is even or odd

x=int(input("enter a number "))
if x%2==0:
    print("number is even")
else:
    print("number is odd")


print("even" if int(input("enter a number"))%2==0 else "odd")

print("odd" if int(input("number"))%2 else "even")