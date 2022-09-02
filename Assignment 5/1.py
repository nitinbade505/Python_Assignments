"""Write a python script to remove the last digit from a given number. (for example, if
user enters 2534 then your output should be 253)"""

x=int(input("Enter a number"))
y=x//10
print(y)


print(x//10)  # direct way to do it using floor div

print(int(x/10))  # another way to remove float value output