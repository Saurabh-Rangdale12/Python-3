# F- String

import math

me = "Saurabh"
al = 3

a = "This is %s %s"%(me, al)

b = "This is {1} {0}"
c = b.format(me, al)
print(c)

k = f"this is {me} {al} {math.cos(90)}"  # this is f string

print(k)