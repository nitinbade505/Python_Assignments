#Write a Python script to find if “Python” is present in the set thisset = {"Java","Python", "Django"}

s= {"Java","Python", "Django"}
print(s)
print(type(s))
for e in s:
    if "Python" in e:
        print("present")
print()

print({'present' for e in s if 'Python' in e})