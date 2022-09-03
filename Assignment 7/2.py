"""Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division"""

print("1. addition")
print("2. substraction")
print("3. multiplication")
print("4. division")
menu=int(input())
match menu:
    case 1:
        print("enter two numbers")
        a,b=int(input()),int(input())
        c=a+b
        print("sum is", c)
    case 2:
        print("enter two numbers")
        a,b=int(input()),int(input())
        c=a-b
        print("substr is", c)
    case 3:
        print("enter two numbers")
        a,b=int(input()),int(input())
        c=a*b
        print("multi is", c)
    case 4:
        print("enter two numbers")
        a,b=int(input()),int(input())
        c=a/b
        print("divi is", c)
    case 5:
        exit()                              # exit() kill the program
    case _:
        print("No menui")
    