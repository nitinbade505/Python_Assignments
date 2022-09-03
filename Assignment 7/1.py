#Write a python script to display the number of days in a given month number.

x=eval(input("enter month number"))
#y=int(input("enter month number"))
match x in (1,3,5,7,8,10,12):
    case 1:
        print("31 days")
match x in (4,6,9,11):
    case 1:
        print("30 days")
match x==2:
    case 1:
        print("28 or 29 days")


month=int(input("enter a month number"))
match month:
    case month if month in (1,3,5,7,8,10,12):
        print("31 Days")
    case month if month in (4,6,9,11):
        print("30 Days")
    case 2:
        print("28 or 29 Days")
    case _:
        print("Invalid")