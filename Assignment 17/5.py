"""Write a python program to add items from another set to the current set. 
thisset ={"Java", "Python", "SQL"}    secondset= {"C", "Cpp", "NoSQL"}"""

s1={"Java", "Python", "SQL"}
s2={"C", "Cpp", "NoSQL"}
s3=s1.union(s2)
print(s3)
print()

s1.add("A")
s2.add(10)
s1.add("C")
print(s1)
print(s2)