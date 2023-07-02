s = list(input())
time = 0
thres = [4, 7, 10, 13, 16, 20, 23]

for i in s:
    n = ord(i)-64
    thres.insert(0, n)
    thres.sort()
    sec = thres.index(n) + 3
    if thres.count(n) == 2: 
        sec += 1
    time += sec
    thres.remove(n)

print(time)