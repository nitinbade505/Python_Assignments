"""Write a python program to check whether a given string is a multiword string or single
word string using match case statement"""

x=input("enter a string : ")
match x:
    case x if " " in x:
        print("multiword string")
    case x:
        print("single word string")

match x:
    case x if ' ' in x:
        print('multiword')
    case x if '' in x:        # if ' ' not in x: also work here
        print('singlword')
    