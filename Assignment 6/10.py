"""Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same."""
print("enter a three number")
a,b,c=int(input()),int(input()),int(input())
print()
if a>b:
    print(a)
elif a>b:
    print(b)
elif b>c:
    print(b)
elif b>c:
    print(c)
elif c>a:
    print(c)
elif c>b:
    print(b)
print()

print((a if a>c else c) if a>b else (b if b>c else c))