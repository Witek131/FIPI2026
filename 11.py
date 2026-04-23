from math import *
for i in range(1, 1000):
    b = ceil(log2(i))
    n = ceil((2783 * b)/8)
    if 3845627*n < 11*2**30:
        print(i, b)
