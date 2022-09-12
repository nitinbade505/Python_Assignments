# Write a python program to check if all items in the tuple are the same.

t=(1,1,1,1)
for e in t:
    print(t,end=' ')
    if e==1:
        print('all items same')
    else:  
        print('all items not same')

i=0
while i<len(t):
    print(t[i],end=' ')
    if t[i]==1:
        print('same item')
    else:
        print('No same')
    i+=1