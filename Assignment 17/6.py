"""Write a python program to add elements of list to a set
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]"""

s1={"Python", "Django", "JavaScript"}
s2=["Java", "C"]
s1.add(("Java","C"))   # tuple has been added
print(s1)
s1.add("Java")
print(s1)
s1.add("C")
print(s1)
print()
s3=s1.union(s2)
print(s3)
print()

s1.update(["Java","C"])    # error if used add instead of update - unhashable type list
print(s1)
