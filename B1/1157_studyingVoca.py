s = str(input()).upper()
set = set(s)
l = []

for i in set:
    l.append(s.count(i))
list = list(set)

if l.count(max(l)) < 2:
    print(list[l.index(max(l))])
else:
    print("?")