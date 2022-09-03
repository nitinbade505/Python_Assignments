"""Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number."""

x=int(input("enter a number"))
match x:
    case x if x>0 and x%2==0:
        print("saurabh sukla")
    case x if x<0 and x%2==1:
        print("prateek jain")
    case x if x>0 and x%2==1:
        print("Aditya chaudhary")


match x:
    case x if x%2==0:
        print("saurabh sir")
    case x if x<0 and x%2:
        print("prateek sir")
    case x if x>0 and x%2:
        print("aditya sir")