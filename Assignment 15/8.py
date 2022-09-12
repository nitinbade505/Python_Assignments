#Write a python script to check if a string contains only numbers.

s='12345'
for e in s:
    print(e,end='')
print()
if '12345' in s:
    print('only Number')
else:
    print('No Number')