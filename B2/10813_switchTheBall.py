n, m = map(int, input().split())
basket = []

for i in range(n):
    basket.append(i+1)

for _ in range(m):
    n1, n2 = map(int, input().split())
    n1 -= 1
    n2 -= 1
    if n1 != n2:
        basket[n1], basket[n2] = basket[n2], basket[n1]

for i in range(n):
    print(basket[i], end=" ")