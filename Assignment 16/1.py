"""Write a python script to store multiple items in a single variable ( Items are “Java”
,“Python”, “SQL”, “C” ) using tuple"""


t=('Java','Python','SQL','C')
print(t)
print(type(t))

t=('Java','Python','SQL','C')
for e in t:
    print(e,end=' ')
print()

t=('Java','Python','SQL','C')
i=0
while i<len(t):
    print(t[i],end=' ')
    i+=1