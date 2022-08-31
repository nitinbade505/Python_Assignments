"""Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and
display the result in binary format."""


x=0o25
y=0x39
z=bin(x+y)
print(z)

x=0o25
a=bin(x)
y=0x39
b=bin(y)
print(a+b)     # result of this wrong becauase a+b operation result 0b101010b111001 alway conccat in str
print(bin(x)+bin(y))   # result of this wrong becauase a+b operation result 0b101010b111001 alway conccat in str
print(bin(x+y))