# Accessing range elements 
import code

# Given range printing
r=range(2,10,2)         # range (begin, end, step)    =range(inclusive, exclusive, comman gap)
for e in r:             # r is an element of range, e is variable
    print(e,end=' ')
print()

# N number range printing
r=range (int(input("enter a number ")))  # for single number range strat value is 0 and end value is enter value with step 1
for e in r:
    print(e,end=' ')
print()

# Reverse range printing
r=range(10,2,-2)
for e in r:
    print(e,end=' ')
print()

# N natural number printing
r=range (int(input("enter a number ")))  # for single number range strat value is 0 and end value is enter value with step 1
for e in r:
    print(e+1,end=' ')
print()

# squares of first N natural numbers
r=range(int(input("enter a number ")))
for e in r:
    print((e+1)**2,end=' ')
print()

# N even natural number in reverse order
r=range(2*int(input("enter a number ")),0,-2)
for e in r:
    if e%2==0:
        print(e,end=' ')
print()

# N even natural number in reverse order
r=range(2*int(input("enter a number ")),0,-2)
for e in r:
    print(e,end=' ')
print()
