s = str(input())
l = [-1] * 26

for i in range(len(s)):
    if l[ord(s[i]) - 97] == -1:
        l[ord(s[i]) - 97] = i

for i in range(len(l)):
    print("%d" % l[i], end=' ')