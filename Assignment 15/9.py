#Write a python script to check if a string contains only characters of the alphabet.

s='abcd'
for e in s:
    print(e,end='')
print()
if 'abcd' in s:
    print('only character')
else:
    print('No character')