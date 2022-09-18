# Write a recursive python function to calculate sum of first N even natural numbers
def f(n):
    if n==0:
        return n
    else:
        return 2*n+f(n-1)
s=f(4)  #  2+4+6+8
print(s)