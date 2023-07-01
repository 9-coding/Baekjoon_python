n = int(input())
l = list(map(int, input().split()))
print(100 * sum(l) / (max(l)*n))