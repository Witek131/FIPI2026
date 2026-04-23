def f(n):
    s = 0
    while n>0:
        if n%11 ==0:
            s+=1
        n//=11
    if s == 60:
        return True
    return False

for x in range(3000):
    s = 9*11**210 + 8*11**150 -x
    if f(s):
        print(x)
