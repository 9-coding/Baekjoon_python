n, m = map(int, input().split())
basket = []

for i in range(n):
    basket.append(0)

for i in range(m):
    b1, b2, num = map(int, input().split())
    b1 -= 1
    b2 -= 1
    while True:
        basket[b1] = num
        b1 += 1
        if b1 > b2:
            break

for i in range(n):
    print(basket[i], end=" ")