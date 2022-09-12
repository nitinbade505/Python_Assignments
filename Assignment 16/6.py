"""Write a python program to divide the tuple into four variables.
tuple1=(100, 200, 300, 400)"""

t=(100,200,300,400)
print(t)
for e in t:
    print(e,end=' ')
print(type(e))

i=0
while i<len(t):
    print(t[i],end=' ')
    print(type(t[i]))
    i+=1
