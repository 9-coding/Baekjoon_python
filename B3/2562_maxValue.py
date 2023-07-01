l = []
min = 100

for i in range(9):
    l.append(int(input()))
    if max(l) == l[i]:
        min = i+1

print(max(l))
print(min)