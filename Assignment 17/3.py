#Write a python script to get the data type of a Set.

s={10,20,'A',3+4j,True,(10,20),range(2)}
print(s)
print(type(s))
for e in s:
    print(e,end=' ')
    print(type(e))
    