from itertools import *
for x,y,z,w in product((0,1) , repeat = 4):
    f = (x or y) and(not (y== z)) and(not w)
    if f:
        print(z,y,x,w)
