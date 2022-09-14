#Write a python program to get a list of the values from a dictionary.

d={101:'Jack',102:'Sparrow',103:'Kabila',104:'funsuk'}
print(d.values())
print()

for k in d:
    print(d[k],end=' ')
print()

for k in d:
    print(k,end=' ')
