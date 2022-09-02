"""Write a python script to use IS operator to display if both variables are the same
object or not?"""

x=10
print(x is 10)
print(10 is x)
print()

print(id(x))
print(id(10))
print()

print(x is 10 and id(x))   # if  x is 11 its show result false in output
print(10 is x and id(10))   # if 10 is x true then shows id result

print(x is not 10 and id(x))
print(10 is not x and id(10))