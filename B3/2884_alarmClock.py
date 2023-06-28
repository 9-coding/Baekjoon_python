h, m = map(int, input().split())

if m >= 45:
    print("{0} {1}".format(h, m-45))
elif h > 0 and m < 45:
    print("{0} {1}".format(h-1, m+15))
elif h == 0 and m < 45:
    print("23 {0}".format(m+15))