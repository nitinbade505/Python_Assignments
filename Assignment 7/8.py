"""Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement"""

x=input("enter 1 string")
y=input("enter 2 string")
match x,y:
    case x,y if x==y:
        print('identical')
    case x,y if x>y:
        print('{} comes before {}'.format(x,y))
    case x,y if x<y:
        print('{} comes after {}'.format(y,x))
    case x,y:                 # case x,y if x!=y:
        print('non identical')
