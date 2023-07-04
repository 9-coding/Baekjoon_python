n = []
m = []
r = []
c = []

for i in range(9):
    n.append(list(map(int, input().split())))
    m.append(max(n[i]))
    c.append(n[i].index(max(n[i])))
    r.append(i)

print(max(m))
print(r[m.index(max(m))]+1, c[m.index(max(m))]+1)