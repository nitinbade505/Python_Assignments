# find out number of "a" in given string, for loop works as per number of elements in iterables.
# for loop iterates a block of code till the number of elements in the iterables

x=input("enter a string ")
count=0
for e in x:                         # for variable in iterable:
    if e=='a':                                   #code
        count+=1                                 #code
print("Count=",count)


x=str('125')   # str(125)   
for e in x:
    #print(x)  # output is number of elemnts time, for 125 print 3 times 125, for aa print 2 times aa
    print(e,end=' ')  # output is like one one elements of x
print()

x=input("enter a string ")    # using break condition
for e in x:
    if e=='r':               # if r found in x string then break works and terminate the code and print already acessed(before r ) elements only
        break                # terminate the code here if found r in x entered string
    print(e,end=' ' )        # access and print entered elements in x  string
else:                          # else works only when break does not work
    print("all character processed")