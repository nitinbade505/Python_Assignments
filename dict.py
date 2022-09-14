# Dictionary - dict --> It is a class, mutable, iterable, not hashable, not a sequence, not a duplicate value,
# indexing not applicable, slicing not applicable.
# It is pair of key value and data value 

d={101:"Rahul",103:"Payal",106:"Arjun",107:"Prachi"}  # 102- Key Value, Rahul - Data value
print(d)
print(type(d))
print()

d=dict(a=10,b=20,c=30)   # a- Key value , 10= data value, Key does not dulicate and repeat not possible.
print(d)
print(type(d))
print()

# Accessing dict elements
d={101:"Rahul",103:"Payal",106:"Arjun",107:"Prachi"}
print(d[106],d[101],d[103])
print()

for k in d:
    print(k,d[k])  # print(k)  --> only print keys
print()

# Edit dict element  --> change only data value not key value element
del d[101]   # [key-value] 
print(d)
print()

d[101]="Ram"   # adding new data value for 101 key value and editing 103 data value
d[103]="Sita"
print(d)
print()

# Methods
print(d.items())
print(type(d.items()))
print(d.keys())
print(type(d.keys()))
print(d.values())
print(type(d.values()))
print()

# Builtin methods
print(len(d))
print(min(d))
print(max(d))
print(sum(d))
print(sorted(d))

# Object methods
print(d)
print(d.pop(101))   # required to pass argument #error print(d.pop())   # required to pass argument
print(d.popitem())  # argument is not required #eror print(d.popitem(101))  # argument is not required
print(d)
print(d.clear())
print(d)
print()

# Comprehension 

d={101:"Rahul",103:"Payal",106:"Arjun",107:"Prachi"}
print(d)
print({(k,d[k]) for k in d}) # print key-value and data-value
print({k for k in d})    # print key value
print({d[k] for k in d})     # print data value
