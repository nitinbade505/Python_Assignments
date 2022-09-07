# while loop iterates a block of code till the specified condition is true
# if condition false code terminated at that coondition.

i=1                         # assign i=1
while i<=5:
    print("MySirG")
    i+=1                    # increment by 1
print()

i=1
while i<=3:
    print("Hello", end=" ")   # to print output in one line with separated by space
    i=i+1                    # increment by 1
print()

i=1
while i<=10:
    print(i,end =' ')
    i+=1
print()

i=10
while i>=1:           # i>0 or i or i>=1
    print(i,end=' ')
    i=i-1                 # decrement for reverse order output
print()

while i>1:
    pass
print()

i=1
x=int(input('enter a number'))
while i<=10:
    if x%2==0:
        continue
    print(i,"=x",x)
    i+=1

i=1
while i<=10:
    if i%2==0:
        break
    print("odd")
    i+=1