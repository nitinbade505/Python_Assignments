# match and case are soft keywords, you can use as varible that is why called soft keyword
# as, else, if, from, or  you can not use as varible
# it print output of match case only

match=4
print(match)

#as=4
#print(as)

# eval convert data as per input you can input different data using eval
# if two cases have same value like case 1 and case 1 its gives ouput as first case on priority
x=eval(input('enter a number '))   # instead of int use eval function for 2.1, True, 3 etc
match x:
    case 1:
        print('one')
    case 2:
        print('two')
    case 3.1:                     # we can also use case -3, 2.1, True like this
        print('three')
    case _:                     # this is ( _: wildcard) use for not match value (case _:)
        print("not match")