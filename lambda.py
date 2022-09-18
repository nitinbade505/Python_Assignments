#  Lambda expression --> Lambda is keyword, its a function without def keyword.
# syntax - lanbda input:expression
# eg. lambda a,b:a+b

# lambda expression
f=lambda a,b:a+b
print(f(2,3))
print()

# function 
def add(a,b):
    print(a+b)
add(2,3)

# Recursion using lambda
f=lambda a: a if a==0 else a*(a-1)
print(f(4))