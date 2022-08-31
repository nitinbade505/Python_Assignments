"""#
Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some
value to it. Write a python script to import A1 module in A0 and print value of the
variable created in A0.py
#""""

A1.py
x=5

A0.py
print(x)

import A1
print(A1.x)

from A1 import x
print(x)

## Other program in a2, x=5,y=3
import a2
print(a2.x)
print()
from a2 import x,y
print(x,y,sep='\n')
print()
from a2 import y
print(y)
print()
from a2 import x
print(x)
from a2 import *
print(x)