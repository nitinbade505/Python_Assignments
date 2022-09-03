"""Write a python script to take the month value in numeric format and display the
number of days in it."""
print("enter a month value")
x=int(input())
a=(1,3,5,7,8,10,12) # 31 days month
b=(4,6,9,11)   # 30 days month
if x in a:
    print("31 days")
elif x in b:
    print("30 days")
else:
    print("28 or 29 days")


month=int(input("enter a number"))
if month in (1,3,5,7,8,10,12):
    print("31 days")
elif month in (4,6,9,11):
    print("30 days")
elif month ==2:
    print("28 or 29 days")
else:
    print("Inavalid")


print("31 days"  if x in a else ("28 or 29 days" if x==2 else "30 days") )


