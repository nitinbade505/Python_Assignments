#Write a python script to calculate simple interest

# simple interest = (principal*interest*time)100

principal=int(input('enter a principal'))
interest = float(input('enter a interest'))
time=int(input('enter a duration of time'))
si=(principal*interest*time)/100
print(si) 