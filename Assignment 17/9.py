#Write a python program to loop through the set and print values
#thisset = {"Python", "Django", "JavaScript", “SQL”}

s= {"Python", "Django", "JavaScript", "SQL"}
print(s)
for e in s:
    print(e)
print()

print({e for e in s})
