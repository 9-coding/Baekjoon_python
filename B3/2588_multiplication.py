a = int(input())
b = int(input())

list = list(map(int, str(b)))
list.reverse()

for i in list:
    print(a*i)

print(a*b)