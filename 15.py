def f(a1,a2, x):
    p = 25<=x<=64
    q = 40<=x<=115
    a = a1<=x<=a2
    return p<=((q and (not a))<= (not p))

d = []
for i in (25,64,40,115):
    d.append(i)
    d.append(i+0.1)
    d.append(i-0.1)
h = []
for a1 in d:
    for a2 in d:
        if a1<=a2 and all(f(a1,a2,x) for x in d):
            h.append(a2-a1)
print(min(h))
