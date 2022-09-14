#Write a python program to create and print a dictionary which stores your information.(name, age, gender …..)

d={'Name':"Nitin",'Age':"30",'Gender':"Male",'Edu':"BE"}
print(d)
print(type(d))

d={'Name':"Nitin",'Age':"30",'Gender':"Male",'Edu':("BE","MBA")}
print(d)
print(type(d))

d={'Name':"Nitin",'Age':"30",'Gender':"Male",'Edu':"BE",'Edu':"MBA"}
print(d)
print(type(d))

d=dict(Name='Nitin',Age='30',Edu='BE')
print(d)
print(type(d))