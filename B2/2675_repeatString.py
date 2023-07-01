n = int(input())

for i in range(n):
    r, s = map(str, input().split())
    for i in range(len(s)):
        print(s[i] * int(r), end='')
    print()