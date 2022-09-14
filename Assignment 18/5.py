#Write a python program to print all key names in the dictionary, one by one.

d={101:'Jack',102:'Sparrow',103:'Kabila',104:'funsuk'}
print(d.values())
print()

for k in d:
    print(k,end=' ')
print()
print()

for k in d:
    print(k)
print()

for k in d:
    print(d[k])
print()

for k in d:
    print(d[k],end=' ')