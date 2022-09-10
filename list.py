
# list example 
l=[1,2,3,4,5]
print(l)
print(type(l))
print()

l1=[10,20,'A',True,3+4j]   # heterogeneous type list conatin all data types
print(l1)
print(type(l1))
print()

print(l[2])
print(type(l[2]))   # find type of list and access element from list
print()

del l[2]     # delete element from list
print(l)
print()

l[2]=10       # edit list 
print(l)
print()

for x in l:           # delete the number using for loop and index number 
    if x==l[0]:
        del l[0]
print(l)
print()

l.append(10)  # add element in list, it should be go to last index
print(l)
print()

l.insert(1,20)  # add element in middle of list at particular index
print(l)
print()

l.insert(9,12) # add element at any index greater than last indes of list should be add at last index of list
print(l)
print()

a,b,c,d,e,f=l   # unpacking, variables should be equal to elements
print(f,c)
print()

l=[a,e,f,c]     # packing
print(l)
print()

# Built in methods
print(len(l))
print(min(l))
print(max(l))
print(sum(l))
print(sorted(l))
print()

# list() methods
l1=list('mysrig')
print(l1)
print()

# Comparison operator on list
l1=[1,2,3]
l2=[2,3,1]
l3=[1,2,3] 
print(l1==l2)     # not match result is false
print(l1==l3)     # match result is true
print(l1+l2)     # concatenation on list
print(l1*3)     # repetation operator
print()

# list of lists
l=[[1,2,3],[3,2,4]]  # first list index 0, sencond list index 1
print(l[0])          # output list index 0
print(l[0][2])       # list index 0, and inside that list index 2
print()

# list comprehension -- create list 
# [expression for variable in iterable]
ll=[x for x in range(5)]
print(ll)
ll=[x*3 for x in range(5)]
print(ll)

ll=[print(x,end=' ') for x in range(5)]
print(type(ll))
print()

# user input
print('enter a list ')
ll=list(input())
print(ll)

# another way to take user input
print('how many numbers ')
n=int(input())
print('enter a numbers ')
ll=[]
i=0
while i<n:
    ll.append(int(input()))
    i+=1
print(ll)