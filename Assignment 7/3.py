"""Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit."""

print("1. isoseles tringle or not")  # two side same lengh
print("2. right angle triangle or not") # x**2==y**2+z**2 # angle is 90 degrr
print("3. equilateral triangle or not") # all side same lenght
print("4. exit")
menu= int(input("enter a choice"))
match menu:
    case 1:
        print("enter 3 number")
        x,y,z=int(input()),int(input()),int(input())
        if x==y or y==z or x==z:
            print("isoles traingle")
        else:
            print("Not isoseles triangle")
    case 2:
        print("enter 3 numbers")
        x,y,z=int(input()),int(input()),int(input())
        if x==90:         # 90 degree angle
            print("right andgle triangle")
        elif y==90:
            print("right angle triangle")
        elif z==90:
            print("right angle triangle")
        else:
            print("not right angle triangle")
    case 3:
        print("enter a 3 numbers")
        x,y,z=int(input()),int(input()),int(input())
        if x==y==z:
            print("equilateral triangle")
        else:
            print("not equilateal triangle")
    case 4:
        exit()

