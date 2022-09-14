# Write a python program to create three dictionaries, then create one dictionary that 
# will contain the other three dictionaries.

d1=dict(a=10,b=20)
print(d1)

d2={'c':11,'d':21}
print(d2)

d3=dict(e=12,f=22)
print(d3)

d1[1]=d2
d1[2]=d3
print(d1)