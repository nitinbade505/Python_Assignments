#Write a Python script to remove all non int values from a list

l=[10,20,'A',3+1j,True]
print(l)
del l[2]
del l[3]
del l[2]
print(l)
print()

l=[10,20,'A',3+1j,True]
print(l)
l.remove(True)
l.remove('A')
print(l)