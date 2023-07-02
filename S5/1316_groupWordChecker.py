n = int(input())
result = 0

for i in range(n):
    s = str(input())
    chk = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            i += 1
        elif s[i+1:].find(s[i]) != -1:
            chk = -1
            break
    if chk == 0:
        result += 1

print(result)