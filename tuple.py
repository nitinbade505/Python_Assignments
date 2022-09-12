# Tuple -- It is class, iterable, immutable, hashable, sequence.

# Create tuple
t=(1,2,3,4)    # tuple creation in ()
print(t)
print(type(t))
t=(10,)   # t()  #Tuple
print(t)
print(type(t))
print()

# Access tuple
t=(1,2,3,4,5,6)
print(t,end=' ')    # Access tuple
print(type(t))
print()

for e in t:              # Access tuple 
    print(e,end=' ')
print()

i=0         
while i<len(t):            # Access tuple
    print(t[i],end=' ')
    i+=1
print()

t=(1,2,3,4,5)       # Slicing operator
print(t[2:4:1])

t=print(tuple([int(e) for e in input("enter a number ").split(',')]))


