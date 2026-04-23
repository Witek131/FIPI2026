f = open('file\\DEMO_9.csv').readlines()
for i in f:
    s = [int(j) for j in i.split(',')]
    s3 = [j for j in s if s.count(j) == 3]
    s4 = [j for j in s if s.count(j) == 1]
    if len(s3) == 3 and len(s4) == 4 and sum(s4)/4 <= s3[0]:
        sw = sum(s)
print(sw)

