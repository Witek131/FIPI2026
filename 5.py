a = []
for i in range(3 , 150):
    s = f'{i:b}'
    if i %3:
        d = f'{i%3*3:b}'
        s = s + d
    else:
        s = s + s[-3:]
    r = int(s, 2)
    if r >= 200:
        a.append(i)

print(min(a))