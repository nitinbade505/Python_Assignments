# Create an endless iterator using generator method to produce Prime numbers

def prime():
    a=1
    while True:
        yield a 
        a+=1
it=prime()
#print(next(it),next(it),next(it),next(it),next(it))
n=int(input('enter a number '))
for e in it:
    if e<=n:
        print(e,end=' ')
