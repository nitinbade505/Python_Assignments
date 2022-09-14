"""Write a python program to remove last item of the given set
thisset = {"Python", "Django", "JavaScript", “SQL”}"""

s= {"Python", "Django", "JavaScript", "SQL"}
s.remove("SQL")
print(s)

s= {"Python", "Django", "JavaScript", "SQL"}
s.discard("SQL")
print(s)

s= {"Python", "Django", "JavaScript", "SQL"}
s.pop()
print(s)