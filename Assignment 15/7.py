# Write a python script to determine whether a string contains a specific substring

a="hi how are you hi" # fullstring
b="hi"               # sybstring
if b in a:
    print("substring found")
else:
    print("not found")
print('found' if b in a else 'not found')  # oneline if-else
print()


s="hi how are you hi"
print(len(s))
print(s.count('i'))
print(s.split(' '))
print()

for e in s:
        print(e,end='')
print()
print(type(e))

i=0
while i<len(s):
    print(s[i],end='')
    i+=1
print()
print(type(s))
print()