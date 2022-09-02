"""Write a python script which takes a three digit number from the user and displays
only its middle digit."""

x=int(input("enter a three digit number"))
y=int(x/10)
z=y%10
print(z)

print(int(x/10%10))

print(x//10%10)  # No need to use int 