from itertools import *
k = 0
for i in product('АКОРСТ', repeat = 5):
    i = ''.join(i)
    k+=1
    if i[0] not in 'АСТ' and i.count('О') == 2:
        e = k
print(e)