n, m = map(int, input().split())
l = []
mid = []

for i in range(n):
    l.append(i+1)

for i in range(m):
    a, b = map(int, input().split())
    mid = l[a-1:b]
    mid.reverse()
    l = l[0:a-1] + mid + l[b:]

for i in range(n):
    print("{0}".format(l[i]), end=' ')