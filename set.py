# set -- it is class, iterable, mutable, not hasable, not sequence, does not have duplicate value, 
# no indexing method, no slicing operator

# Create set
s1={1,5,8}
print(s1)     # output does not have order
s2={10,2,8,10,8}   # duplicate not allowed in output # Discard the duplicate value
print(s2)
s3={}       # not a set
s4=set()
s5=([1,5,3])   # only one argument pass, that should be iterable here is one list pass 
print(s5)
s6={10,}
print(s6)
print(type(s6))
print()

for e in s2:
    print(e,end=' ')
print()

#builtin methods
print(len(s2))
print(min(s2))
print(max(s2))
print(sum(s2))
print(sorted(s2))
print()

# concatenation and repeation 
#set1 + set2    # not suppoeted
#set * int   # not supported
# >, < , >= , <=  -- not getting reliable result  == , !=   supported

#set object methods
# add(), update() , discard(), remove(), union(), clear(), pop() etc
s1={1,2,3,4,5}
s2={6,7,8,9}
print(s1,s2)
print(s1)

s1.add(10)
print(s1)
s1.update('A','B')
print(s1)
s1.discard(10)
print(s1)
s1.remove('A')
print(s1)
s3=s1.intersection(s2)
print(s3)
s3=s1.union(s2)
print(s3)
print()

# set comprehension
# s={expression for e in objet}
s1={1,2,3,4,5}
for e in s1:
    print(e,end=' ')
print()

print({e for e in s1})
