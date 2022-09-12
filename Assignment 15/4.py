"""Write a python script to demonstrate String Concatenation adding space in between (
Given Strings a=”Learning” b=”Python” )"""
a="Learning"
b="Python"
s=a+b
print(s)
print(a+b)
print(s.split(' '))
print(''.join(s))
print(a+' '+b)     # correct way to add with space