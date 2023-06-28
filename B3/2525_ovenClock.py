h, m = map(int, input().split())
t = int(input())

m = h * 60 + m
t = m + t

if int(t/60) >= 24:
    h = int(t/60) - 24
else:
    h = int(t/60)
    
print("{0} {1}".format(h, t%60))