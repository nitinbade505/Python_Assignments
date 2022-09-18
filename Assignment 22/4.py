# Write a recursive python function to calculate sum of squares of first N natural numbers

def f(n):
    if n==1:
        return 1
    else:
        return n*n+f(n-1)
s=f(4)  # 1*1 + 2*2 + 3* 3 + 4*4
print(s)