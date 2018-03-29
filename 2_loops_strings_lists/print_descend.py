a = int(input())
max1 = a
min2 = a
b = int(input())
if max1 < b:
    max1 = b
else:
    max2 = b
c = int(input())
if c > max1:
    print(c)
    print(min2)
    print(max1)
else:
    print(max1)
    if c < max2:
        print(c)
        print(max2)
    else:
        print(max2)
        print(c)