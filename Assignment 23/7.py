# Create an endless iterator using generator method to produce terms of Fibonacci series

def fibo():
    a,b=0,1
    while True:
        yield a 
        a,b=b,a+b
it=fibo()
#print(next(it),next(it),next(it),next(it),next(it))
n=int(input('enter a number '))
for e in it:
    if e<=n:
        print(e,end=' ')