# Write a recursive python function to calculate sum of first N odd natural numbers
def f(n):
    if n>0:
        if n==1:
            return 1
        else:
            return 2*n-1 + f(n-1) 
s=f(4)  # 1 + 3 + 5 + 7
print(s)