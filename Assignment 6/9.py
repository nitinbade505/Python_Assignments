#Write a python script to check whether a given year is a leap year or not.
x=int(input("enter a days of year ")) # 365 not leap # 366 leap year
if x<=365:
    print("not leap year")
else:
    print("leap year")

print("leap" if int(input("enter a days of year"))>=366 else "not leap")


print(("enter a year"))
year=int(input())
if year%400==0 or year%100!=0 and year%4==0:
    print("leap year")
else:
    print("non leap year")
