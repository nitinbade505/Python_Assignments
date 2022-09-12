# str - it is class, immutable, iterable, hashable, sequence

x=4.5
print(hash(x))    # Hash value is fixed for lifetime
print(id(x))      # Id is different every time its not fixed
print()

s="MySirG"                  # Access str 
print(s[0])  
print(s[-2])
print(s,end=' ')
print()

s='Guruji'               # Access using for loop
for a in s:
    print(a,end='')
print()

i=0
while i<len(s):
    print(s[i],end='')
    i+=1
print()

# Builtin methods
print(len(s))
print(min(s))     # depends on unicode value
print(max(s))    # depends on unicode value
print(sorted(s))   # arrange in ascending order 
print()

# str formating
s="{},Welcome"
print(s.format('Nitin'))
a,b=4,5
s="value of a is {} and b is {}"
print(s.format(a,b))
print()

# split and join 
s="my sir ji great"
print(s.split(' '))
s="10,20,30,40"
print(s.split(','))
print()
s="1,2,3,4"
print(s.split(','))
print([int(e) for e in s.split(',')])
# join 
s='my sir gi is great'
print(s.split(' '))   # split separated by ' '
print(''.join(s))   # join by ' '

# Slicing  -- work on index
s="hi how are you"
print(s[0:12:1])
print(s[12:0:-1])
print(s[::-1])     # reverse the string

l=[1,2,3,4,5]     # slicing work on list as well
print(l[1:4:1])