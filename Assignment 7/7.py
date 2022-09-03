"""Write a python program to check whether a given number is positive, negative or
zero using match case statement"""

x= int(input("enter a number"))
match x:
    case x if x>0:
        print('positive')
    case x if x<0:
        print('negative')
    case _:                                   #case x if x==0:
        print('zero')