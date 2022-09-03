"""Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary part"""

#x=eval(input("enter a number"))   
x=complex(input("enter a nuimber"))
if x.real>x.imag:
    print("greater number is real", x.real)
else:
    print("greter number is imag", x.imag)


print(x.real) if x.real>x.imag else print(x.imag)