s = str(input())
result = len(s)
a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in a:
    if s.find(i) != -1:
        result -= s.count(i)

print(result)