"""Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year"""

x=int(input("enter a year"))
match x:
    case x if x%400==0 and x%100==0:
        print("century leap year")
    case x if x%4==0 and x%100!=0:
        print("non century leap year ")
    case x if x%100==0:
        print('century non leap year')
    case x:
        print('non century non leap year')