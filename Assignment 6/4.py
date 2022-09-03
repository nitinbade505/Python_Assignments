"""Write a python script to print greater between two numbers. Print number only once
even if the numbers are the same"""

x=int(input("enter a number x "))
y=int(input("enter a number y "))
if x>y:
    print("x is greater than y")
if y>x:
    print("y is greater than x")
if x==y:
    print("both are same")

print("two numbers")
a,b=int(input()),int(input())
print(a if a>b else b)