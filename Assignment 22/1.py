# Write a recursive python function to calculate sum of first N natural numbers

def f(n):
    if n==1:
        return 1
    #s=n+f(n-1)
    return n+f(n-1)  
    #return s 
s=f(6)          # 1+2+3+4+5+6
print(s)
print()

def f(n):
    if n==1:
        return 1
    else:
        return n+f(n-1)
s=f(5)
print(s)