import string
a = string.ascii_lowercase

for i in '0123456789' + a[:19]:
    s = int(f'923{i}874', 29) + int(f'524{i}6152', 29)
    if s%28==0:
        print(s//28)