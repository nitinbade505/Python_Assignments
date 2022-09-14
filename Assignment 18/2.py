#Write a python program to access the items of a dictionary by referring to its key name.

d={101:'Jack',102:'Sparrow',103:'Kabila',104:'funsuk'}
for k in d:
    print(k)
print()

for k in d:
    print(k,d[k])
print()

print(d.items())
print()