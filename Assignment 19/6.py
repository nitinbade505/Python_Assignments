# Write a python program to create a function that finds a maximum of four numbers.

def fun(a,b,c,d):
    print([a,b,c,d])
    print([max(a,b,c,d)])
fun(7,8,13,4)
fun(20,60,30,20)
print()

def fun(a):
    print(a)
    print(max(a))
fun(list(input('enter a number ')))
