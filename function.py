# Function is "block of code" which only "runs" when its "called"
# Its has name for identification --> eg. def add(), def subs(), def multi() -- def is keyword
# You can called function multiple times. You can called function form anywhere(in the middle of code) in code.

def add():
    a=int(input("enter a number "))
    b=int(input("enter a number "))
    c=a+b
    print("Sum is",c)
add()          # called function first time
add()          # called function second time
print("hi")
print('bye')
add()          # called function third time after some code(middle of code)
print(add())   # you can called like this way as well
print()

# Ways to define funcions
# 1. Takes nothing, return nothing
# def add()  -- TN - takes nothing means no arguments in functiopn, does not have "return keyword" in program means return nothing

#2. Takes something, return nothing
# def add(a,b) -- add(2,3) - TS means (a,b) formal arguments is present and (2,3) actual argument presnet in function.

#3. Takes Nothing, return something
# def add() --return --add() - TN means no argumets in function takes nothing and  "return keyword" in program means return something

#4. Takes something, return something
# def add(a,b) --return --add(2,3) - Its means arguments and return keyword present in program

# Default Arguments --> Value is assigned by using the assignment (=) operator.
def add (a,b,c=1):      # You can use any value in default argument c=0,c=1,c=2 etc
    s=a+b+c
    return s
print(add(2,3))
print(add(2,3,10))

def add(a,b,c=0,d=0):   # (a,b=0,c) SyntaxError: non-default argument follows default argument
    s=a+b+c+d
    return s
print(add(2,3,4,5))

# Return Something  -- What you aren expecting in a ? None
def f():
    print('Hello')
a=f()
print(a)
print(type(a))      # <class 'NoneType'>
print()

# Positional vs Keyword Arguments
def f(a,b):
    print("a=",a,"b=",b)
f(2,3)        # Positiona; arguments
f(b=2,a=3)    # Keyword arguments
# f(2,a=4)      TypeError: f() got multiple values for argument 'a'
f(5,b=4)
# f(a=2,b)    SyntaxError: positional argument follows keyword argument
print()

# Variable lenght arguments   --> (*t) "t" is tuple here
def f (*t):
    print(t)
f(10)
f(10,20,30)
f(10,20,30,40)